from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5

from game_top import db, login
import sqlalchemy as sa
from sqlalchemy import func
import sqlalchemy.orm as so
from typing import Optional

class User(UserMixin, db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(64), index=True, unique=True)
    email: so.Mapped[str] = so.mapped_column(sa.String(120), index=True, unique=True)
    password_hash: so.Mapped[Optional[str]] = so.mapped_column(sa.String(256))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return f'https://www.gravatar.com/avatar/{digest}?d=identicon&s={size}'

    def __repr__(self):
        return f'<User {self.username}>'


class AvgRating(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    game_name: so.Mapped[str] = so.mapped_column(sa.String(100), unique=True, nullable=False)
    avg_originality: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_gameplay: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_story: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_bugs: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_graphics: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_sound: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_music: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_design: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_atmosphere: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_general_impression: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    avg_total_score: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)

    def __repr__(self):
        return f'Game: {self.game_name}'


class PersonalRating(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    game_name: so.Mapped[str] = so.mapped_column(sa.String(100), nullable=False)
    author: so.Mapped[int] = so.mapped_column(sa.String(64), nullable=False)
    originality: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    gameplay: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    story: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    bugs: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    graphics: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    sound: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    music: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    design: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    atmosphere: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    general_impression: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)
    total_score: so.Mapped[int] = so.mapped_column(sa.Integer(), nullable=False)



@login.user_loader
def load_user(id):
    return db.session.get(User, int(id))

def update_avg_rating():
    avg_data = db.session.query(
        PersonalRating.game_name,
        func.avg(PersonalRating.originality).label('avg_originality'),
        func.avg(PersonalRating.gameplay).label('avg_gameplay'),
        func.avg(PersonalRating.story).label('avg_story'),
        func.avg(PersonalRating.bugs).label('avg_bugs'),
        func.avg(PersonalRating.graphics).label('avg_graphics'),
        func.avg(PersonalRating.sound).label('avg_sound'),
        func.avg(PersonalRating.music).label('avg_music'),
        func.avg(PersonalRating.design).label('avg_design'),
        func.avg(PersonalRating.atmosphere).label('avg_atmosphere'),
        func.avg(PersonalRating.general_impression).label('avg_general_impression'),
        func.avg(PersonalRating.total_score).label('avg_total_score')
    ).group_by(PersonalRating.game_name).all()

    for data in avg_data:
        avg_rating = AvgRating.query.filter_by(game_name=data.game_name).first()

        if avg_rating:
            avg_rating.avg_originality = round(data.avg_originality)
            avg_rating.avg_gameplay = round(data.avg_gameplay)
            avg_rating.avg_story = round(data.avg_story)
            avg_rating.avg_bugs = round(data.avg_bugs)
            avg_rating.avg_graphics = round(data.avg_graphics)
            avg_rating.avg_sound = round(data.avg_sound)
            avg_rating.avg_music = round(data.avg_music)
            avg_rating.avg_design = round(data.avg_design)
            avg_rating.avg_atmosphere = round(data.avg_atmosphere)
            avg_rating.avg_general_impression = round(data.avg_general_impression)
            avg_rating.avg_total_score = round(data.avg_total_score)
        else:
            avg_rating = AvgRating(
                game_name=data.game_name,
                avg_originality=round(data.avg_originality),
                avg_gameplay=round(data.avg_gameplay),
                avg_story=round(data.avg_story),
                avg_bugs=round(data.avg_bugs),
                avg_graphics=round(data.avg_graphics),
                avg_sound=round(data.avg_sound),
                avg_music=round(data.avg_music),
                avg_design=round(data.avg_design),
                avg_atmosphere=round(data.avg_atmosphere),
                avg_general_impression=round(data.avg_general_impression),
                avg_total_score=round(data.avg_total_score)
            )
            db.session.add(avg_rating)

    db.session.commit()
