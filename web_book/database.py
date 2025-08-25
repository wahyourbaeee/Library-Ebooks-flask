from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

app =Flask(__name__)




app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']

db = SQLAlchemy(app)

class Books(db.model):
    id = db.column(db.integer, primary_key = True)
    title = db.column(db.string(150), nullable = False)
    author = db.column(db.string(100))
    year = db.column(db.integer)
    
    def to_dict(self):
        return{
            "id" : self.id,
            "title" : self.title,
            "author" : self.author,
            "year" : self.year
        }

with app.app_context():
    db.create_all()

# db = SQLAlchemy(model_class=Base)