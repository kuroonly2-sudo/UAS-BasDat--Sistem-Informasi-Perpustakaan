<?php
$conn = new mysqli("localhost", "root", "", "uas_perpustakaan_db");
if ($conn->connect_error) { die("Koneksi gagal: " . $conn->connect_error); }

// Proses Insert Data
if (isset($_POST['tambah'])) {
    $id_peminjaman = $_POST['id_peminjaman'];
    $id_buku = $_POST['id_buku'];
    $status = $_POST['status'];
    $conn->query("INSERT INTO detail_peminjaman (id_peminjaman, id_buku, status) VALUES ('$id_peminjaman', '$id_buku', '$status')");
    header("Location: sisforpus.php");
}

// Proses Delete Data
if (isset($_GET['hapus'])) {
    $id = $_GET['hapus'];
    $conn->query("DELETE FROM detail_peminjaman WHERE id_detail = $id");
    header("Location: sisforpus.php");
}
?>

<!DOCTYPE html>
<html lang="id">
<head>
    <title>Sirkulasi Perpustakaan</title>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; background: #f4f4f4; }
        .container { max-width: 800px; margin: 0 auto; background: white; padding: 20px; border-radius: 5px; }
        .form-group { margin-bottom: 10px; }
        input, select, button { padding: 8px; width: 100%; margin-bottom: 10px; border-radius: 4px; border: 1px solid #ccc; }
        button { background: #2b6cb0; color: white; cursor: pointer; font-weight: bold; border: none; }
        .list-item { background: #f9f9f9; padding: 10px; margin-bottom: 5px; border-left: 4px solid #2b6cb0; list-style: none; }
        .btn-hapus { color: red; float: right; text-decoration: none; }
    </style>
</head>
<body>
<div class="container">
    <h2>Data Penilaian Sirkulasi Buku</h2>
    <form method="POST" action="">
        <div class="form-group">
            <input type="number" name="id_peminjaman" placeholder="ID Peminjaman" required>
            <input type="number" name="id_buku" placeholder="ID Buku" required>
            <select name="status" required>
                <option value="Dipinjam">Dipinjam</option>
                <option value="Dikembalikan">Dikembalikan</option>
            </select>
        </div>
        <button type="submit" name="tambah">Simpan Data Transaksi</button>
    </form>

    <h3>Daftar Log Sirkulasi Buku Aktif:</h3>
    <ul>
    <?php
    $res = $conn->query("SELECT * FROM detail_peminjaman ORDER BY id_detail DESC");
    while ($row = $res->fetch_assoc()) {
    ?>
        <li class="list-item">
            ID Log: <?= $row['id_detail'] ?> | No Nota Pinjam: <?= $row['id_peminjaman'] ?> | Kode Buku: <?= $row['id_buku'] ?> | Status: <strong><?= $row['status'] ?></strong>
            <a href="?hapus=<?= $row['id_detail'] ?>" class="btn-hapus" onclick="return confirm('Hapus rekam log ini?')">Hapus Log</a>
        </li>
    <?php } ?>
    </ul>
</div>
</body>
</html>