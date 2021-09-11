import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT


class Connection:
    def __init__(self, user, password, db_name='postgres'):
        """
        PostgreSQL constructor

        - *user*: PostgreSQL user name
        - *password*: User's password
        - *db_name*: Database name to connect, default is 'postgres'

        """
        self._user = user
        self._password = password
        self._db_name = db_name
        self.connect()

    def connect(self):
        """
        Connect to PostgreSQL database

        """
        self._conn = psycopg2.connect(user=self._user, password=self._password, dbname=self._db_name)
        self._conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self._cursor = self._conn.cursor()
