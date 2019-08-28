import click
from pprint import pprint
from getcard import first_step


@click.command()
@click.option('--count', default=3, prompt='Count of gamblers',
              help='Count of gamblers')
@click.option('--step', default=1, help='Step the game.')
def hello(count):
    """Check integer"""
    pprint(first_step(count))

if __name__ == '__main__':
    hello()
