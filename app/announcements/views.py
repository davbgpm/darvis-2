from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user

from app import db
from app.models import Announcement
from app.announcements.forms import (
    EditAnnouncementForm, 
    AddAnnouncementForm,
    DeleteAnnouncementForm
)
from app.announcements import roles as permissions
from app.announcements import bp
from app.announcements.helpers import send_message


#@bp.route("/")
#@bp.route("/index")
@login_required
@permissions.list_announcements.require()
def list_announcements():
    """list_announcements 
        
    This view function deals with announcement adding.
    It allows us to view the announcements, edit, delete add annc button.
    
    """
    announcements = Announcement.get_all()

    kw = {
        "title" : "All Announcements",
        # "username" : current_user.username,
        "announcements" : announcements
    }

    return render_template("announcements/list.html", **kw)


#@bp.route("/add", methods=['GET', 'POST'])
@login_required
@permissions.add_announcements.require()
def add_announcements():
    """add_announcements 
    
    GUI for adding announcements
    """
    form = AddAnnouncementForm()

    if form.validate_on_submit():
        ann = Announcement(
            title = form.title.data,
            body = form.body.data,
            user_id = current_user.id
        )
        db.session.add(ann)
        db.session.commit()
        send_message(ann)
        flash("Success! Announcement added.", "success")
        return redirect(url_for("announcements.list_announcements"))

    kw = {
        "title" : "Add Announcement",
        "form" : form,
        # "username" : current_user.username
    }

    return render_template('announcements/edit.html', **kw)

#@bp.route("/<int:announcement_id>/edit", methods=['GET', 'POST'])
@login_required
@permissions.edit_announcements.require()
def edit_announcement(announcement_id: int):
    """edit_announcements

    Allows editing of announcements

    Args:
        announcement_id (int): ID in database of announcements
    """

    ann = Announcement.query.filter_by(id=announcement_id).first_or_404()
    ann_name = ann.title
    form = EditAnnouncementForm(obj=ann)

    if form.validate_on_submit():
        ann.title = form.title.data
        ann.body = form.body.data
        db.session.commit()
        flash("Success! Page updated.", "success")
        return redirect(url_for("announcements.list_announcements"))
    
    kw = {
        "title" : f"Editing '{ann_name}'",
        "form" : form,
        "ann_name" : ann_name, 
        # "username" : current_user.username
    }

    return render_template('announcements/edit.html', **kw)

#@bp.route("/<int:announcement_id>/delete", methods=['GET', 'POST'])
@login_required
@permissions.delete_announcements.require()
def delete_announcement(announcement_id: int):
    """delete_announcement
    
    Deletes the announcements, given an id

    Args:
        announcement_id (int): ID in database of announcements
    """

    ann = Announcement.query.filter_by(id=announcement_id).first_or_404()
    ann_name = ann.title
    form = DeleteAnnouncementForm(obj=ann)

    if form.validate_on_submit():
        if form.confirmation.data.lower() == "i am sure":
            db.session.delete(ann)
            db.session.commit()
            flash("Success! Page updated.", "success")
            return redirect(url_for("announcements.list_announcements"))
        else:
            flash("Type the text EXACTLY as shown.", "danger")

    kw = {
        "title" : f"Deleting '{ann_name}'",
        "form" : form,
        "ann_name" : ann_name, 
        # "username" : current_user.username
    }

    return render_template('announcements/delete.html', **kw)