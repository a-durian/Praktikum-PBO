# ===== ASOSIASI ====

class Nasabah:
    def __init__(self, nama, nomor_rekening):
        self.nama = nama
        self.nomor_rekening = nomor_rekening
        
    def tarik_tunai(self, atm, jumlah):
        atm.saldo_kas -= jumlah

class MesinATM:
    def __init__(self, id_atm, lokasi, saldo_kas):
        self.id_atm = id_atm
        self.lokasi = lokasi
        self.saldo_kas =  saldo_kas

adrian = Nasabah("Adrian", 2509106043)
atm_pusat = MesinATM("Pusat", "Samarinda", 67000)

adrian.tarik_tunai(atm_pusat, 500)

print(f"\n{atm_pusat.saldo_kas}\n")

# ==== AGREGASI ====
# Ciri-ciri Agregasi:
# ● Objek bagian dibuat di luar objek induk
# ● Objek bagian dikirim ke objek induk melalui konstruktor atau method
# ● Jika objek induk dihapus dari memori, objek bagian tetap ada

class Bank:
    def __init__(self, nama_bank, kode):
        self.nama_bank = nama_bank
        self.kode = kode
        self.karyawan = []

    def tambah_karyawan(self, karyawan):
        self.karyawan.append(karyawan)

class Karyawan:
    def __init__(self, nama, nip, posisi):
        self.nama = nama
        self.nip = nip
        self.posisi = posisi

bank = Bank("Mandiri", "0067")
adrian = Karyawan("Adrian", 2509106032, "Manager")
puky = Karyawan("Puky", 2509106067, "Cuky")

bank.tambah_karyawan(adrian)
# del bank
# del adrian
print(adrian.nama, adrian.nip)
print(puky.nama, puky.nip, puky.posisi)
print(bank.nama_bank)
print("\n")

# ==== KOMPOSISI ====
class Bank:
    def __init__(self, nama_bank, kode):
        self.nama_bank = nama_bank
        self.kode = kode
        self.karyawan = []

    def tambah_karyawan(self, karyawan):
        self.karyawan.append(karyawan)

class Karyawan:
    def __init__(self, nama, nip, posisi):
        self.nama = nama
        self.nip = nip
        self.posisi = posisi


print("hellow world")
print("hellow world")