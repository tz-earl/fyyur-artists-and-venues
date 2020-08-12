import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database

# TODO IMPLEMENT DATABASE URL

# N.B. A user password is required, otherwise, you get a runtime exception
db_url = "postgres+psycopg2://earl:passwd@localhost:5432/fyyur"
SQLALCHEMY_DATABASE_URI = db_url
SQLALCHEMY_TRACK_MODIFICATIONS = False
