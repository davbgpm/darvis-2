from flask import Blueprint

# This is auth blueprint
bp = Blueprint('external', __name__)

from app.external import urls