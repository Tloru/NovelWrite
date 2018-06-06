from datetime import datetime

from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app import login


@login.user_loader
def load_user(id):
	return User.query.get(int(id))


class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(128), unique=True)
	username = db.Column(db.String(32), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	stories = db.relationship('Story', backref='author', lazy='dynamic')

	def __repr__(self):
		return '<User {}>'.format(self.username)

	def __str__(self):
		return self.username

	def set_password(self, password):
		self.password_hash = generate_password_hash(password)

	def check_password(self, password):
		return check_password_hash(self.password_hash, password)


class Story(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64), index=True)
	description = db.Column(db.String(256))
	created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	chapters = db.relationship('Chapter', backref='story', lazy='dynamic')

	def __repr__(self):
		return '<Story {}>'.format(self.title)


class Chapter(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	heading = db.Column(db.String(64), index=True)
	description = db.Column(db.String(256))
	contents = db.Column(db.Text)
	created = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	story_id = db.Column(db.Integer, db.ForeignKey('story.id'))

	def __repr__(self):
		return '<Chapter {}>'.format(self.heading)
