# main.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Books

app = Flask(__name__)

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    


# Mengikat objek db ke aplikasi Flask
db.init_app(app)

# Membuat semua tabel database
with app.app_context():
    db.create_all()

# --- Rute Aplikasi ---

@app.route("/")
def main (): 
    # ambil database selruh buku
    all_books = Books.query.all()
    return render_template("index.html", books=all_books)

@app.route("/books/add",  methods = ['GET', 'POST']) 
def add_book():
    if request.method == 'POST':
    # Mengambil data dari form HTML
        new_book = Books(
            title = request.form['title'],
            author = request.form['author'],
            isbn = request.form['isbn'],
            # year  = request.form['year']
            cover_image = request.form.get('cover_image')
        )
        # Menambahkan dan menyimpan buku ke database
        db.session.add(new_book)
        db.session.commit()
        # Mengarahkan kembali ke halaman utama
        return redirect(url_for('main'))
    
    # Jika method adalah GET, tampilkan halaman form    
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