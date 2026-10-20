"""Praktik 5 - Analisis frekuensi kata dari file teks.

Pemakaian:
    python praktik_5_frekuensi_kata.py              (default: teks.txt)
    python praktik_5_frekuensi_kata.py file_lain.txt
"""
import re
import sys

nama_file = sys.argv[1] if len(sys.argv) > 1 else "teks.txt"

try:
    with open(nama_file, encoding="utf-8") as f:
        teks = f.read()                      # string
except FileNotFoundError:
    print(f"File '{nama_file}' tidak ditemukan.")
    raise SystemExit(1)

# tokenisasi: huruf kecil, ambil kata saja (list)
kata = re.findall(r"[a-zA-Z']+", teks.lower())

if not kata:
    print("File tidak berisi kata.")
    raise SystemExit

# (a) frekuensi tiap kata (dict)
frekuensi = {}
for k in kata:
    frekuensi[k] = frekuensi.get(k, 0) + 1

# (b) 10 kata paling sering
top10 = sorted(frekuensi.items(), key=lambda item: item[1], reverse=True)[:10]
print("10 kata paling sering muncul:")
for i, (k, n) in enumerate(top10, start=1):
    print(f"  {i:>2}. {k:<15} {n}")

# (c) hapax legomena (set)
hapax = {k for k, n in frekuensi.items() if n == 1}
print(f"\nHapax legomena ({len(hapax)} kata):")
print("  ", sorted(hapax))

# (d) type-token ratio
jenis = len(set(kata))
total = len(kata)
print(f"\nKata unik (type) : {jenis}")
print(f"Total kata (token): {total}")
print(f"Type-token ratio  : {jenis / total:.4f}")
