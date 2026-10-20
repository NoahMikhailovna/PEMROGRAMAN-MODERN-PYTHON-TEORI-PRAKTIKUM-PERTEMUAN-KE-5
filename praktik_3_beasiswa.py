"""Praktik 3 - Operasi set pada penerima beasiswa."""

beasiswa_a = [1001, 1002, 1003, 1004, 1005, 1003]  # ada duplikat sengaja
beasiswa_b = [1004, 1005, 1006, 1007, 1002, 1007]

set_a = set(beasiswa_a)
set_b = set(beasiswa_b)

print("Penerima beasiswa A:", sorted(set_a))
print("Penerima beasiswa B:", sorted(set_b))
print()

# (a) menerima keduanya (irisan)
print("(a) Menerima A dan B      :", sorted(set_a & set_b))

# (b) hanya A
print("(b) Hanya beasiswa A      :", sorted(set_a - set_b))

# (c) B tapi tidak A
print("(c) Beasiswa B, bukan A   :", sorted(set_b - set_a))

# (d) semua mahasiswa unik (gabungan)
semua = set_a | set_b
print("(d) Semua penerima unik   :", sorted(semua), f"(total {len(semua)})")
