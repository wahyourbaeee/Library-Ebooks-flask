from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy()


class Books(db.Model):
    id = db.column(db.integer, primary_key = True)
    title = db.column(db.string(150), nullable = False)
    author = db.column(db.string(100))
    isbn = db.column(db.string(200))
    year = db.column(db.integer)
    Picture = db.column(db.string)
    
    def to_dict(self):
        return{
            "id" : self.id,
            "title" : self.title,
            "author" : self.author,
            "isbn" : self.isbn,
            "picture" : self.Picture
            # "year" : self.year
        }


with app.app_context():
    db.create_all()

# db = SQLAlchemy(model_class=Base)