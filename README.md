# Library Management CLI Application

This is a Python CLI application for managing a library. It allows users to manage authors, books, and publishers. The application uses SQLite for data storage and the Click library for the command-line interface.

## Features

- Manage authors: create, list, delete.
- Manage books: create, list, delete.
- Manage publishers: create, list, delete.

## Requirements

- Python 3.9 or higher
- pipenv

## Installation

1. **Clone the repository** (if you haven't already):

    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    cd yourrepository
    ```

2. **Install dependencies**:

    ```bash
    pipenv install
    ```

3. **Initialize the database**:

    ```bash
    pipenv run python init_db.py
    ```

## Usage

### Author Commands

- Create an author:

    ```bash
    pipenv run python cli.py create-author "Author Name"
    ```

- List all authors:

    ```bash
    pipenv run python cli.py list-authors
    ```

- Delete an author by ID:

    ```bash
    pipenv run python cli.py delete-author 1
    ```

### Book Commands

- Create a book (author ID is required):

    ```bash
    pipenv run python cli.py create-book "Book Title" 1
    ```

- List all books:

    ```bash
    pipenv run python cli.py list-books
    ```

- Delete a book by ID:

    ```bash
    pipenv run python cli.py delete-book 1
    ```

### Publisher Commands

- Create a publisher:

    ```bash
    pipenv run python cli.py create-publisher "Publisher Name"
    ```

- List all publishers:

    ```bash
    pipenv run python cli.py list-publishers
    ```

- Delete a publisher by ID:

    ```bash
    pipenv run python cli.py delete-publisher 1
    ```


## Dependencies

- `click` - For creating the CLI interface
- `rich` - For enhanced CLI output

## Database Schema

The database schema is defined in `schema.sql`:

```sql
-- schema.sql
DROP TABLE IF EXISTS authors;
DROP TABLE IF EXISTS books;
DROP TABLE IF EXISTS publishers;

CREATE TABLE authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author_id INTEGER,
    FOREIGN KEY (author_id) REFERENCES authors (id)
);

CREATE TABLE publishers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
);

##License

This `README.md` file provides detailed instructions for setting up and using the CLI application, including commands for managing authors, books, and publishers. It also includes a brief overview of the project structure and dependencies.


