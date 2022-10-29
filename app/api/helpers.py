import base64
import string
import random

from flask import current_app, url_for
from cryptography.fernet import Fernet
from captcha.image import ImageCaptcha
from PIL import Image

import re

LINK_REGEX = re.compile("https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)")

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def secure_link(*a, **kw):
    return url_for(*a, **kw, _external=True, 
                   _scheme=current_app.config["API_LINKS_SCHEME"])

def clickable_links(content):
    return LINK_REGEX.sub(r'<a href="\g<0>">\g<0></a>', content)

def _encrypt(answer):
    f = Fernet(current_app.config["FERNET_KEY"])
    return base64.b64encode(f.encrypt(bytes(answer, 'utf-8'))).decode('utf-8')

def _decrypt(token):
    f = Fernet(current_app.config["FERNET_KEY"])
    return f.decrypt(base64.b64decode(token), ttl=180).decode('utf-8')

def generate_captcha():
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    image_captcha = ImageCaptcha(width=250, height=125)
    image_generated = image_captcha.generate(random_string)
    tkn = _encrypt(random_string)
    return image_generated, tkn

def check_captcha(tkn, ans):
    try:
        a = _decrypt(tkn)
    except:
        return False
    else:
        return a == ans