from flask_wtf import FlaskForm
from wtforms.fields.numeric import IntegerRangeField

from game_top import db
from wtforms.fields.simple import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, EqualTo,ValidationError, Email
import sqlalchemy as sa
from game_top.models import User


class LoginForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня')
    submit = SubmitField('Войти')

class RegisterForm(FlaskForm):
    username = StringField('Имя', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField('Повторите пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зарегистрироваться')

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user is not None:
            raise ValidationError('Это имя пользователя занято')

    def validate_email(self, email):
        user = db.session.scalar(sa.select(User).where(User.email == email.data))
        if user is not None:
            raise ValidationError('Этот email уже занят')



class GameForm(FlaskForm):
    game_name = StringField('Название игры', validators=[DataRequired()])

    originality = IntegerRangeField(
        'Originality',
        default=1,
        render_kw={'min':1, 'max':10, 'oninput': 'updateValue(this)'}
    )
    gameplay = IntegerRangeField(
        'Gameplay',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    story = IntegerRangeField(
        'Story',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    bugs = IntegerRangeField(
        'Bugs',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    graphics = IntegerRangeField(
        'Graphics',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    sound= IntegerRangeField(
        'Sound',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    music = IntegerRangeField(
        'Music',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    design = IntegerRangeField(
        'Design',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    atmosphere = IntegerRangeField(
        'Atmosphere',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    general_impression = IntegerRangeField(
        'General Impression',
        default=1,
        render_kw={'min': 1, 'max': 10, 'oninput': 'updateValue(this)'}
    )
    submit = SubmitField('Подтвердить')

