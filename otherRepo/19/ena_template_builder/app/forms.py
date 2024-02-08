"""Forms for the application."""

import wtforms_json
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField

wtforms_json.init()


class MyForm(FlaskForm):

    class Meta:
        csrf = False

    name = StringField('Name')
    age = IntegerField('Age')
    submit = SubmitField('Submit')
