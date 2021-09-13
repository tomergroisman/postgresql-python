from postgresql_python.connection import Connection


class Database(Connection):
    """
    PostgreSQL database class

    """

    def create_database(self, db_name: str):
        """
        Create a new database

        - *db_name*: The new database name

        Throws psycopg2.errors.DuplicateDatabase error if database is already exists
        Throws except psycopg2.errors.SyntaxError error on wrong query

        """
        create_db_query = f'CREATE DATABASE {db_name}'
        self._cursor.execute(create_db_query)

    def drop_database(self, db_name: str):
        """
        Drop a database

        - *db_name*: The database name to drop

        Throws psycopg2.errors.InvalidCatalogName error if database does not exists
        Throws except psycopg2.errors.SyntaxError error on wrong query

        """
        drop_db_query = f'DROP DATABASE {db_name}'
        self._cursor.execute(drop_db_query)
