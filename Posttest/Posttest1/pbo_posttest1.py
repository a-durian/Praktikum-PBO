# Tema: Sistem Manajemen Karakter dan Pertarungan Arena MMORPG
# Dworian Arena

class Item:
    total_item = 0
    
    def __init__(self, nama, bonus_damage):
        self.nama = nama
        self.__bonus_damage = 0
        self.bonus_damage = bonus_damage
    @property
    def bonus_damage(self):
        return self.__bonus_damage
    
    @bonus_damage.setter
    def bonus_damage(self,nilai):
        if nilai < 0:
            self.__bonus_damage = 0
        else:
            self.__bonus_damage = nilai
        
    @classmethod
    def item_starter(cls):
        return cls("Atk Potion", 10)
    
    @staticmethod
    def item_starter(nama) -> bool:
        return len(nama.strip()) >= 3
        
class Character:
    total_character = 0
    max_level = 15
    game_title = "Dworian Arena"
    
    def __init__(self, name, role, hp, damage):
        self.name = name
        self.role = role
        self.level = 1
        self.hp = hp
        self.energy = 100
        self.damage = damage
        self.equipment = Item("Starter Sword", 0)
    
    @property
    def hp(self):
        return self.__hp
    
    @hp.setter
    def hp(self, nilai):
        if nilai < 0:
            self.__hp = 0
        else:
            self.__hp = nilai
            
    @property
    def damage(self):
        return self.__damage
    
    @damage.setter
    def damage(self, nilai):
            if nilai < 0:
                self.__damage = 0
            else:
                self.__damage = nilai
    def get_total_damage(self) -> int:
        return self.damage + self.equipment.bonus_damage
    
    def upgrade_level(self):
        if self.level >= self.max_level:
            print(f"[!] {self.name} sudah mencapai level maksimal ({self.max_level}).")
            return
        self.level += 1
        self.hp += 20
        self.damage += 5
        print(f"[+] {self.name} naik lvl {self.level}! (+20 HP, +5 Base Dmg)")
    
    def info(self):
            print(f"{self.name} | HP: {self.hp} | Energy: {self.energy} | Dmg: {self.damage}")
        
    @classmethod
    def reset_counter(cls):
        cls.total_character = 0
        
    @staticmethod
    def validasi_nama(nama) -> bool:
        return len(nama.strip()) >= 3

class Arena:
    nama_instansi = "Dworian Battle Arena"
    
    def __init__(self, nama_arena):
        self.nama_arena = nama_arena
        self.__daftar_karakter = []
        
    @property
    def daftar_karakter(self):
        return self.__daftar_karakter
    
    def create_character(self, name, role, hp, damage):
        if not Character.validasi_nama(name):
            print("[!] Gagal membuat karakter!")
            
        karakter_baru = Character(name, role, hp, damage)
        self.__daftar_karakter.append(karakter_baru)
        print(f"[+] Karakter {name} ({role}) berhasil dibuat!")
    
    def read_character(self):
        print(f"\n=== DAFTAR KARAKTER DI {(self.nama_arena.upper())} ===")
        if not self.__daftar_karakter:
            print("...Blum ada karakter yang terdaftar...")
            return
        for i, c in enumerate(self.__daftar_karakter, 1):
            print(f"{i}. ", end="")
            c.info()
            
    def update_character(self, index):
        if not (0 <= index < len(self.__daftar_karakter)):
            print("[!] Karakter tidak ditemukan.")
            return
        target = self.__daftar_karakter[index]
        print(f"\n--- REVAMP/UPDATE: {target.name} ---")
        print("1. Level Up")
        print("2. Ganti Nama")
        print("3. Ganti Equipment")
        pilihan = input("Pilih menu update:")
        
        if pilihan == "1":
            target.upgrade_level()
        elif pilihan == "2":
            nama_baru = input("Masukkan nama baru: ")
            if Character.validasi_nama(nama_baru):
                target.name = nama_baru
                print(f"[^] Nama berhasil diubah menjadi {target.name}")
            else:
                print("[!] Nama tidak valid !")
        elif pilihan == "3":
            nama_item = input("Nama equipment baru: ")
            try: 
                bonus = int(input("Bonus damage equipment:"))
                target.equipment = Item(nama_item, bonus)
                print(f"[^] Equipment {target.name} diubah menjadi {target.equipment.nama} ")
            except ValueError:
                print("[!] Bonus damage harus berupa angka!")
        else:
            print("[!] Pilihan tidak valid!")
    
    def delete_character(self, index):
        if not (0 <= index < len(self.__daftar_karakter)):
            print("[! Karakter tidak ditemukan")
            return
        dihapus = self.__daftar_karakter.pop(index)
        print(f"[^] Karakter '{dihapus.nama} berhasil dihapus!")

    @classmethod
    def ubah_instansi(cls, nama_baru):
        cls.nama_instansi = nama_baru
        
    @staticmethod
    def ubah_instansi(cls, nama_baru):
        cls.nama_instansi = nama_baru
        
    @staticmethod
    def estimasi_durasi_match(jumlah_peta) -> int:
        return jumlah_peta * 5
    
# MAIN MENUUU
if __name__ == "__main__":
    arena_utama = Arena("Colosseum Dworian")
    
    arena_utama.create_character("Drian", "Fighter", 150, 25)
    arena_utama.create_character("eudora", "Mage", 100, 40)
    
    while True:
        print(f"\n========== MENU CRUD {Arena.nama_instansi.upper()} ==========")
        print("1. [CREATE] Buat Karakter Baru")
        print("2. [READ]   Tampilkan Semua Karakter")
        print("3. [UPDATE] Revamp / Upgrade Karakter")
        print("4. [DELETE] Hapus Karakter")
        print("5. Keluar")
        
        pilihan = input("pilih menu: ")
        
        if pilihan == "1":
            nama = input("Nama Karakter : ")
            role = input("Class/Role    : ")
            try:
                hp = int(input("Base HP     : "))
                damage = int(input("Base Damage    :"))
                arena_utama.create_character(nama, role, hp, damage)
            except ValueError:
                print("[!] HP dan Damage harus berupa angka!")
                
        elif pilihan == "2":
            arena_utama.read_character()
        
        elif pilihan == "3":
            arena_utama.read_character()

            if arena_utama.daftar_karakter:
                try:
                   idx = int(input("\nPilih karakter yang mau diupdate: ")) - 1
                   arena_utama.update_character(idx)
                except ValueError:
                    print("[!] Input harus berupa angka nomor urut!") 
                    
        elif pilihan == "4":
            arena_utama.read_character()
            if arena_utama.daftar_karakter:
                try:
                    idx = int(input("Pilih nomor karakter yg mau dihapus: ")) - 1                        
                    arena_utama.delete_character(idx)
                except ValueError:
                    print("[!] Input harus berupa angka nomor urut!")
                        
        elif pilihan == "5":
            print("\nThenkyuu! Program dihentikan..")
            break
        else:
            print("[!] Pilihan tidak valid!")    

