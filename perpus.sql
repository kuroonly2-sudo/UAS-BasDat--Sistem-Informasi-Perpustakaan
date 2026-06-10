-- 1. Perintah INSERT (Menambahkan Data Peminjaman Baru)
INSERT INTO detail_peminjaman (id_peminjaman, id_buku, status) 
VALUES (1, 12, 'Dipinjam');

-- 2. Perintah UPDATE (Mengubah Status Buku karena Telah Dikembalikan)
UPDATE detail_peminjaman 
SET status = 'Dikembalikan' 
WHERE id_peminjaman = 1 AND id_buku = 12;

-- 3. Perintah DELETE (Menghapus Rekam Data Sirkulasi)
DELETE FROM detail_peminjaman 
WHERE id_peminjaman = 1 AND id_buku = 12;
