from django.conf import settings
import requests
def send_msg_tg(text):
    url = "https://api.telegram.org/bot"+settings.TG_BOT_TOKEN_FULL+"/sendMessage"

    payload = {
        "chat_id": "775207817",
        "text": text,
        "disable_web_page_preview": False,
        "disable_notification": False,
        "reply_to_message_id": 0
    }
    headers = {
        "accept": "application/json",
        "User-Agent": "Telegram Bot SDK - (https://github.com/irazasyed/telegram-bot-sdk)",
        "content-type": "application/json"
    }

    requests.post(url, json=payload, headers=headers)
