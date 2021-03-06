import datetime
import psycopg2
import psycopg2.extras


def connect(username, password, host, port, database=None):
    try:
        connection = psycopg2.connect(user=username,
                                      password=password,
                                      host=host,
                                      port=port,
                                      database=database)
        connection.autocommit = True
        return connection
    except (Exception, psycopg2.Error) as error:
        print('Error while connecting to Postgres SQL:', error)
    return None


def cursor(username, password, host, port, database=None):
    connection = connect(username, password, host, port, database)
    dict_cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)
    return dict_cursor


def close_connection(connection, cursor=None):
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
        print("PostgreSQL connection is closed")
        return True
    return False


def get_version(cursor):
    query = 'SELECT version();'
    run_query(cursor, query)
    record = cursor.fetchone()
    print('You are connected to - ', record, '\n')
    return record


def database_exists(cursor, database_name):
    query = f"SELECT datname FROM pg_catalog.pg_database WHERE datname = '{database_name}';"
    run_query(cursor, query)
    return bool(cursor.rowcount)


def create_database(cursor, name):
    query = f'CREATE DATABASE {name}'
    result = run_query(cursor, query)
    if result:
        print(f'Created database: {name}')
    else:
        print(f'Failed to create database {name}')
    return result


def delete_database(cursor, name):
    query = f'DROP DATABASE IF EXISTS {name}'
    run_query(cursor, query)
    print(f'Deleted database: {name}')


def table_exists(cursor, table_name):
    query = f"SELECT to_regclass('{table_name}');"
    run_query(cursor, query)
    result = cursor.fetchone()[0]
    return result == table_name and result is not None


def create_table(cursor, table_name, columns=None):
    query = f'CREATE TABLE {table_name} ('
    if columns is not None:
        for column_name, column_type in columns.items():
            query += f'{column_name} {column_type},'
        query = query.strip(',')
    query += ');'
    return run_query(cursor, query)


def delete_table(cursor, table_name):
    query = f'DROP TABLE IF EXISTS {table_name}'
    return run_query(cursor, query)


def add_column(cursor, table, column_name, column_type='varchar'):
    query = f'ALTER TABLE {table} ADD COLUMN "{column_name}" {column_type};'
    return run_query(cursor, query)


def delete_column(cursor, table, column):
    query = f'ALTER TABLE {table} DROP COLUMN "{column}";'
    return run_query(cursor, query)


def insert_row(cursor, table, columns, values):
    query = f'INSERT INTO {table} {columns} VALUES {values};'
    return run_query(cursor, query)


def insert_row_as_dict(cursor, table, dictionary):
    columns = '('
    values = '('
    for key, value in dictionary.items():
        columns += str(key) + ','
        value = _escape_apostrophes(value)
        values += "'" + str(value) + "',"
    columns = columns.strip(',') + ')'
    values = values.strip(',') + ')'
    query = f'INSERT INTO {table} {columns} VALUES {values};'
    return run_query(cursor, query)


def update_value(cursor, table, search_column, search_value, set_column, set_value):
    if isinstance(search_value, str) or isinstance(search_value, datetime.date):
        search_value = f"('{search_value}')"
    if isinstance(set_value, str) or isinstance(set_value, datetime.date):
        set_value = f"('{set_value}')"
    query = f'UPDATE {table} SET {set_column} = {set_value} WHERE {search_column} = {search_value}'
    success = run_query(cursor, query)
    if success:
        print(f'Successfully updated row into table {table}')
    return success


def remove_row(cursor, table, column, value):
    value = _escape_apostrophes(value)
    query = f"DELETE FROM {table} WHERE {column} = '{value}';"
    success = run_query(cursor, query)
    if success:
        print(f'Successfully removed {cursor.rowcount} row(s) from table {table}')
    return success


def run_query(cursor, query):
    print(query)
    try:
        cursor.execute(query)
        return True
    except Exception as error:
        print(f'Postgres error: {error}')
        return False


def get_list_results(cursor):
    rows = cursor.fetchall()
    items = []
    for row in rows:
        items.append(row[0])
    return items


def _escape_apostrophes(text):
    if text is not None and isinstance(text, str):
        text = text.replace("'", "''")
    return text
