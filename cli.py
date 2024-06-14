import click
from rich.console import Console
from rich.table import Table
from models import Author, Book, Publisher

console = Console()

@click.group()
def cli():
    pass

# Author commands
@click.command()
@click.argument('name')
def create_author(name):
    Author.create(name)
    console.print(f"Author [bold green]{name}[/bold green] created successfully.")

@click.command()
def list_authors():
    authors = Author.get_all()
    if authors:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", min_width=20)
        for author in authors:
            table.add_row(str(author[0]), author[1])
        console.print(table)
    else:
        console.print("No authors found.", style="bold red")

@click.command()
@click.argument('author_id', type=int)
def delete_author(author_id):
    if Author.find_by_id(author_id):
        Author.delete(author_id)
        console.print(f"Author with ID [bold red]{author_id}[/bold red] deleted successfully.")
    else:
        console.print(f"Author with ID [bold red]{author_id}[/bold red] not found.", style="bold red")

# Book commands
@click.command()
@click.argument('title')
@click.argument('author_id', type=int)
def create_book(title, author_id):
    if Author.find_by_id(author_id):
        Book.create(title, author_id)
        console.print(f"Book [bold green]{title}[/bold green] created successfully.")
    else:
        console.print(f"Author with ID [bold red]{author_id}[/bold red] not found. Cannot create book.", style="bold red")

@click.command()
def list_books():
    books = Book.get_all()
    if books:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Title", min_width=20)
        table.add_column("Author ID", min_width=10)
        for book in books:
            table.add_row(str(book[0]), book[1], str(book[2]))
        console.print(table)
    else:
        console.print("No books found.", style="bold red")

@click.command()
@click.argument('book_id', type=int)
def delete_book(book_id):
    if Book.find_by_id(book_id):
        Book.delete(book_id)
        console.print(f"Book with ID [bold red]{book_id}[/bold red] deleted successfully.")
    else:
        console.print(f"Book with ID [bold red]{book_id}[/bold red] not found.", style="bold red")

# Publisher commands
@click.command()
@click.argument('name')
def create_publisher(name):
    Publisher.create(name)
    console.print(f"Publisher [bold green]{name}[/bold green] created successfully.")

@click.command()
def list_publishers():
    publishers = Publisher.get_all()
    if publishers:
        table = Table(show_header=True, header_style="bold magenta")
        table.add_column("ID", style="dim", width=6)
        table.add_column("Name", min_width=20)
        for publisher in publishers:
            table.add_row(str(publisher[0]), publisher[1])
        console.print(table)
    else:
        console.print("No publishers found.", style="bold red")

@click.command()
@click.argument('publisher_id', type=int)
def delete_publisher(publisher_id):
    if Publisher.find_by_id(publisher_id):
        Publisher.delete(publisher_id)
        console.print(f"Publisher with ID [bold red]{publisher_id}[/bold red] deleted successfully.")
    else:
        console.print(f"Publisher with ID [bold red]{publisher_id}[/bold red] not found.", style="bold red")

# Add commands to CLI
cli.add_command(create_author)
cli.add_command(list_authors)
cli.add_command(delete_author)
cli.add_command(create_book)
cli.add_command(list_books)
cli.add_command(delete_book)
cli.add_command(create_publisher)
cli.add_command(list_publishers)
cli.add_command(delete_publisher)

if __name__ == '__main__':
    cli()
