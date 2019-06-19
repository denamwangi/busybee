import os

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError

import models

app = Flask(__name__)

app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


@app.route("/")
def index():
	pass

@app.route("/add_goal", methods=["POST"])
def add_goal():
	data = request.form.get('goal')

	try:
		goal = models.Goal(
			description=data,
		)

		db.session.add(goal)
		db.session.commit()
		return("Successfully added goal")
	except Exception as e:
		return 'bad request bruh', 400


@app.route("/get_goals", methods=["GET"])
def get_goals():
	goals = models.Goal.query.all()
	result = [g.serialize() for g in goals]
	return jsonify(result)

@app.route("/add_task", methods=["POST"])
def add_task():
	description = request.form.get('task')
	goal_id = request.form.get('goal_id')

	try:
		task = models.Task(
			description=description, 
			goal_id=goal_id
		)
		db.session.add(task)
		db.session.commit()
		return("Successfully added task")
	except IntegrityError:
		return 'Bad request bruh. Are you sure this goal exists?', 400


if __name__ == "__main__":
	app.run()
