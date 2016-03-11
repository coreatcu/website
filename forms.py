from flask_wtf import Form
from flask.ext.wtf.recaptcha import RecaptchaField
from wtforms import TextField, TextAreaField
from wtforms.validators import DataRequired, Email

class ContactForm(Form):
    name = TextField('Name', validators=[DataRequired()])
    email = TextField('Email', validators=[DataRequired(), Email()])
    subject = TextField('Subject', validators=[DataRequired()])
    message = TextAreaField('Message', validators=[DataRequired()])
    recaptcha = RecaptchaField()