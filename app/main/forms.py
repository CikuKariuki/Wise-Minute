from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    review = TextAreaField('Pitch Review',validators=[Required()])
    submit = SubmitField('submit')

class UpdateProfile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')

class PitchForm(FlaskForm):
    title = StringField("Pitch Title", validators = [Required()])
    content = TextAreaField('Write your pitch here')
    submit = SubmitField('Pitch')