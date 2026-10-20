# Pemrograman Modern Python - Teori & Praktikum Pertemuan ke-5

Repositori ini berisi penyelesaian tugas teori dan praktikum mata kuliah **Pemrograman Modern Python (Pertemuan ke-5)** yang mencakup struktur data string, list, dictionary, set, dan pemrosesan teks.

---

## 📁 Struktur Direktori

```text
├── praktik_1_kalimat.py         # Praktik 1: Analisis kalimat (kata, karakter, terpanjang, title case)
├── praktik_2_nilai.py           # Praktik 2: Statistik nilai mahasiswa (rata-rata, grade, frekuensi)
├── praktik_3_beasiswa.py        # Praktik 3: Operasi himpunan / set (irisan, selisih, gabungan)
├── praktik_4_inventaris.py      # Praktik 4: Manajemen inventaris toko (dict + tuple)
├── praktik_5_frekuensi_kata.py  # Praktik 5: Analisis frekuensi kata & hapax legomena
├── teks.txt                     # Data teks input untuk Praktik 5
├── soal_teori.md                # Jawaban lengkap soal teori pertemuan 5
└── ss/                          # Folder screenshot hasil eksekusi terminal
    ├── praktik_1_kalimat.png
    ├── praktik_2_nilai.png
    ├── praktik_3_beasiswa.png
    ├── praktik_4_inventaris.png
    └── praktik_5_frekuensi_kata.png
```

---

## 🚀 Ringkasan Materi & Program Praktik

### 1. Praktik 1 - Analisis Kalimat (`praktik_1_kalimat.py`)
- Menerima masukan kalimat dari pengguna.
- Menghitung jumlah kata dan jumlah karakter.
- Mencari kata terpanjang beserta panjang karakternya.
- Mengubah format kalimat menjadi *Title Case*.

### 2. Praktik 2 - Statistik Nilai Mahasiswa (`praktik_2_nilai.py`)
- Menerima kumpulan nilai mahasiswa yang dipisahkan spasi.
- Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
- Mengelompokkan nilai ke dalam kategori grade (A, B, C, D, E).
- Menghitung frekuensi kemunculan masing-masing grade.

### 3. Praktik 3 - Operasi Himpunan Mahasiswa Beasiswa (`praktik_3_beasiswa.py`)
- Memanfaatkan tipe data `set` untuk mengelola data ID mahasiswa penerima beasiswa A dan B.
- Menggunakan operasi himpunan:
  - **Irisan (`&`)**: Mahasiswa penerima kedua beasiswa.
  - **Selisih (`-`)**: Penerima hanya salah satu beasiswa.
  - **Gabungan (`|`)**: Seluruh penerima unik.

### 4. Praktik 4 - Inventaris Toko (`praktik_4_inventaris.py`)
- Menggunakan struktur data `dict` dengan format `{nama_barang: (harga, stok)}`.
- Fungsi penambahan barang baru (`tambah_barang`).
- Pembaruan stok dengan konsep *immutable tuple* (`update_stok`).
- Pencarian barang berdasarkan rentang harga tertentu (`cari_by_harga`).
- Perhitungan total nilai aset inventaris (`total_nilai`).

### 5. Praktik 5 - Analisis Frekuensi Kata (`praktik_5_frekuensi_kata.py`)
- Membaca dan men-tokenisasi teks dari file `teks.txt`.
- Menghitung frekuensi kemunculan tiap kata menggunakan dictionary.
- Menampilkan 10 kata yang paling sering muncul.
- Mendeteksi *hapax legomena* (kata yang hanya muncul satu kali) menggunakan `set`.
- Menghitung rasio *Type-Token* (TTR).

---

## 📸 Tangkapan Layar Eksekusi (Terminal)

Screenshot hasil eksekusi dari masing-masing program tersimpan lengkap di folder [`ss/`](./ss).
