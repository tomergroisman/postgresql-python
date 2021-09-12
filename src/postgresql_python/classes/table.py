from postgresql_python.connection import Connection


class Table(Connection):
    """
    PostgreSQL table class

    """

    def create_table(self, table_name, columns, primary_keys=None, forign_keys=None):
        """
        Create a new table in the database

        - *table_name*: The new table name
        - *columns*: A list of column dictionaties: {
            name (string),
            data_type (string),
            length (number),
            constrains (list)
        }
        - *primary_keys*: A list of primary keys (string)
        - *forign_keys*: A list of forgin keys dictionaties: {name (string), reference (string)}

        """
        str_columns = None
        for column in columns:
            name = column.get('name', None)
            data_type = column.get('data_type', None)
            length = f'({column.get("length")})' if column.get('length', None) else ''
            constrains = f'{" ".join(column.get("constrains"))}' if column.get('constrains', None) else None
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

    def drop_table(self, table_name):
        """
        Drop a table from the database

        - *table_name*: The table name to drop

        """
        drop_table_query = f'DROP TABLE {table_name}'
        self._cursor.execute(drop_table_query)

    def insert(self, table_name, instance):
        """
        Insert an instance to table

        - *table_name*: The table name to insert
        - *instance*: An instance dictionary: {columns (list<string>), values(list<string>)}

        """
        columns = instance.get('columns', None)
        str_columns = f'({", ".join(columns)})' if columns else ''
        values = instance.get('values', None)
        if values is None:
            raise AttributeError('No values were passed')
        str_values = f'({", ".join([wrap_string_with_quotes(value) for value in values])})'

        query_body_str = f'{str_columns} VALUES {str_values}'

        insert_instance_query = (
            f'INSERT INTO {table_name}'
            f'{query_body_str}'
        )
        self._cursor.execute(insert_instance_query)

    def get(self, table_name, filter='*'):
        """
        Get instances from the table

        - *table_name*: The table name to get from
        - *filter (optional)*: A SQL query filter

        """
        get_query = f'SELECT {filter} FROM {table_name}'
        self._cursor.execute(get_query)
        results = self._cursor.fetchall()
        return results


def wrap_string_with_quotes(str):
    return f"'{str}'"
