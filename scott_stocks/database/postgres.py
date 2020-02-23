import psycopg2

def connect(username, password, host, port, database):
    try:
        connection = psycopg2.connect(user = username,
                                      password = password,
                                      host = host,
                                      port = port,
                                      database = database)
        connection.autocommit = True
        return connection
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL", error)
    return None

def close_connection(connection, cursor = None):
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
        print("PostgreSQL connection is closed")
        return True
    return False

def get_version(cursor):
    query = "SELECT version();"
    run_query(cursor, query)
    record = cursor.fetchone()
    print("You are connected to - ", record,"\n")

def create_database():
    raise NotImplementedError

def create_table():
    raise NotImplementedError

def add_column(cursor, table, column, typeName):
    query = f'ALTER TABLE {table} ADD COLUMN "{column}" {typeName};'
    return run_query(cursor, query)

def delete_column(cursor, table, column):
    query = f'ALTER TABLE {table} DROP COLUMN "{column}";'
    return run_query(cursor, query)

def insert_row_dict(cursor, table, dictionary):
    columns = '('
    values = '('
    for key, value in dictionary.items():
        columns += str(key) + ','
        values += '"' + str(value) + '",'
    columns = columns.strip(',') + ')'
    values = values.strip(',') + ')'
    query = f'INSERT INTO {table} {columns} VALUES {values};'
    success = run_query(cursor, query)
    return success

def insert_row(cursor, table, columns, values):
    query = f'INSERT INTO {table} {columns} VALUES {values};'
    success = run_query(cursor, query)
    return success

def update_row(cursor, table, searchColumn, searchValue, setColumn, setValue):
    query = f'UPDATE {table} SET {setColumn} = {setValue} WHERE {searchColumn} = {searchValue}'
    success = run_query(cursor, query)
    if success:
        print(f'Successfully updated row into table {table}')
    return success

"""
def upsert(cursor, table, columnList, valueList):
    columns = '('
    for column in columnList:
        columns += column
    query = f'INSERT INTO {table} {columns} VALUES {values} ON CONFLICT DO UPDATE SET '
    success = run_query(cursor, query)
    return success
"""

def remove_row(cursor, table, column, value):
    query = f"DELETE FROM {table} WHERE {column} = '{value}';"
    success = run_query(cursor, query)
    if success:
        print(f'Successfully removed {cursor.rowcount} row(s) from table {table}')
    
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
