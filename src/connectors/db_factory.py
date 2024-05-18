import sqlite3
import psycopg2

from src.connectors.postgres import PostgresConnection


class DBConnectorFactory:
    @staticmethod
    def create_connector(db_type):
        if not db_type:
            raise ValueError("Database type must be provided")

        if db_type == 'sqlite':
            pass
        elif db_type == 'postgresql':
            return PostgresConnection
        elif db_type == 'mysql':
            pass
        elif db_type == 'oracle':
            pass
        else:
            raise ValueError(f"Unsupported database type: {db_type}")

# class SQLiteConnector:
#   def connect(self, db_name):
#     return sqlite3.connect(db_name)

# class PostgreSQLConnector:
#   def connect(self, db_name, user, password, host, port):
#     conn_string = f"dbname='{db_name}' user='{user}' password='{password}' host='{host}' port='{port}'"
#     return psycopg2.connect(conn_string)

# class MySQLConnector:
#   def connect(self, db_name, user, password, host, port):
#     conn_string = f"dbname='{db_name}' user='{user}' password='{password}' host='{host}' port='{port}'"
#     return psycopg2.connect(conn_string)

# class OracleConnector:
#   def connect(self, db_name, user, password, host, port):
#     conn_string = f"dbname='{db_name}' user='{user}' password='{password}' host='{host}' port='{port}'"
#     return psycopg2.connect(conn_string)
