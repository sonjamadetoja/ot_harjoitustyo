import os
import sqlite3

dirname = os.path.dirname(__file__)

connection = sqlite3.connect(os.path.join(dirname, '..', 'data', "database.sqlite"))
connection.row_factory = sqlite3.Row

def get_database_connection():
    return connection

def get_database_connection_test():
    connection_test = sqlite3.connect(os.path.join(dirname, '..', 'data', "database_test.sqlite"))
    connection_test.row_factory = sqlite3.Row
    return connection_test