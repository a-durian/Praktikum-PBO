# print("Hello, World!")

# class Product:
#     def __init__(self, name, price, stock, category, brand):
#         self.name = name
#         self.price = price
#         self.stock = stock
#         self.category = category
#         self.brand = brand
#     def tambah_stok(self, jumlah):
#         self.stock += jumlah    
#     def kurangi_stok(self, jumlah):
#         if self.stock >= jumlah:
#             self.stock -= jumlah
#     def ubah_harga(self, harga_baru):
#         self.price = harga_baru

# class Laptop:
#     pass


#* ATRIBUT INSTANCE
class Tim:
    def __init__(self, nama, ceo):
        self.nama = nama
        self.ceo = ceo
        
rrq = Tim("RRQ Hoshi", "Pak AP")
evos = Tim("Evos Legends", "Hartman Harris")

print(rrq.nama) # RRQ Hoshi
print(evos.nama) # Evos Legends

# ATRIBUT KELAS
class Tim:
    nama_liga = "MPL Indonesia"

    def __init__(self, nama, ceo):
        self.nama = nama
        self.ceo = ceo

rrq = Tim("RRQ", "Pak AP")
evos = Tim("Evos Legends", "Hartman Harris")

print(rrq.nama_liga) # MPL Indonesia
print(evos.nama_liga) # MPL Indonesia

#INSTANCE METHOD
class Pertandingan:
    def __init__(self, tim_a, tim_b):
        self.tim_a = tim_a
        self.tim_b = tim_b
        self.skor_a = 0
        self.skor_b = 0
        self.selesai = False
    def tambah_skor(self, tim, poin=1):
        if tim == self.tim_a:
            self.skor_a += poin
        elif tim == self.tim_b:
            self.skor_b += poin
        else:
            print(f"{tim} tidak terdaftar di pertandingan ini!")
    def selesaikan(self):
        self.selesai = True
    def tampilkan_hasil(self):
        status = "Selesai" if self.selesai else "Berlangsung"
        print(f"{self.tim_a} {self.skor_a} - {self.skor_b} {self.tim_b} ({status})")

final = Pertandingan("RRQ", "Evos Legends")
final.tambah_skor("RRQ", 2)
final.tambah_skor("Evos Legends", 1)
final.selesaikan()
final.tampilkan_hasil() # RRQ 2 - 1 Evos Legends (Selesai)

#CLASS METHOD
# class Jadwal:
# musim_liga = "MPL Indonesia Season 14"
# def __init__(self, tim_a, tim_b, tanggal):
# self.tim_a = tim_a
# self.tim_b = tim_b
# self.tanggal = tanggal
# # Class method sebagai factory method -- buat objek dari dictionary
# def dari_dict(cls, data):
# """Alternatif konstruktor: buat Jadwal dari data berbentuk
# dictionary."""
# return cls(data["tim_a"], data["tim_b"], data["tanggal"])
# @classmethod
# def ganti_musim(cls, musim_baru):
# """Mengubah musim liga aktif, berlaku untuk seluruh objek
# Jadwal."""
# cls.musim_liga = musim_baru
# def info(self):
# print(f"{self.tim_a} vs {self.tim_b} - {self.tanggal}
# ({Jadwal.musim_liga})\n")
# data_laga = {"tim_a": "RRQ", "tim_b": "Evos Legends", "tanggal": "12
# September 2026"}
# data_laga2 = {"tim_a": "ONIC", "tim_b": "Alter Ego", "tanggal": "13
# September 2026"}
# laga1 = Jadwal.dari_dict(data_laga)
# laga2 = Jadwal.dari_dict(data_laga2)
# laga1.info() # RRQ vs Evos Legends - 12 September 2026 (MPL Indonesia
# Season 14)
# laga2.info() # ONIC vs Alter Ego - 13 September 2026 (MPL Indonesia
# Season 14)
# Jadwal.ganti_musim("MPL Indonesia Season 15")
# laga1.info() # RRQ vs Evos Legends - 12 September 2026 (MPL Indonesia
# Season 15)
# laga2.info() # ONIC vs Alter Ego - 13 September 2026 (MPL Indonesia
# Season 15)

print("hello worudooo")