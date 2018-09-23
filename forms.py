from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField, IntegerField, widgets, TextField
from wtforms.validators import DataRequired, NumberRange, Length, ValidationError


class CaesarForm(FlaskForm):
    rotateBy = IntegerField('Rotate by ', widget=widgets.Input(input_type='number'),
                            validators=[DataRequired(), NumberRange(min=1, max=26)], default=1)
    textArea = TextAreaField('Message to Encrypt',
                             validators=[DataRequired()])
    submit = SubmitField('Encrypt!')


def validate_keyWord(form, field):
    if field.data.isalpha() is False:
        raise ValidationError(
            'You can only use letters in your keyword.')


class VigenereForm(FlaskForm):

    keyWord = TextField('Enter word for Key ',
                        validators=[DataRequired(), Length(min=2, max=10), validate_keyWord])

    textArea = TextAreaField('Message to Encrypt',
                             validators=[DataRequired()])
    submit = SubmitField('Encrypt!')
