# main
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template , request
# from database import app, Books, db
from models import app , Books, db

app = Flask(__name__)

@app.route("/")
def main ():
    return render_template("index.html")

@app.route("/books/add",  methods = ['GET', 'POST']) 
def add_book():
    if request.method == 'POST':
        book = Books(
            title = request.form['title'],
            author = request.form['author'],
            isbn = request.form['isbn'],
            # year  = request.form['year']
            Picture = request.form['Picture']
        )
        db.session.add(book)
        db.session.commit()
        
    return render_template("addBooks.html")

@app.route("/books/delete")
def delete_books():
    return "ini page delete books, silahkan pilih buku yang ingin di hapus"

@app.route("/books/update")
def update_books():
    return 'hapus buku berdasarkan id'

@app.route("/books/lastRead")
def last_reading_books():
    return "kamu terakhir baca buku"

@app.route("/books/showBooks")
def show_all_books():
    return "lihat semua buku yang ada dalam list"


if __name__ == '__main__':
    app.run(debug=True)