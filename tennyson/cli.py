import click
import tennyson.password

@click.group()
def main():
    """
    CLI tools for tennyson
    """
    pass


@main.command()
def password():
    print(tennyson.password.password())
