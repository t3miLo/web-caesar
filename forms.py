from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField, widgets
from wtforms.validators import DataRequired, NumberRange


class CaesarForm(FlaskForm):
    rotateBy = IntegerField('Rotate by ', widget=widgets.Input(input_type='number'),
                            validators=[DataRequired(), NumberRange(min=1, max=26)], default=1)
    textArea = TextAreaField('Message to Encrypt',
                             validators=[DataRequired()])
    submit = SubmitField('Encrypt!')
