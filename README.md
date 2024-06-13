# My CLI App

My CLI App is a command-line interface application for managing a library system. It allows users to create, list, and delete authors and books. The application uses a SQLite database for storing data and is built with Python using the `click` library for the CLI interface.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Commands](#commands)
- [Project Structure](#project-structure)
- [Dependencies](#dependencies)

## Installation

### Prerequisites

- Python 3.8 or higher
- Pipenv for managing virtual environments

### Steps

1. Navigate to your project directory:
    ```bash
    cd path/to/your/my_cli_app
    ```

2. Create a virtual environment and install dependencies:
    ```bash
    pipenv install
    ```

3. Activate the virtual environment:
    ```bash
    pipenv shell
    ```

4. Initialize the database:
    ```bash
    python -c "from database import init_db; init_db()"
    ```

## Usage

Once the setup is complete, you can start using the CLI application to manage authors and books.

### Example Commands

- Create an author:
    ```bash
    python cli.py create-author "John Doe"
    ```

- List all authors:
    ```bash
    python cli.py list-authors
    ```

- Delete an author:
    ```bash
    python cli.py delete-author <author_id>
    ```

- Create a book:
    ```bash
    python cli.py create-book "The Great Adventure" <author_id>
    ```

- List all books:
    ```bash
    python cli.py list-books
    ```

- Delete a book:
    ```bash
    python cli.py delete-book <book_id>
    ```

Replace `<author_id>` and `<book_id>` with the actual IDs of the author or book.

## Commands

### Author Commands

- `create-author <name>`: Creates a new author with the given name.
- `list-authors`: Lists all authors in the database.
- `delete-author <author_id>`: Deletes the author with the specified ID.

### Book Commands

- `create-book <title> <author_id>`: Creates a new book with the given title and author ID.
- `list-books`: Lists all books in the database.
- `delete-book <book_id>`: Deletes the book with the specified ID.


## Dependencies

- [click](https://pypi.org/project/click/): A package for creating command-line interfaces.
- [sqlite3](https://docs.python.org/3/library/sqlite3.html): A package for interacting with SQLite databases (built into Python).

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
