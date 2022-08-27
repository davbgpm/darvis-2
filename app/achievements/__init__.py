from flask import Blueprint

# This is achievements blueprint
bp = Blueprint('achievements', __name__)

from app.achievements import routes