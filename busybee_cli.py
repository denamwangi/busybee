import click

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

@cli.command()
@click.option('--task', prompt='What did you just complete lovely?')
def add_task(task):
	'''This script logs what you accomplished today'''
	click.echo("Nice job on completing %s" % task)
	for i, grp in enumerate(GROUPS):
		click.echo("{} {}".format(i, grp))
	group = click.prompt('what group should it go under?')	
	click.echo('you picked %s' % group)


@cli.command()
def list():
	'''Shows a grouped list of what you've done'''
	for group in meh:
		click.echo(click.style(group, fg='magenta'))
		for item in meh[group]:
			click.echo('     %s' % item)
