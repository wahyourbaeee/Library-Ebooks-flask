from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy()


class Base(db.model):
  id = db.column(db.integer, primary_key = True)
  title = db.column(db.string(150), nullable = False)
  author = db.column(db.string(100))
  year = db.column(db.integer)

