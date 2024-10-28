from flask import render_template, flash, redirect, url_for, request
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import check_password_hash
from wtforms.validators import email

from game_top import app
from game_top.forms import LoginForm, RegisterForm, GameForm
from game_top import db
import sqlalchemy as sa
from game_top.models import User, AvgRating, PersonalRating, update_avg_rating


@app.route('/rating', methods=['GET', 'POST'])
@login_required
def rating():
    form = GameForm()
    total_score = 0
    if form.validate_on_submit():
        user_game = db.session.scalar(sa.select(PersonalRating).where(
            (PersonalRating.author == current_user.username) &
            (PersonalRating.game_name == form.game_name.data)
        ))
        if user_game:
            flash('Вы уже оценивали эту игру')
            return redirect('rating')


        total_score = (form.originality.data + form.gameplay.data + form.story.data + form.bugs.data + form.graphics.data + form.sound.data + form.music.data + form.design.data +
                   form.atmosphere.data + form.general_impression.data)

        new_rating = PersonalRating(game_name=form.game_name.data, author=current_user.username, originality=form.originality.data, gameplay=form.gameplay.data, story=form.story.data, bugs=form.bugs.data, graphics=form.graphics.data,
                        sound=form.sound.data, music=form.music.data, design=form.design.data, atmosphere=form.atmosphere.data, general_impression=form.general_impression.data, total_score=total_score)

        db.session.add(new_rating)
        db.session.commit()
        update_avg_rating()
        return redirect(url_for('rating'))


    return render_template('rating.html', form=form, total_score=total_score)


@app.route('/', methods=['GET', 'POST'])
def index():
    game_rating = AvgRating.query.all()
    return render_template('index.html', game_rating=game_rating)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(sa.select(User).where(User.username == form.username.data))
        if user is None or not user.check_password(form.password.data):
            flash('Неправильно введен логин или пароль')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Вы успешно зарегистрированы!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)



@app.route('/profile/<username>')
def profile(username):
    user = db.first_or_404(sa.select(User).where(User.username == username))
    return render_template('profile.html', user=user)



@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

