# models.py
from flask_sqlalchemy import SQLAlchemy

# Inisialisasi objek SQLAlchemy, tanpa terikat dengan aplikasi
db = SQLAlchemy()

class Books(db.Model):
    __tablename__ = 'books' # Nama tabel di database
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    author = db.Column(db.String(100))
    isbn = db.Column(db.String(200))
    year = db.Column(db.Integer)
    cover_image = db.Column(db.String)
    ebook_file = db.Column(db.String)
    
    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "isbn": self.isbn,
            "cover_image": self.cover_image,
            "ebook_file": self.ebook_file,
            "year": self.year
        }
