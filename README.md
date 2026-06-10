# UAS-BasDat--Sistem-Informasi-Perpustakaan

A. Pemilihan Topik
Topik yang dipilih untuk pengerjaan tugas UAS Basis Data ini adalah A. Sistem Informasi Perpustakaan.
Sistem ini dirancang untuk menangani kebutuhan operasional perpustakaan secara digital, mulai dari pengelolaan registrasi anggota baru, inventarisasi koleksi buku (katalog), manajemen transaksi sirkulasi peminjaman, hingga pencatatan pengembalian buku beserta rekapitulasi status sirkulasinya secara real-time.

B. Proses Bisnis dan Penentuan Modul Sistem
Alur operasional pada sistem ini didefinisikan ke dalam tiga modul utama berikut:
1.	Modul Anggota (Keanggotaan): Calon peminjam didaftarkan ke dalam sistem dengan mencantumkan data pribadi (Nama, Alamat, dan Nomor Telepon). Data ini disimpan ke dalam database untuk keperluan pelacakan riwayat aktivitas sirkulasi buku.
2.	Modul Buku (Katalog Koleksi): Menginventarisasi data seluruh buku yang tersedia di perpustakaan (Judul, Pengarang, Penerbit, dan Jumlah Stok) untuk memastikan ketersediaan fisik buku saat akan dipinjam.
3.	Modul Transaksi (Sirkulasi): Memproses pencatatan peminjaman buku oleh anggota. Sistem secara dinamis mencatat tanggal pinjam, batas tanggal kembali, status buku, serta otomatis memperbarui jumlah stok buku yang tersedia di rak.

C. Aktor yang Terlibat dalam Tiap Modul
Pengguna sistem terbagi menjadi dua aktor utama:
1.	Anggota Perpustakaan: Aktor eksternal yang memberikan data pribadi untuk didaftarkan, melakukan pencarian katalog, melakukan peminjaman buku, serta menerima informasi batas waktu pengembalian.
2.	Admin / Pustakawan: Aktor internal yang memiliki hak akses penuh untuk mengelola data master keanggotaan, memperbarui katalog buku, memproses transaksi peminjaman, serta mengubah status sirkulasi saat buku dikembalikan.

D. Desain Entity Relationship Diagram (ERD)
Berikut adalah representasi struktur tabel fisik pada Sistem Informasi Perpustakaan yang memenuhi standar relasional:
Deskripsi Entitas dan Atribut:
•	Anggota (Master): Menyimpan data identitas peminjam. PK: id_anggota. Atribut: nama, alamat, dan no_telp.
•	Buku (Master): Menyimpan daftar koleksi pustaka. PK: id_buku. Atribut: judul, pengarang, penerbit, dan stok.
•	Peminjaman (Transaksi Utama): Mencatat header transaksi sirkulasi. PK: id_peminjaman. FK: id_anggota. Atribut: tanggal_pinjam dan tanggal_kembali.
•	Detail Peminjaman (Detail Transaksi): Menangani relasi many-to-many antara buku dan peminjaman (satu transaksi bisa memuat banyak buku). PK: id_detail. FK: id_peminjaman dan id_buku. Atribut: status.

E. Penentuan Kardinalitas Relasi
•	Relasi Anggota ke Peminjaman (1:M): Satu orang anggota yang sama dapat melakukan transaksi peminjaman berkali-kali di waktu yang berbeda. Namun, satu ID transaksi peminjaman hanya boleh terikat pada satu anggota yang sah.
•	Relasi Peminjaman ke Detail Peminjaman (1:M): Satu transaksi peminjaman dapat memuat beberapa judul buku sekaligus di dalam lembar detailnya.
•	Relasi Buku ke Detail Peminjaman (1:M): Satu judul buku yang sama dapat dipinjam berulang kali dalam berbagai ID transaksi detail yang berbeda oleh banyak anggota.

F. Proses Normalisasi Database
Proses normalisasi dilakukan secara bertahap untuk menghilangkan redundansi data serta mencegah terjadinya anomali data (insert, update, delete anomaly).
•	Bentuk Tidak Ternormalisasi (UNF) & 1NF: Seluruh data peminjam, data buku, dan tanggal transaksi digabungkan dalam satu tabel raksasa. Atribut bernilai atomik namun memicu pengulangan data nama anggota dan judul buku yang sangat parah di setiap baris transaksi.
•	Bentuk Normal Kedua (2NF): Memecah tabel induk agar seluruh atribut non-key bergantung penuh secara fungsional (fully functionally dependent) pada Primary Key masing-masing. Terbentuklah tabel terpisah: anggota, buku, dan peminjaman.
•	Bentuk Normal Ketiga (3NF): Menghilangkan ketergantungan transitif (transitive dependency) di mana atribut non-key bergantung pada atribut non-key lainnya. Hubungan many-to-many antara peminjaman dan buku diselesaikan dengan membuat jembatan tabel detail_peminjaman.

G. Implementasi Desain ke DBMS MySQL/MariaDB
Berikut adalah skrip DDL (Data Definition Language) SQL untuk menyusun struktur database perpustakaan secara aman: 

H. Manipulasi Data Menggunakan SQL
Berikut adalah perintah DML (Data Manipulation Language) SQL untuk menguji fungsionalitas manipulasi data pada tabel transaksi/master: 

I. Kode Program Python (CRUD Tabel Master Buku)
Skrip backend Python menggunakan pustaka mysql-connector-python untuk mengelola data master buku:

J. Kode Program PHP (CRUD Antarmuka Web Transaksi Detail)
Berikut skrip aplikasi web PHP native (tanpa menggunakan komponen tabel HTML yang rumit agar mudah dibaca dan dimodifikasi) untuk pemrosesan sirkulasi: 
