// script.js

// Di sini Anda bisa menambahkan fungsionalitas JavaScript interaktif.
// Contoh:
// - Menampilkan modal atau form untuk menambah/mengedit buku.
// - Menangani klik pada tombol "Edit" dan "Hapus".
// - Memperbarui konten halaman secara dinamis.

// Contoh sederhana untuk menampilkan pesan saat tombol "Tambah Buku" diklik
document.addEventListener('DOMContentLoaded', () => {
    const tambahBukuBtn = document.querySelector('header .btn');

    tambahBukuBtn.addEventListener('click', () => {
        alert('Fitur "Tambah Buku" akan ditambahkan di sini!');
    });
});
