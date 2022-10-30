import datetime

from flask import render_template, flash, redirect, url_for
from flask_login import login_required

from app import db
from app.models import Flight
import app.fids.roles as permissions
from app.fids.forms import AddFlightForm

@login_required
@permissions.list_flights.require()
def list_():
    f = Flight.query.all()
    return render_template("fids/list.html", title="Flight list", data=f)


@login_required
@permissions.add_flights.require()
def add():
    form = AddFlightForm()
    if form.validate_on_submit():
        flight1 = Flight()
        flight1.dep_time = form.dep_time.data
        flight1.flight_code = form.flight_code.data
        flight1.dest = form.dest.data
        flight1.status = form.status.data
        db.session.add(flight1)
        db.session.commit()
        flash("Success")
        
        return redirect(url_for("fids.list_"))
    
    return render_template("fids/edit.html", title="Add Flight", form=form)


@login_required
@permissions.edit_flights.require()
def edit(id):
    pass


@login_required
@permissions.delete_flights.require()
def delete(id):
    pass