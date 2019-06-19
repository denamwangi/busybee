import click
import requests


class Config(object):

	def __init__(self):
		url = "http://127.0.0.1:5000/get_goals"
		self.goals = requests.get(url).json()

pass_config = click.make_pass_decorator(Config, ensure=True)

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
@pass_config
def add_task(config, task):
	'''This adds something you accomplished today'''
	click.echo("Nice job on completing %s" % task)

	for group in config.goals:
		click.echo("{} {}".format(group['id'], group['description']))
	goal_id = click.prompt('what goal should it go under?')	
	click.echo('you picked %s' % goal_id)

	url = "http://127.0.0.1:5000/add_task"
	requests.post(url, data = {'task': task, 'goal_id': goal_id})


@cli.command()
@pass_config
def list(config):
	'''Shows a grouped list of what you've done'''
	for group in config.goals:
		click.echo(click.style(group['description'], fg='magenta'))
		for item in group['tasks']:
			click.echo('     %s' % item['description'])
