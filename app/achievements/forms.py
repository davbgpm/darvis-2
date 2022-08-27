from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    BooleanField, 
    SubmitField, 
    TextAreaField,
    SelectField
)
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
# from flask_babel import _, lazy_gettext as _l
from app.models import Achievement

class EditAchievementForm(FlaskForm):
    title = StringField('Achievement Title', validators=[DataRequired()])
    body = TextAreaField('Achievement', validators=[DataRequired()])
    category = SelectField('Category',
                           choices=[
                               ('academics'), 
                               ('cocurricular'), 
                               ('sports')
                               ], 
                           validators=[DataRequired()])
    region = SelectField('region',
                           choices=[
                               ('state'), 
                               ('national'), 
                               ('international')
                               ], 
                           validators=[DataRequired()])
    submit = SubmitField('Update Achievement')


class AddAchievementForm(EditAchievementForm):
    pass
    # title = StringField('Achievement Title', validators=[DataRequired()])
    # body = TextAreaField('Achievement', validators=[DataRequired()], id="summernote")
    submit = SubmitField('Add Achievement')


class DeleteAchievementForm(FlaskForm):
    confirmation = StringField("Type 'I am sure' here to proceed without the quotes",
         validators=[DataRequired()])
    submit = SubmitField('Delete Achievement')