from flask import Blueprint

# This is auth blueprint
bp = Blueprint('fids', __name__)

from app.fids import urls