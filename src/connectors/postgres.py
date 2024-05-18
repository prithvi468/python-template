# Description: This file contains the PostgresConnection class 
# which is a singleton class that creates a connection to the Postgres database.
import psycopg2
from psycopg2 import pool


class PostgresConnection:
    _instance = None
    _pool = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            try:
                cls._pool = psycopg2.pool.SimpleConnectionPool(
                    minconn=1,
                    maxconn=10,
                    host='localhost',
                    port=5432,
                    user='your_username',
                    password='your_password',
                    database='your_database'
                )
                print("Connection pool created successfully")
            except psycopg2.OperationalError as e:
                print(f"Error creating connection pool: {e}")
                cls._instance = None  # Reset instance in case of error
                raise
        return cls._instance

    def get_connection(self):
        try:
            if self._pool is None:
                raise Exception("Connection pool is not initialized")
            connection = self._pool.getconn()
            print("Connection obtained from pool")
            return connection
        except (psycopg2.OperationalError, Exception) as e:
            print(f"Error getting connection: {e}")
            raise

    def release_connection(self, connection):
        try:
            if self._pool is None:
                raise Exception("Connection pool is not initialized")
            self._pool.putconn(connection)
            print("Connection released back to pool")
        except (psycopg2.OperationalError, Exception) as e:
            print(f"Error releasing connection: {e}")
            raise
