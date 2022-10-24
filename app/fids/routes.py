from flask import render_template

from app import db
from app.models import Flight
import app.fids.roles as permissions

@permissions.list_flights.require()
def list_():
    f = Flight.query.all()
    return render_template("fids/list.html", title="Flight list", data=f)


@permissions.add_flights.require()
def add():
    pass


@permissions.edit_flights.require()
def edit(id):
    pass


@permissions.delete_flights.require()
def delete(id):
    pass