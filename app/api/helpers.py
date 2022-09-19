from flask import current_app, url_for
import re

def remove_html_tags(text):
    """Remove html tags from a string"""
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

def secure_link(*a, **kw):
    return url_for(*a, **kw, _external=True, 
                   _scheme=current_app.config["API_LINKS_SCHEME"])