import click
from rich.console import Console
from rich.table import Table
from models import Author, Book, Publisher

console = Console()

@click.group()
def cli():
    pass

@cli.command()
@click.argument('name')
def create_author(name):
    author_id = Author.create(name)
    if author_id:
        console.print(f'[bold green]Author "{name}" created successfully with id {author_id}.[/bold green]')
    else:
        console.print(f'[bold red]Author "{name}" already exists.[/bold red]')

@cli.command()
def list_authors():
    authors = Author.get_all()
    table = Table(title="Authors")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")

    for author in authors:
        table.add_row(str(author["id"]), author["name"])

    console.print(table)

@cli.command()
@click.argument('author_id', type=int)
def delete_author(author_id):
    rows_deleted = Author.delete(author_id)
    if rows_deleted:
        console.print(f'[bold green]Author with id "{author_id}" deleted successfully.[/bold green]')
    else:
        console.print(f'[bold red]Author with id "{author_id}" not found.[/bold red]')

@cli.command()
@click.argument('title')
@click.argument('author_id', type=int)
def create_book(title, author_id):
    book_id = Book.create(title, author_id)
    if book_id:
        console.print(f'[bold green]Book "{title}" created successfully with id {book_id}.[/bold green]')
    else:
        console.print(f'[bold red]Error creating book "{title}". Check if the author ID {author_id} exists.[/bold red]')

@cli.command()
def list_books():
    books = Book.get_all()
    table = Table(title="Books")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Title", style="magenta")
    table.add_column("Author", style="green")

    for book in books:
        table.add_row(str(book["id"]), book["title"], book["author_name"])

    console.print(table)

@cli.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    rows_deleted = Book.delete(book_id)
    if rows_deleted:
        console.print(f'[bold green]Book with id "{book_id}" deleted successfully.[/bold green]')
    else:
        console.print(f'[bold red]Book with id "{book_id}" not found.[/bold red]')

@cli.command()
@click.argument('name')
def create_publisher(name):
    publisher_id = Publisher.create(name)
    if publisher_id:
        console.print(f'[bold green]Publisher "{name}" created successfully with id {publisher_id}.[/bold green]')
    else:
        console.print(f'[bold red]Publisher "{name}" already exists.[/bold red]')

@cli.command()
def list_publishers():
    publishers = Publisher.get_all()
    table = Table(title="Publishers")
    table.add_column("ID", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name", style="magenta")

    for publisher in publishers:
        table.add_row(str(publisher["id"]), publisher["name"])

    console.print(table)

@cli.command()
@click.argument('publisher_id', type=int)
def delete_publisher(publisher_id):
    rows_deleted = Publisher.delete(publisher_id)
    if rows_deleted:
        console.print(f'[bold green]Publisher with id "{publisher_id}" deleted successfully.[/bold green]')
    else:
        console.print(f'[bold red]Publisher with id "{publisher_id}" not found.[/bold red]')

if __name__ == "__main__":
    cli()
