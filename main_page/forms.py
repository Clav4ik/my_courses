from django.forms import ModelForm, TextInput, CharField
from phonenumber_field.formfields import PhoneNumberField

from .models import Ticket
from captcha.fields import CaptchaField

class TicketForm(ModelForm):
    captcha = CaptchaField(error_messages={'invalid': ' Каптча невірна'})

    class Meta:
        model = Ticket
        fields = ("name", "phone", "captcha")
        error_messages = {
            'phone': {
                'invalid': " Помилка у веденому номері",
            },
        }
        widgets = {
            "name": TextInput(attrs={
                "type": "text",
                "placeholder": "Ім'я"
            }),
            "phone": TextInput(attrs={
                "type" : "tel",
                'placeholder': '0556667788'
            })

        }

