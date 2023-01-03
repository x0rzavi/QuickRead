from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AnalyzeForm(FlaskForm):
    url = StringField('URL', validators=[DataRequired()])
    submit = SubmitField('Analyze')