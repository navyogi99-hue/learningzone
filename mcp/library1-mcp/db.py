import os
from mysql.connector.connection_cext import CMySQLConnection
from typing import Any
import mysql.connector
import json
from dotenv import load_dotenv
load_dotenv()

def get_connection() -> CMySQLConnection:
    """Create and return a connection to the MySQL database using environment variables."""
    return mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        user=os.getenv("MYSQL_USERNAME", "root"),
        password=os.getenv("MYSQL_PASSWORD", "rootpasword"),
        database=os.getenv("MYSQL_DATABASE", "library")
        )
def add_book(
        book_id: str,
        title: str,
        author: str,
        published_year: str,
        available_copies: int,
        total_copies: int,
        genre: str,
        available: bool,
        active: bool,
        tags: list[str],
        isbn: str
        ) -> None:
    """Add a new book to the library database."""
    query = """
    INSERT INTO books (book_id, title, author, published_year, available_copies, total_copies, genre, available, active, tags, isbn)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    execute_query(query, (book_id, title, author, published_year, available_copies, total_copies, genre, available, active, json.dumps(tags), isbn))

def execute_query(query: str, params: tuple[Any, ...] = ()) -> list[tuple[Any, ...]]:
    """
    Execute a SQL query with optional parameters.

    For SELECT queries, returns a list of result rows.
    For INSERT/UPDATE/DELETE queries, commits the transaction and returns an empty list.
    """
    with get_connection() as connection:

        with connection.cursor() as cursor:

            cursor.execute(query, params)

            if cursor.description:
                return cursor.fetchall()

            connection.commit()
            return []
def execute_transaction(
    steps: list[tuple[str, tuple[Any, ...]]],
) -> list[Any]:
    """
    Run several statements in a single transaction on one connection.

    `steps` is a list of (query, params) tuples executed in order. They share
    one connection, so a statement can reference the row just inserted by the
    previous one via MySQL's LAST_INSERT_ID(). Everything commits together; any
    error rolls the whole batch back.

    Returns one result per step: the fetched rows for a SELECT, otherwise the
    AUTO_INCREMENT id produced by that statement (cursor.lastrowid).
    """
    connection = get_connection()
    try:
        cursor = connection.cursor()  # type: MySQLCursor
        results: list[Any] = []
        for query, params in steps:
            cursor.execute(query, params or ())
            if cursor.description:
                results.append(cursor.fetchall())
            else:
                results.append(cursor.lastrowid)
        connection.commit()
        cursor.close()
        return results
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()



if __name__ == "__main__":
    result = execute_query('select * from authors')
    print(result)