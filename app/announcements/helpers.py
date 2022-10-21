import threading
import requests

from flask import current_app

from app.models import Announcement

def send_async_tgmsg(app, apikey, channel, id_):
    with app.app_context():
        obj = Announcement.query.get(id_)
        requests.post(f"https://api.telegram.org/bot{apikey}/sendMessage", json={"chat_id": channel, "text": f"Reference # {obj.id} \n<b>{obj.title}</b> \n\n{obj.body}", "parse_mode": "HTML"})

def send_message(obj):
    if current_app.config["TELEGRAM_BOTAPI_USE"]:
        threading.Thread(target=send_async_tgmsg, args=(current_app._get_current_object(), current_app.config["TELEGRAM_BOTAPI_KEY"], current_app.config["TELEGRAM_BOTAPI_CHANNEL"], obj.id)).start()