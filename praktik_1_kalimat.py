"""Praktik 1 - Analisis kalimat."""

kalimat = input("Masukkan sebuah kalimat: ").strip()
kata = kalimat.split()

# (a) jumlah kata
print(f"Jumlah kata       : {len(kata)}")

# (b) jumlah karakter (termasuk spasi)
print(f"Jumlah karakter   : {len(kalimat)}")

# (c) kata terpanjang
if kata:
    terpanjang = max(kata, key=len)
    print(f"Kata terpanjang   : {terpanjang} ({len(terpanjang)} huruf)")
else:
    print("Kata terpanjang   : -")

# (d) title case
print(f"Title case        : {kalimat.title()}")
