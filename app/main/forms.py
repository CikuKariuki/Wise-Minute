from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class ReviewForm(FlaskForm):
    title = StringField('Review title',validators = [Required()])
    review = TextAreaField('Article Review',validators=[Required()])
    submit = SubmitField('submit')
    