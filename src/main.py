from flask import Flask
from db_factory import DBConnectorFactory

app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello, World!'

DB_TYPE = 'postgresql'
db_connector = DBConnectorFactory.create_connector(DB_TYPE)

if __name__ == '__main__':
  # change port to 5001
  app.run(port=5001)