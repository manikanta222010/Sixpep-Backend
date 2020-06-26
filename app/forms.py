from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Optional
from app.models import User


class LoginForm(FlaskForm):
    mailid = StringField('Email ID', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):

    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    dob = DateField('DOB', format='%m/%d/%Y', validators=[Optional()])
    address = StringField('Address', validators=[Optional()])
    submit = SubmitField('signup')



    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')

    
    def validate_name(self, name):
        user = User.query.filter_by(name=name.data).first()
        if user is not None:
            raise ValidationError('Please enter name.')
            
    def validate_dob(self, dob):
        user = User.query.filter_by(dob=dob.data).first()
        if user is not None:
            raise ValidationError('Please enter a valid date of birth.')