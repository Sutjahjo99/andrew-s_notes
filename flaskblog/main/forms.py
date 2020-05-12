from flask_wtf import FlaskForm, RecaptchaField
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
	email = StringField('Your Email', validators=[DataRequired(), Email()])
	title = StringField('Message Title', validators=[DataRequired()])
	message = TextAreaField('Content', validators=[DataRequired()])
	submit = SubmitField('Send')
	#recaptcha = RecaptchaField()