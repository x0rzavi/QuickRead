from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, InputRequired

class AnalyzeForm(FlaskForm):
    url = StringField('Enter article link to analyze:', validators=[InputRequired()])
    submit = SubmitField('GodSpeed!')