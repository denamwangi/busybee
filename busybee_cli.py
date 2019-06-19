import click
import requests


GROUPS = ['group1', 'group2']
TASKS = ['task 1', 'task 2', 'task 3']
meh = {
	'group1': ['task1','task2'],
	'group2': ['task3'],
	}


@click.group()
def cli():
	pass


@cli.command()
@click.option('--goal', prompt='What goal would you like to add for the week?')
def add_goal(goal):
	'''This adds in a goal for this week'''
	click.echo('K-got it! Added %s to your goals' % goal)
	url = "http://127.0.0.1:5000/add_goal"
	requests.post(url, data = {'goal': goal})


@cli.command()
@click.option('--task', prompt='What did you just complete lovely?')
def add_task(task):
	'''This adds something you accomplished today'''
	click.echo("Nice job on completing %s" % task)
	for i, grp in enumerate(GROUPS):
		click.echo("{} {}".format(i, grp))
	goal_id = click.prompt('what goal should it go under?')	
	click.echo('you picked %s' % goal_id)

	url = "http://127.0.0.1:5000/add_task"
	requests.post(url, data = {'task': task, 'goal_id': goal_id})


@cli.command()
def list():
	'''Shows a grouped list of what you've done'''
	for group in meh:
		click.echo(click.style(group, fg='magenta'))
		for item in meh[group]:
			click.echo('     %s' % item)
