"""Praktik 4 - Inventaris toko: dict {nama_barang: (harga, stok)}."""

inventaris = {
    "Pensil": (2500, 100),
    "Buku Tulis": (7000, 50),
    "Penghapus": (1500, 80),
    "Pulpen": (4000, 60),
}


# (a) tambah barang baru
def tambah_barang(inv, nama, harga, stok):
    if nama in inv:
        print(f"'{nama}' sudah ada. Gunakan update_stok().")
        return
    inv[nama] = (harga, stok)
    print(f"'{nama}' ditambahkan.")


# (b) update stok (tuple immutable -> buat tuple baru)
def update_stok(inv, nama, stok_baru):
    if nama not in inv:
        print(f"'{nama}' tidak ditemukan.")
        return
    harga, _ = inv[nama]
    inv[nama] = (harga, stok_baru)
    print(f"Stok '{nama}' diubah menjadi {stok_baru}.")


# (c) cari barang berdasarkan rentang harga
def cari_by_harga(inv, harga_min, harga_max):
    return {
        nama: data
        for nama, data in inv.items()
        if harga_min <= data[0] <= harga_max
    }


# (d) total nilai inventaris
def total_nilai(inv):
    return sum(harga * stok for harga, stok in inv.values())


if __name__ == "__main__":
    print("Awal:", inventaris)

    tambah_barang(inventaris, "Spidol", 6000, 40)
    update_stok(inventaris, "Pensil", 120)

    hasil = cari_by_harga(inventaris, 2000, 5000)
    print("\nBarang harga Rp2.000 - Rp5.000:")
    for nama, (harga, stok) in hasil.items():
        print(f"  {nama}: Rp{harga:,} (stok {stok})")

    print(f"\nTotal nilai inventaris: Rp{total_nilai(inventaris):,}")
