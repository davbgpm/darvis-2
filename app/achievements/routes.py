from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models import Achievement
from app.achievements.forms import (
    EditAchievementForm, 
    AddAchievementForm,
    DeleteAchievementForm
)
from app.achievements import bp
from app.achievements import roles as permissions


@bp.route("/")
@bp.route("/index")
@login_required
@permissions.list_achievements.require()
def list_achievements():
    """list_achievements 
        
    This view function deals with achievement adding.
    It allows us to view the achievements, edit, delete add achc button.
    
    """
    achievements = Achievement.get_all()

    kw = {
        "title" : "All Achievements",
        # "username" : current_user.username,
        "achievements" : achievements
    }

    return render_template("achievements/list.html", **kw)


@bp.route("/add", methods=['GET', 'POST'])
@login_required
@permissions.add_achievements.require()
def add_achievements():
    """add_achievements 
    
    GUI for adding achievements
    """
    form = AddAchievementForm()

    if form.validate_on_submit():
        ach = Achievement(
            title = form.title.data,
            body = form.body.data,
            user_id = current_user.id,
            category = form.category.data,
            region = form.region.data,
        )   
        db.session.add(ach)
        db.session.commit()
        flash("Success! Achievement added", "success")
        return redirect(url_for("achievements.list_achievements"))

    kw = {
        "title" : "Add Achievement",
        "form" : form,
        # "username" : current_user.username
    }

    return render_template('achievements/edit.html', **kw)

@bp.route("/<int:achievement_id>/edit", methods=['GET', 'POST'])
@login_required
@permissions.edit_achievements.require()
def edit_achievement(achievement_id: int):
    """edit_achievements

    Allows editing of achievements

    Args:
        achievement_id (int): ID in database of achievements
    """
    

    ach = Achievement.query.filter_by(id=achievement_id).first_or_404()
    ach_name = ach.title
    form = EditAchievementForm(obj=ach)

    if form.validate_on_submit():
        ach.title = form.title.data
        ach.body = form.body.data
        ach.category = form.category.data
        ach.region = form.region.data
        
        db.session.commit()
        flash("Success! Achievement updated", "success")
        return redirect(url_for("achievements.list_achievements"))
    
    kw = {
        "title" : f"Editing '{ach_name}'",
        "form" : form,
        "ach_name" : ach_name, 
        # "username" : current_user.username
    }

    return render_template('achievements/edit.html', **kw)

@bp.route("/<int:achievement_id>/delete", methods=['GET', 'POST'])
@login_required
@permissions.delete_achievements.require()
def delete_achievement(achievement_id: int):
    """delete_achievement
    
    Deletes the achievements, given an id

    Args:
        achievement_id (int): ID in database of achievements
    """
    msg = ""

    ach = Achievement.query.filter_by(id=achievement_id).first_or_404()
    ach_name = ach.title
    form = DeleteAchievementForm(obj=ach)

    if form.validate_on_submit():
        if form.confirmation.data.lower() == "i am sure":
            db.session.delete(ach)
            db.session.commit()
            flash("Success! Achievement deleted", "success")
            return redirect(url_for("achievements.list_achievements"))
        else:
            flash("Type the text EXACTLY as shown.", "danger")

    kw = {
        "title" : f"Deleting '{ach_name}'",
        "form" : form,
        "ach_name" : ach_name, 
        # "username" : current_user.username
    }

    return render_template('achievements/delete.html', **kw)