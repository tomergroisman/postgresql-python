from typing import List
from postgresql_python.connection import Connection
from postgresql_python.types import Column, ForignKey, Instance


class Table(Connection):
    """
    PostgreSQL table class

    """

    def create_table(
        self,
        table_name: str,
        columns: List[Column],
        primary_keys: List[str] = None,
        forign_keys: List[ForignKey] = None
    ):
        """
        Create a new table in the database

        - *table_name*: The new table name
        - *columns*: A list of column dictionaties
        - *primary_keys?*: A list of primary keys
        - *forign_keys?*: A list of forgin keys dictionaties

        """
        str_columns = None
        for column in columns:
            name = column.get('name')
            data_type = column.get('data_type')
            length = f'({column.get("length")})' if column.get('length') else ''
            constrains = f'{" ".join(column.get("constrains"))}' if column.get('constrains') else None
            parsed_column = filter(None, [name, data_type + length if data_type else None, constrains])
            str_column = " ".join(parsed_column)
            try:
                str_columns.append(str_column)
            except AttributeError:
                str_columns = [str_column]
        str_columns = ', \n'.join(str_columns) if str_columns else None
        str_primary_keys = f'PRIMARY KEY ({", ".join(primary_keys)})' if primary_keys else None
        str_forign_keys = '\n'.join(
            [
                (
                    f'FOREIGN KEY {forign_key.get("name")} '
                    f'REFERENCES {forign_key.get("reference")} ({forign_key.get("name")})'
                )
                for forign_key in forign_keys
            ]) if forign_keys else None

        query_body = filter(None, [str_columns, str_primary_keys, str_forign_keys])
        query_body_str = "\n".join(query_body)

        create_db_query = (
            f'CREATE TABLE {table_name} ('
            f'{query_body_str}'
            f')'
        )
        self._cursor.execute(create_db_query)

    def drop_table(self, table_name: str):
        """
        Drop a table from the database

        - *table_name*: The table name to drop

        """
        drop_table_query = f'DROP TABLE {table_name}'
        self._cursor.execute(drop_table_query)

    def insert(self, table_name: str, instance: Instance):
        """
        Insert an instance to table

        - *table_name*: The table name to insert
        - *instance*: An instance dictionary

        """
        columns = instance.get('columns')
        str_columns = f'({", ".join(columns)})' if columns else ''
        values = instance.get('values')
        if values is None:
            raise AttributeError('No values were passed')
        str_values = f'({", ".join([wrap_string_with_quotes(value) for value in values])})'

        query_body_str = f'{str_columns} VALUES {str_values}'

        insert_instance_query = (
            f'INSERT INTO {table_name}'
            f'{query_body_str}'
        )
        self._cursor.execute(insert_instance_query)

    def get(
        self,
        table_name: str,
        columns: str = '*',
        filter: str = '1=1',
        order: str = '1',
        limit: str = 'ALL',
        offset: str = 0,
    ):
        """
        Get instances from the table

        - *table_name*: The table name to get from
        - *columns (optional)*: The columns to filter, default is all columns
        - *filter (optional)*: A SQL query filter
        - *order (optional)*: Order instances command
        - *limit (optional)*: Limitation number of result
        - *offset (optional)*: Offset from the first instance

        """
        get_query = f'SELECT {columns} FROM {table_name} WHERE {filter} ORDER BY {order} LIMIT {limit} OFFSET {offset}'
        self._cursor.execute(get_query)
        results = self._cursor.fetchall()
        return results


def wrap_string_with_quotes(str: str):
    return f"'{str}'"
