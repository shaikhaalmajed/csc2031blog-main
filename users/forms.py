from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Email, ValidationError, EqualTo, Length
import re

def character_check(form, field):
    excluded_chars = "<&%"
    for char in field.data:
        if char in excluded_chars:
            raise ValidationError(f"Character {char} is not allowed.")

def validate_data(form, password):
    p = re.compile(r"(?=.*\d)(?=.*[a-z])")
    if not p.match(password.data):
        raise ValidationError("Must contain 1 digit and must contain 1 lowercase word character")



class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired(),
                                       Email(),
                                       character_check])
    password = PasswordField(validators=[DataRequired(),
                                         character_check,
                                         validate_data,
                                         Length(min=8, max=15)])
    confirm_password = PasswordField(validators=[DataRequired(),
                                                 character_check,

                                                 EqualTo('password', message='Both password fields must be equal!')])

    submit = SubmitField()



