# app/__init__.py

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import pymysql

# Initialize db and migrate
db = SQLAlchemy()
migrate = Migrate()

# Install PyMySQL to avoid the 'ModuleNotFoundError'
pymysql.install_as_MySQLdb()

def create_app():
    app = Flask(__name__)

    # Configure the database URI
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/rumputpanjangamanda'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize db and migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprint for routing
    from app.routes import bp as main_bp  # Import blueprint here
    app.register_blueprint(main_bp)

    return app
