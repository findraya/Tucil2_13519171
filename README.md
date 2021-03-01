# Tugas Kecil 2 IF2211 Strategi Algoritma
Topik: Penyusunan Rencana Kuliah dengan Topological Sort (Penerapan Decrease and Conquer) <br/>
Semester II Tahun 2020/2021

## Deskripsi Singkat Algoritma Decrease and Conquer yang Diimplementasikan
Program dibuat dengan bahasa python dan melakukan topological sort dengan mengimplementasikan algoritma Decrease and Conquer.
Diawali dengan membaca input dari file dan memasukkan detail tiap matkul seperti jumlah prerequisite (preqcount) ke dalam linked list. Lalu, dilakukan loop pada linked list dan memindahkan matkul dengan preqcount = 0 ke dalam linked list baru. Setelah itu, mengurangi preqcount dari matkul lain yang memiliki prerequisite seperti yang baru dipindahkan. Proses diulangi hingga semua matkul menjadi terurut. 
Jadi, dilakukan decrease dari preqcount tiap matkul hingga menghasilkan solusi yang telah di-sort.

## Requirement Program
Hanya membutuhkan instalasi python untuk menjalankan program

## Cara Menggunakan
1. Jalankan program dengan perintah `python src/13519171.py` pada terminal. Pastikan Anda berada dalam folder `root`
2. Ketik nama file text dari folder `test` yang ingin dijalankan
3. Tunggu hingga program menampilkan hasil sorting permasalahan berdasarkan tiap semester

## Author
13519171 - Fauzan Yubairi Indrayadi <br/>
Kelas 04