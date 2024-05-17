# Description: This file contains the PostgresConnection class 
# which is a singleton class that creates a connection to the Postgres database.
# import psycopg2

# class PostgresConnection:
#   _instance = None

#   def __new__(cls):
#     if cls._instance is None:
#       cls._instance = super().__new__(cls)
#       cls._instance.connection = psycopg2.connect(
#         host='localhost',
#         port=5432,
#         user='your_username',
#         password='your_password',
#         database='your_database'
#       )
#     return cls._instance

#   def get_connection(self):
#     return self.connection
  
# Postgress connection class with a pool of connections
class PostgresConnection:
  _instance = None
  _pool = None
  
  def __new__(cls):
    if cls._instance is None:
      cls._instance = super().__new__(cls)
      cls._pool = psycopg2.pool.SimpleConnectionPool(
        minconn=1,
        maxconn=10,
        host='localhost',
        port=5432,
        user='your_username',
        password='your_password',
        database='your_database'
      )
    return cls._instance
  
  def get_connection(self):
    return self._pool.getconn()
  
  def release_connection(self, connection):
    self._pool.putconn(connection)



  
