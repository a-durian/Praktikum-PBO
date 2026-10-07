# INHERITANCE
class CatatanTransaksi:
    # """Sama seperti materi UML class relationships."""
    def __init__(self, id_transaksi, tipe, nominal, keterangan):
        self.id_transaksi = id_transaksi
        self.tipe = tipe
        self.nominal = nominal
        self.keterangan = keterangan
    def __str__(self):
        simbol = "+" if self.tipe == "KREDIT" else "-"
        return f"[{self.id_transaksi}] {self.tipe:<6} {simbol}Rp{self.nominal:,} | Ket: {self.keterangan}"

class Rekening:
# """Superclass: atribut dan method yang dimiliki SEMUA jenis rekening."""

    def __init__(self, nomor_rekening, nama_pemilik, saldo_awal=0):
        self.nomor_rekening = nomor_rekening
        self.nama_pemilik = nama_pemilik
        self._saldo = saldo_awal # protected: boleh diakses subclass
        self._riwayat = [] # komposisi dengan CatatanTransaksi
    
        if saldo_awal > 0:
            self._buat_catatan("KREDIT", saldo_awal, "Setoran awal pembukaan rekening")

    @property
    def saldo(self):
        return self._saldo
    def _buat_catatan(self, tipe, nominal, keterangan):
        id_baru = f"TRX-{len(self._riwayat) + 1:04d}"
        self._riwayat.append(CatatanTransaksi(id_baru, tipe, nominal, keterangan))
    
    def setor(self, nominal, keterangan="Setor tunai"):
        if nominal <= 0:
            print(" Nominal setoran tidak valid.")
            return
        self._saldo += nominal
        self._buat_catatan("KREDIT", nominal, keterangan)
        print(f" Setoran Rp{nominal:,} berhasil dicatat.")
    def tarik(self, nominal, keterangan="Tarik tunai"):
        if nominal <= 0:
            print(" Nominal penarikan tidak valid.")
        elif nominal > self._saldo:
            print(" Saldo tidak mencukupi untuk transaksi.")
        else:
            self._saldo -= nominal
            self._buat_catatan("DEBET", nominal, keterangan)
            print(f" Penarikan Rp{nominal:,} berhasil dicatat.")
    def cetak_rekening_koran(self):
        print(f"\n Rekening Koran: {self.nomor_rekening} an {self.nama_pemilik}")
        print(f" Jenis Rekening: {type(self).__name__}")
        print(f" Saldo Akhir: Rp{self._saldo:,}")
        print(" Riwayat Mutasi Transaksi:")
        for trx in self._riwayat:
            print(f" {trx}")