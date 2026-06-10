import mysql.connector

def get_koneksi():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="uas_perpustakaan_db"
    )

def tambah_buku():
    db = get_koneksi()
    cursor = db.cursor()
    judul = input("Judul Buku: ")
    pengarang = input("Pengarang: ")
    penerbit = input("Penerbit: ")
    stok = int(input("Jumlah Stok: "))
    
    sql = "INSERT INTO buku (judul, pengarang, penerbit, stok) VALUES (%s, %s, %s, %s)"
    cursor.execute(sql, (judul, pengarang, penerbit, stok))
    db.commit()
    db.close()
    print("-> Data buku berhasil ditambahkan!")

def lihat_buku():
    db = get_koneksi()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM buku")
    print("\n[ID]   | [Judul Buku]                   | [Stok]")
    print("-" * 50)
    for row in cursor.fetchall():
        print(f"{row[0]:<6} | {row[1]:<30} | {row[4]}")
    db.close()

def ubah_buku():
    db = get_koneksi()
    cursor = db.cursor()
    id_buku = input("Masukkan ID Buku yang akan diubah: ")
    judul_baru = input("Judul Baru: ")
    stok_baru = input("Stok Baru: ")
    
    sql = "UPDATE buku SET judul = %s, stok = %s WHERE id_buku = %s"
    cursor.execute(sql, (judul_baru, stok_baru, id_buku))
    db.commit()
    db.close()
    print("-> Data buku berhasil diubah!")

def ubah_id_buku():
    db = get_koneksi()
    cursor = db.cursor()
    id_lama = input("Masukkan ID Buku yang lama: ")
    id_baru = input("Masukkan ID Buku yang baru: ")
    
    try:
        sql = "UPDATE buku SET id_buku = %s WHERE id_buku = %s"
        cursor.execute(sql, (id_baru, id_lama))
        db.commit()
        print(f"-> Sukses! ID Buku {id_lama} berhasil diganti menjadi {id_baru}.")
    except mysql.connector.Error as err:
        print(f"\n[!] Gagal mengganti ID! Error: {err}")
        print("[!] Tips: Pastikan ID baru belum dipakai oleh buku lain atau hapus dulu relasi transaksinya.")
    finally:
        db.close()

def hapus_buku():
    db = get_koneksi()
    cursor = db.cursor()
    id_buku = input("Masukkan ID Buku yang dihapus: ")
    
    sql = "DELETE FROM buku WHERE id_buku = %s"
    cursor.execute(sql, (id_buku,))
    db.commit()
    db.close()
    print("-> Data buku berhasil dihapus!")

while True:
    print("\n--- KELOLA DATA KATALOG BUKU ---")
    print("1. Tambah | 2. Lihat | 3. Ubah | 4. Hapus | 5. ubah ID | 6. Keluar")
    pilih = input("Pilih menu: ")
    if pilih == '1': tambah_buku()
    elif pilih == '2': lihat_buku()
    elif pilih == '3': ubah_buku()
    elif pilih == '4': hapus_buku()
    elif pilih == '5': ubah_id_buku()
    elif pilih == '6': break