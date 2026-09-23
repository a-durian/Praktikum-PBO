# # 

# ### Private!!
# class RekeningBank:
#     def __init__(self, pemilik, saldo):
#         self.pemilik = pemilik
#         self.__saldo = saldo # private

#     def tarik_saldo(self, jumlah):
#         if jumlah > self.__saldo:
#             print("Saldo tidak cukup.")
#         elif jumlah <= 0:
#             print("Jumlah penarikan tidak valid.")
#         else:
#             self.__saldo -= jumlah
#             print(f"Berhasil menarik {jumlah}. Sisa saldo: {self.__saldo}")

#     def cek_saldo(self):
#         print(f"Saldo saat ini: {self.__saldo}")

# rekening = RekeningBank("Budi", 100000)
# rekening.tarik_saldo(30000)
# rekening.cek_saldo()
# print(rekening.__saldo) ## AttributeError, karena sudah di-name-mangling

# akses "paksa" ke private tetap mungkin lewat name mangling, tapi ini
# melanggar konvensi encapsulation dan sebaiknya TIDAK dilakukan:
# print(rekening._RekeningBank__saldo) # 70000, tapi ini praktik yang buruk

## GETTER & SETTER

class RekeningBank:
    def __init__(self, pemilik, saldo):
        self.__pemilik = pemilik
        self.__saldo = saldo

    def get_saldo(self):
        return self.__saldo

    def set_saldo(self, saldo_baru):
        if saldo_baru > 0:
            self.__saldo = saldo_baru

drian = RekeningBank("drian", 6700000)
print(drian.get_saldo())
drian.set_saldo(-5000)
print(drian.get_saldo())

class MMORPG:
    def __init__(self,nama, hp, damage):
        self.nama = nama
        self.hp = hp
        self.damage = damage
        
