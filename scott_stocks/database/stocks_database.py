import sys
sys.path.append('E:/Google Drive/Computers/Dev/Stocks/scott_stocks')

import psycopg2.extras
from database import postgres

username = 'postgres'
password = ''
host = 'localhost'
port = '5432'
database = 'stocks'

connection = postgres.connect(username, password, host, port, database)
cursor = connection.cursor(cursor_factory = psycopg2.extras.DictCursor)

if __name__ == "__main__":
    pass
