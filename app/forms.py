from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms import BooleanField
from wtforms import TextAreaField
from wtforms.validators import DataRequired
from wtforms.validators import Length


class LoginForm(FlaskForm):
    openid = StringField('openid', validators=[DataRequired()])
    remember_me = BooleanField('remenber me', default=False)


class EditForm(FlaskForm):
    nickname = StringField('nickname', validators=[DataRequired()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=140)])