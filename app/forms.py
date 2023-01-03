from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

class AnalyzeForm(FlaskForm):
    data = StringField('Data', validators=[DataRequired()])
    submit = SubmitField('Analyze')