from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remenber me', default=False)
