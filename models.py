import datetime
from app import db


class Goal(db.Model):
	__tablename__ = 'goal'

	id = db.Column(db.Integer(), primary_key=True)
	date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	description = db.Column(db.String())
	tasks = db.relationship('Task', backref='goal', lazy=True)

	def __init__(self, description):
		self.description = description
	
	def __repr__(self):
		return '<id {}>'.format(self.id)


class Task(db.Model):
	__tablename__ = 'task'

	id = db.Column(db.Integer(), primary_key=True)
	date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
	description = db.Column(db.String())
	goal_id = db.Column(db.Integer, db.ForeignKey('goal.id'),
		nullable=False)

	def __init__(self, description, goal_id):
		self.description = description
		self.goal_id = goal_id
	
	def __repr__(self):
		return '<id {}>'.format(self.id)