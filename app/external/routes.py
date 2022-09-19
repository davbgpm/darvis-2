from flask import render_template, redirect, url_for
from flask_login import login_required, current_user

from app import db
from app.models import Achievement
from app.main import bp

def index():
    """index 
    
    Generate a page with gives links to other apps.
    """
    return "Homepage"


def view_achievement(achievement_id: int):
    """view_achievement 
    
    View Achievements

    Args:
        achievement_id (int): ID of ach
    """
    achievement = Achievement.query.filter_by(id=achievement_id).first_or_404()
    return render_template("external/view_achievement.html", achievement=achievement)

