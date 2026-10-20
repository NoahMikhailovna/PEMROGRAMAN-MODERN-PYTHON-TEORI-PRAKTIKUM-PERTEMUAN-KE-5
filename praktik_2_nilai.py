"""Praktik 2 - Statistik nilai mahasiswa."""


def tentukan_grade(nilai):
    if nilai >= 85:
        return "A"
    elif nilai >= 70:
        return "B"
    elif nilai >= 55:
        return "C"
    elif nilai >= 40:
        return "D"
    return "E"


masukan = input("Masukkan nilai (pisahkan dengan spasi): ").split()
nilai = [float(n) for n in masukan]

if not nilai:
    print("Tidak ada nilai yang dimasukkan.")
    raise SystemExit

# (a) rata-rata
print(f"Rata-rata : {sum(nilai) / len(nilai):.2f}")

# (b) tertinggi & terendah
print(f"Tertinggi : {max(nilai)}")
print(f"Terendah  : {min(nilai)}")

# (c) kelompokkan ke kategori
kelompok = {"A": [], "B": [], "C": [], "D": [], "E": []}
for n in nilai:
    kelompok[tentukan_grade(n)].append(n)

# (d) frekuensi tiap kategori
frekuensi = {grade: len(daftar) for grade, daftar in kelompok.items()}

print("\nPengelompokan nilai:")
for grade, daftar in kelompok.items():
    print(f"  {grade}: {daftar}")

print("\nFrekuensi:")
for grade, jumlah in frekuensi.items():
    print(f"  {grade}: {jumlah}")
