from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os

app = Flask(__name__)

# Use an absolute path for the SQLite database file
db_path = os.path.join(os.path.dirname(__file__), 'event_management.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path

db = SQLAlchemy(app)
migrate = Migrate(app, db)
