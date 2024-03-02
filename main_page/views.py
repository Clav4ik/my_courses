from django.contrib import messages
from django.shortcuts import render

from .forms import TicketForm
from .tasks import check_flag


def home_page(request):
    form = TicketForm()
    error = ""
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid() and len(request.POST["phone"]) < 13:
            form.save()
            check_flag.delay(form.instance.name, str(form.instance.phone)[3::])
            messages.success(request, "Ви відправили Ім'я {} \n та номер ({})".format(request.POST["name"], request.POST["phone"]))
        else:

            error = 'Форма була невірной'


    context = {
        'form': form,
        'error': error

    }
    return render(request, "index.html", context=context)