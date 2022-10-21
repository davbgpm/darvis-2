from flask import current_app, url_for
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