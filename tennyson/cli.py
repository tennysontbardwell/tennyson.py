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
    for p in tennyson.password.for_display_passwords():
        print(p)
