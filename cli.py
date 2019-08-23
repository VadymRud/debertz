import click


@click.command()
@click.option('--count', default=3, prompt='Count of gamblers',
              help='Count of gamblers')
# @click.option('--name', prompt='Your name', help='The person to greet.')
def hello(count):
    """Check integer"""
    

if __name__ == '__main__':
    hello()
