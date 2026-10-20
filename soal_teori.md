# Latihan Soal Teori — Struktur Data Python

Modul: String, List, Tuple, Set, Dictionary & Pemilihan Struktur Data

---

## Soal 1

**Jelaskan perbedaan mendasar antara list dan tuple dalam Python. Berikan contoh skenario di mana tuple lebih tepat digunakan daripada list, dan sebaliknya.**

### Jawaban

Perbedaan mendasarnya ada di **mutabilitas**. List bersifat *mutable* (isi, urutan, dan ukurannya bisa diubah setelah dibuat), sedangkan tuple bersifat *immutable* (tidak bisa diubah setelah dibuat).

| Aspek | List | Tuple |
|---|---|---|
| Sintaks | `[1, 2, 3]` | `(1, 2, 3)` |
| Mutable | Ya | Tidak |
| Metode | Banyak (`append`, `insert`, `remove`, `pop`, `sort`, dll.) | Hanya `count()` dan `index()` |
| Hashable | Tidak | Ya (jika semua isinya hashable) |
| Bisa jadi kunci dict / elemen set | Tidak | Ya |
| Performa iterasi | Sedikit lebih lambat | Sedikit lebih cepat |

**Kapan tuple lebih tepat:**
- Data bersifat konstan, misalnya koordinat `(-6.2088, 106.8456)`, tanggal `(2026, 10, 20)`, atau warna RGB `(255, 128, 0)`.
- Data dipakai sebagai kunci dictionary, misalnya `{(0, 0): "origin"}`.
- Fungsi mengembalikan beberapa nilai sekaligus (`return nilai_min, nilai_max`).
- Ingin menegaskan secara semantik bahwa data tidak boleh berubah.

**Kapan list lebih tepat:**
- Data perlu ditambah, dihapus, atau diurutkan selama program berjalan, misalnya daftar mata kuliah yang diambil mahasiswa (bisa tambah/drop), keranjang belanja, atau antrian tugas.

---

## Soal 2

**Mengapa set tidak mendukung pengindeksan seperti list dan tuple? Jelaskan kaitannya dengan implementasi hash table dan sifat unordered.**

### Jawaban

Set diimplementasikan dengan **hash table**. Posisi penyimpanan sebuah elemen ditentukan oleh **nilai hash** elemen tersebut, bukan oleh urutan pemasukannya. Akibatnya:

1. Set bersifat **unordered**: tidak ada jaminan urutan elemen, dan urutan bisa berbeda dari urutan saat elemen dimasukkan.
2. Karena tidak ada urutan yang pasti, konsep "elemen ke-0", "elemen ke-1", dan seterusnya **tidak bermakna**. Memanggil `s[0]` tidak punya arti yang konsisten, sehingga Python melempar `TypeError`.
3. Slicing juga tidak didukung karena slicing bergantung pada urutan.

Set dirancang untuk *keanggotaan* (`x in s`) dan *operasi himpunan*, bukan untuk akses berdasarkan posisi. Kalau butuh akses berindeks, ubah dulu ke list, misalnya `list(s)` atau `sorted(s)`.

```python
s = {10, 20, 30}
# print(s[0])        # TypeError: 'set' object is not subscriptable
print(sorted(s)[0])  # 10 -> konversi ke list terurut dulu
```

---

## Soal 3

**Apa yang dimaksud dengan hashable dalam konteks Python? Sebutkan tiga tipe data yang hashable dan tiga yang tidak hashable. Mengapa kunci dictionary harus hashable?**

### Jawaban

Objek disebut **hashable** jika memiliki nilai hash (`hash(obj)`) yang **tetap selama masa hidup objek** dan dapat dibandingkan dengan objek lain (`==`). Pada praktiknya, tipe immutable umumnya hashable.

- **Hashable:** `int`, `str`, `tuple` (selama semua elemennya hashable). Contoh lain: `float`, `bool`, `frozenset`.
- **Tidak hashable:** `list`, `dict`, `set`.

**Mengapa kunci dictionary harus hashable?**
Dictionary adalah hash table. Saat menyimpan pasangan `kunci: nilai`, Python menghitung `hash(kunci)` untuk menentukan lokasi penyimpanan. Saat mengambil nilai, Python menghitung hash kunci lagi dan langsung menuju lokasi tersebut. Jika kunci bisa berubah (mutable), hash-nya ikut berubah, sehingga Python tidak bisa menemukan lagi lokasi data yang dulu disimpan. Karena itu kunci wajib hashable agar akses tetap konsisten dan cepat (O(1)).

```python
d = {(1, 2): "valid"}      # tuple -> OK
# d = {[1, 2]: "invalid"}  # TypeError: unhashable type: 'list'
```

---

## Soal 4

**Jelaskan mengapa pencarian keanggotaan (operator `in`) pada set memiliki kompleksitas O(1) sedangkan pada list O(n). Apa implikasi praktisnya untuk data besar?**

### Jawaban

- **List:** disimpan sebagai array berurutan tanpa struktur pencarian. Untuk mengecek `x in lst`, Python harus membandingkan `x` dengan elemen satu per satu dari awal sampai ketemu atau habis. Dalam kasus terburuk semua `n` elemen diperiksa, jadi **O(n)**.
- **Set:** disimpan dalam hash table. Untuk mengecek `x in s`, Python menghitung `hash(x)`, lalu langsung memeriksa lokasi (bucket) yang bersesuaian. Jumlah langkahnya hampir tidak bergantung pada ukuran set, jadi rata-rata **O(1)**.

**Implikasi praktis untuk data besar:**
- Pada data kecil perbedaannya nyaris tidak terasa. Pada jutaan elemen, pengecekan berulang pada list bisa sangat lambat, sedangkan set tetap cepat.
- Cocok untuk validasi, filtering, dan deduplikasi data besar. Misalnya mengecek apakah NIM sudah terdaftar di antara 1 juta data: pakai set, bukan list.
- Trade-off: set butuh memori lebih besar karena overhead hash table, dan tidak mempertahankan urutan.

```python
import time

data_list = list(range(1_000_000))
data_set = set(data_list)

t = time.perf_counter(); 999_999 in data_list; print("list:", time.perf_counter() - t)
t = time.perf_counter(); 999_999 in data_set;  print("set :", time.perf_counter() - t)
```

---

## Soal 5

**Apa perbedaan antara metode `sort()` dan fungsi `sorted()` pada list? Kapan sebaiknya menggunakan masing-masing?**

### Jawaban

| Aspek | `lst.sort()` | `sorted(iterable)` |
|---|---|---|
| Jenis | Metode milik list | Fungsi bawaan |
| Efek | Mengurutkan **in-place** (mengubah list asli) | Mengembalikan **list baru**, data asli tidak berubah |
| Nilai kembali | `None` | List terurut |
| Objek yang didukung | Hanya list | Iterable apa pun (list, tuple, set, dict, string, dll.) |

Keduanya mendukung parameter `key` dan `reverse`.

**Kapan dipakai:**
- Gunakan `sort()` jika list asli memang boleh diubah dan ingin hemat memori (tidak membuat salinan).
- Gunakan `sorted()` jika urutan asli harus dipertahankan, atau jika datanya bukan list (misalnya set, tuple, atau `dict.items()`).

```python
angka = [3, 1, 4, 1, 5]
urut = sorted(angka)
print(angka)   # [3, 1, 4, 1, 5]  -> tidak berubah
print(urut)    # [1, 1, 3, 4, 5]

angka.sort()
print(angka)   # [1, 1, 3, 4, 5]  -> berubah

print(sorted({"b", "a", "c"}))  # ['a', 'b', 'c']  -> sorted() bisa untuk set
```
