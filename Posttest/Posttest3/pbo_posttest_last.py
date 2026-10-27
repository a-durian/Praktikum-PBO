# Tema: Sistem Manajemen Karakter dan Pertarungan Arena MMORPG
# Dworian Arena

from abc import ABC, abstractmethod

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
    def bonus_damage(self, nilai):
        if nilai < 0:
            self.__bonus_damage = 0
        else:
            self.__bonus_damage = nilai

    @classmethod
    def item_starter(cls):
        return cls("Atk Potion", 10)

    @staticmethod
    def validasi_nama_item(nama) -> bool:
        return len(nama.strip()) >= 3


# ABSTRACT CLASS
class Character(ABC):
    total_character = 0
    max_level = 15
    game_title = "Dworian Arena"

    # AGREGASI
    def __init__(self, name, role, hp, damage, equipment):
        self.name = name
        self.role = role
        self.level = 1
        self.hp = hp
        self.energy = 100
        self.damage = damage
        self.equipment = equipment

    # PRIVATE
    @property
    def hp(self):
        return self.__hp

    @hp.setter
    def hp(self, nilai):
        if nilai < 0:
            self.__hp = 0
        else:
            self.__hp = nilai

    # PROTECTED
    @property
    def damage(self):
        return self._damage

    @damage.setter
    def damage(self, nilai):
        if nilai < 0:
            self._damage = 0
        else:
            self._damage = nilai

    @abstractmethod
    def get_total_damage(self) -> int:
        """Wajib diimplementasikan oleh subclass."""
        pass

    @abstractmethod
    def skill_spesial(self, target) -> str:
        """Wajib diimplementasikan oleh subclass. Mengembalikan pesan hasil skill."""
        pass

    def _pakai_energy(self, biaya) -> bool:
        if self.energy < biaya:
            return False
        self.energy -= biaya
        return True
    def serang(self, target):
        dmg = self.get_total_damage()
        target.hp -= dmg
        print(f"[x] {self.name} menyerang {target.name} (-{dmg} HP). Sisa HP {target.name}: {target.hp}")

    def upgrade_level(self):
        if self.level >= self.max_level:
            print(f"[!] {self.name} sudah mencapai level maksimal ({self.max_level}).")
            return
        self.level += 1
        self.hp += 20
        self.damage += 5
        self.energy = 100
        print(f"[+] {self.name} naik lvl {self.level}! (+20 HP, +5 Base Dmg, Energy penuh)")

    def info(self):
        print(f"{self.name} | HP: {self.hp} | Energy: {self.energy} | Dmg: {self.damage}")

    # OPERATOR OVERLOADING
    def __str__(self):
        return f"{self.name} ({self.role}) Lv.{self.level} | Total Dmg: {self.get_total_damage()}"

    def __lt__(self, other):
        return self.get_total_damage() < other.get_total_damage()

    @classmethod
    def reset_counter(cls):
        cls.total_character = 0

    @staticmethod
    def validasi_nama(nama) -> bool:
        return len(nama.strip()) >= 3

class Fighter(Character):
    def __init__(self, name, hp, damage, equipment, armor=10):
        super().__init__(name, "Fighter", hp, damage, equipment)
        self.armor = armor

    def get_total_damage(self) -> int:
        return self._damage + self.equipment.bonus_damage

    def skill_spesial(self, target) -> str:
        if not self._pakai_energy(20):
            return f"[!] {self.name} kehabisan energy untuk Shield Bash!"
        dmg = self.get_total_damage() + self.armor
        target.hp -= dmg
        return f"[SKILL] {self.name} (Fighter) Shield Bash ke {target.name} (-{dmg} HP). Sisa HP: {target.hp}"

    def info(self):
        super().info()
        print(f"   Armor: {self.armor}")

class Mage(Character):
    def __init__(self, name, hp, damage, equipment, mana=50):
        super().__init__(name, "Mage", hp, damage, equipment)
        self.mana = mana 

    def get_total_damage(self) -> int:
        return self._damage + self.equipment.bonus_damage + (self.mana // 10)

    def skill_spesial(self, target) -> str:
        if not self._pakai_energy(30):
            return f"[!] {self.name} kehabisan energy untuk Fireball!"
        dmg = self.get_total_damage() * 2
        target.hp -= dmg
        return f"[SKILL] {self.name} (Mage) Fireball ke {target.name} (-{dmg} HP). Sisa HP: {target.hp}"

    def info(self):
        super().info()
        print(f"   Mana: {self.mana}")

class KonsolLog:
    def catat(self, pesan):
        print(f"   [LOG-KONSOL] {pesan}")


class FileLog:
    def __init__(self, nama_file="riwayat_arena.txt"):
        self.nama_file = nama_file

    def catat(self, pesan):
        with open(self.nama_file, "a", encoding="utf-8") as f:
            f.write(pesan + "\n")


def catat_ke_semua(daftar_pencatat, pesan):
    for pencatat in daftar_pencatat:
        pencatat.catat(pesan)


class Arena:
    nama_instansi = "Dworian Battle Arena"

    daftar_role = {"fighter": Fighter, "mage": Mage}

    def __init__(self, nama_arena, daftar_pencatat):
        self.nama_arena = nama_arena
        self.__daftar_karakter = []
        self.__daftar_pencatat = daftar_pencatat

    @property
    def daftar_karakter(self):
        return self.__daftar_karakter

    def __len__(self):
        return len(self.__daftar_karakter)

    def create_character(self, name, role, hp, damage):
        if not Character.validasi_nama(name):
            print("[!] Gagal membuat karakter!")
            return

        kelas_role = self.daftar_role.get(role.lower())
        if kelas_role is None:
            print(f"[!] Role '{role}' tidak dikenal. Pilihan: {', '.join(r.title() for r in self.daftar_role)}")
            return

        item_awal = Item("Starter Sword", 0)
        karakter_baru = kelas_role(name, hp, damage, item_awal)
        self.__daftar_karakter.append(karakter_baru)
        print(f"[+] Karakter {name} ({karakter_baru.role}) berhasil dibuat!")

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
            print("[!] Karakter tidak ditemukan")
            return
        dihapus = self.__daftar_karakter.pop(index)
        print(f"[^] Karakter '{dihapus.name} berhasil dihapus!")

    def adu_skill(self, index_target):
        if not (0 <= index_target < len(self.__daftar_karakter)):
            print("[!] Karakter tidak ditemukan.")
            return
        target = self.__daftar_karakter[index_target]
        print(f"\n=== SEMUA KARAKTER MENYERANG {target.name.upper()} ===")
        for penyerang in self.__daftar_karakter:
            if penyerang is target:
                continue
            penyerang.serang(target)
            pesan = penyerang.skill_spesial(target)
            catat_ke_semua(self.__daftar_pencatat, pesan)  # duck typing

    def ranking_damage(self):
        print("\n=== RANKING TOTAL DAMAGE ===")
        if not self.__daftar_karakter:
            print("...Blum ada karakter yang terdaftar...")
            return
        for i, c in enumerate(sorted(self.__daftar_karakter, reverse=True), 1):
            print(f"{i}. {c}")
        print(f"Jumlah karakter di arena: {len(self)}")

    @classmethod
    def ubah_instansi(cls, nama_baru):
        cls.nama_instansi = nama_baru

    @staticmethod
    def estimasi_durasi_match(jumlah_peta) -> int:
        return jumlah_peta * 5

def bukti_abstraksi():
    print("=== BUKTI ABSTRAKSI ===")
    try:
        Character("Test", "Test", 100, 10, Item("Test Item", 0))
    except TypeError as e:
        print(f"[OK] Character tidak bisa dibuat langsung -> TypeError: {e}")


# MAIN MENUUU
if __name__ == "__main__":
    bukti_abstraksi()
    arena_utama = Arena("Colosseum Dworian", [KonsolLog(), FileLog()])
    arena_utama.create_character("Drian", "Fighter", 150, 25)
    arena_utama.create_character("eudora", "Mage", 100, 40)

    while True:
        print(f"\n========== MENU CRUD {Arena.nama_instansi.upper()} ==========")
        print("1. [CREATE] Buat Karakter Baru")
        print("2. [READ]   Tampilkan Semua Karakter")
        print("3. [UPDATE] Revamp / Upgrade Karakter")
        print("4. [DELETE] Hapus Karakter")
        print("5. [BATTLE] Semua Karakter Serang 1 Target")
        print("6. [RANK]   Ranking Total Damage")
        print("7. Keluar")

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
            arena_utama.read_character()
            if arena_utama.daftar_karakter:
                try:
                    idx = int(input("Pilih nomor karakter yang jadi target: ")) - 1
                    arena_utama.adu_skill(idx)
                except ValueError:
                    print("[!] Input harus berupa angka nomor urut!")

        elif pilihan == "6":
            arena_utama.ranking_damage()

        elif pilihan == "7":
            print("\nThenkyuu! Program dihentikan..")
            break
        else:
            print("[!] Pilihan tidak valid!")