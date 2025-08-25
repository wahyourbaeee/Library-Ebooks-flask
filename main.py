# main.py
from flask import Flask, render_template, request, redirect, url_for
from models import db, Books
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

# Konfigurasi database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///books.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False    


# Konfigurasi untuk unggah file
UPLOAD_FOLDER = 'static/ebooks'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True) # Pastikan folder sudah ada

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
        # Mengambil data dari form HTML (metadata)
        title = request.form.get('title')
        author = request.form.get('author')
        isbn = request.form.get('isbn')
        cover_image = request.form.get('cover_image')
        
        # Menangani unggahan file ebook
        ebook_file = request.files.get('ebook_file')
        file_path = None
        if ebook_file and ebook_file.filename:
            # Gunakan secure_filename untuk keamanan
            filename = secure_filename(ebook_file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            ebook_file.save(file_path)
            # Simpan path relatif untuk database
            file_path = f"/{UPLOAD_FOLDER}/{filename}"
            
        # Membuat objek buku baru dengan semua data
        new_book = Books(
            title=title,
            author=author,
            isbn=isbn,
            cover_image=cover_image,
            ebook_file=file_path
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

@app.route("/<id>", methods = ['GET'])
def read_book():
    return 'hallo'

@app.route("/books/lastRead")
def last_reading_books():
    return "kamu terakhir baca buku"

@app.route("/books/showBooks")
def show_all_books():
    return "lihat semua buku yang ada dalam list"


if __name__ == '__main__':
    app.run(debug=True)