from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('You Email Address',validators=[Required(),Email()])
    username = StringField('Enter your username',validators = [Required()])
    password = PasswordField('Password', validators = [Required() EqualTo('password_confirm',message = 'Password must match')])
    password_confirm = PasswordField('Confirm Password' validators=[Required()])
    submit = SubmitField('Sign Up')