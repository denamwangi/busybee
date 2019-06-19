import click
import requests


class Config(object):

	def __init__(self):
		url = "http://127.0.0.1:5000/get_goals"
		self.goals = requests.get(url).json()

pass_config = click.make_pass_decorator(Config, ensure=True)

@click.group()
def cli():
	'''Sup! This tool will help you easily log your goals and related tasks'''
	pass


@cli.command()
def add_goal():
	'''This adds in a goal for this week U+1F41D'''
	more = 'yes'
	while more == 'yes':
		goal = click.prompt('What goal would you like to add for the week?')
		click.echo('K-got it! Added %s to your goals' % goal)
		url = "http://127.0.0.1:5000/add_goal"
		requests.post(url, data = {'goal': goal})
		more = click.prompt('Want to add another one?', type=click.Choice(['yes', 'no']))


@cli.command()
@pass_config
def add_task(config):
	'''This adds something you accomplished today'''
	more = 'y'
	while more == 'y':
		task = click.prompt('What did you just accomplish lovely?')
		click.echo("Nice job on completing %s" % task)

		for group in config.goals:
			click.echo("{} {}".format(group['id'], group['description']))
		goal_id = click.prompt('what goal should it go under?')	
		click.echo('you picked %s' % goal_id)

		url = "http://127.0.0.1:5000/add_task"
		response = requests.post(url, data = {'task': task, 'goal_id': goal_id})

		if response.status_code == 400:
			click.echo(response.text + '...try again')
		else:
			more = click.prompt('Want to add another?', type=click.Choice(['y', 'n']))



@cli.command()
@pass_config
def list(config):
	'''Shows a grouped list of what you've done'''
	for group in config.goals:
		click.echo(click.style(group['description'], fg='magenta'))
		for item in group['tasks']:
			click.echo('     %s' % item['description'])
