import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2.extras import RealDictCursor


class Connection:
    def __init__(self, user: str, password: str, db_name: str = 'postgres'):
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
        Connect to PostgreSQL server

        """
        self._conn = psycopg2.connect(
            user=self._user,
            password=self._password,
            dbname=self._db_name,
            cursor_factory=RealDictCursor
        )
        self._conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        self._cursor = self._conn.cursor()

    def disconnect(self):
        """
        Disconnect from PostgreSQL server

        """
        self._conn.close()
        self._cursor = None
