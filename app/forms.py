from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class SignupForm(FlaskForm):
    fullname = StringField("Full name",  validators=[DataRequired(), Length(min=3, max=64)])
    username  = StringField("Username",  validators=[DataRequired(), Length(min=3, max=64)])
    email     = StringField("Email",     validators=[DataRequired(), Email()])
    password  = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm   = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo("password", message="Passwords must match ❌")])
    agree     = BooleanField("I agree to the terms", validators=[DataRequired()])
    submit    = SubmitField("Register")


class LoginForm(FlaskForm):
    email    = StringField("Email",    validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit   = SubmitField("Login")
