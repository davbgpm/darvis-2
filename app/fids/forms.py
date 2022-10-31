from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateTimeField
from wtforms.validators import DataRequired, ValidationError

from app.models import Flight

class AddFlightForm(FlaskForm):
    dep_time = DateTimeField("Departs at")
    flight_code = StringField("Flight #", validators=[DataRequired()])
    dest = StringField("Destination")
    status = StringField("Status")
    submit = SubmitField("Submit")
    
    def validate_flight_code(self, val):
        if Flight.query.filter_by(flight_code = val.data).first():
            raise ValidationError("flight already existent")