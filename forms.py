from flask_wtf import Form
from wtforms.fields import TextField, PasswordField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo


class LoginForm(Form):
    username = TextField('Username', validators=[DataRequired(), Length(min=5)])
    password = PasswordField('Passwort', validators=[DataRequired()])
    remember = BooleanField('Remember me', default=False)

class EditPasswordForm(Form):
    old_password = PasswordField('Aktuelles Passwort', validators=[DataRequired()])
    password = PasswordField('Passwort', validators=[DataRequired(), EqualTo('confirm', message='Passwoerter muessen uebereinstimmen!'), Length(min=8)])
    confirm = PasswordField('Passwort wiederholen', validators=[DataRequired()])

class EditUserPasswordForm(Form):
    password = PasswordField('Passwort', validators=[DataRequired(), EqualTo('confirm', message='Passwoerter muessen uebereinstimmen!'), Length(min=8)])
    confirm = PasswordField('Passwort wiederholen', validators=[DataRequired()])

class NewUserForm(Form):
    username = TextField('Username', validators=[DataRequired(), Length(min=5)])
    password = PasswordField('Passwort', validators=[DataRequired()])
    active = BooleanField('Active', default=True)

class EditUserForm(Form):
    username = TextField('Username', validators=[DataRequired(), Length(min=5)])
    active = BooleanField('Active', default=True)

