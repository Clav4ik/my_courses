
from .tg_bot import send_msg_tg
from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)
@shared_task
def check_flag(name, phone):
    logger.info("Sent telegramm message")
    return send_msg_tg(name + '\n' + str(phone))
    # tickets = Ticket.objects.filter(in_procesing=False)
    #
    # if(tickets):
    #     for ticket in tickets:
    #
    #         send_msg_tg(ticket.name+'\n' + str(ticket.phone))
    #         ticket.in_procesing = True
    #         ticket.save()
    #     return 1
    # else: return 0
