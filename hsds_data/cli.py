import click


@click.group()
@click.version_option()
def cli():
    "Data validator and transformer for Human Services Data Standard."


@cli.command(name="command")
@click.argument(
    "example"
)
@click.option(
    "-o",
    "--option",
    help="An example option",
)
def first_command(example, option):
    "Command description goes here"
    click.echo("Here is some output")
