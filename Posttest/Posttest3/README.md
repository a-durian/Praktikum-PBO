# Dworian Arena

Program CRUD karakter buat game MMORPG, dibuat pakai Python. Bisa bikin karakter (Fighter atau Mage), lihat daftarnya, update (level up, ganti nama, ganti equipment), sama hapus karakter. Di posttest ini ditambah fitur battle (semua karakter nyerang satu target) dan ranking damage, sekalian nerapin abstraksi dan polimorfisme dari modul 6.

File programnya `dworian_arena.py`, jalanin aja pakai `python dworian_arena.py`.

## Class Diagram

![Class Diagram](class_diagram.png)

Penjelasan relasinya:

**Asosiasi: Character ke Character.** Di method `serang(target)`, satu Character make Character lain sebagai target. Keduanya hidup sendiri-sendiri, nggak ada yang memiliki yang lain, makanya asosiasi.

**Agregasi: Character ke Item.** Item (equipment) dibuat di luar Character terus dikirim lewat parameter `equipment`. Kalau Character-nya dihapus, Item-nya masih ada, jadi aku pilih agregasi.

**Agregasi: Arena ke KonsolLog dan FileLog.** Sama kayak di atas, pencatat dibuat di luar (di bagian main) terus dimasukin ke Arena lewat `__init__`. Arena nggak bikin sendiri.

**Komposisi: Arena ke Character.** Character dibuat langsung di dalam `Arena.create_character()` dan disimpan di list private `__daftar_karakter`. Jadi karakternya cuma ada di dalam Arena, kalau dihapus dari Arena ya hilang.

Bedanya agregasi sama komposisi ada di siapa yang bikin objeknya dan apa yang terjadi kalau "pemiliknya" hilang. Item dibuat dari luar jadi tetap ada, sedangkan Character dibuat dan dipegang Arena sendiri jadi ikut hilang.

(Pewarisan Fighter dan Mage ke Character juga ada di diagram, tapi itu bukan relasi yang diminta.)

## Abstraksi

Abstract class-nya adalah `Character(ABC)`. Di dalamnya ada 2 abstract method:
- `get_total_damage()`
- `skill_spesial(target)`

Dua-duanya wajib ditulis ulang di subclass, dan sudah diimplementasi oleh `Fighter` dan `Mage`.

Method konkret yang dipakai bareng semua subclass: `serang()`, `_pakai_energy()`, `upgrade_level()`, dan `info()`. Misalnya `serang()` manggil `get_total_damage()` tanpa peduli dia lagi dipanggil dari Fighter atau Mage, konsepnya mirip `jalankan()` di materi.

Konsep inheritance dari posttest sebelumnya tetap dipakai: `super().__init__()`, atribut unik (`armor` buat Fighter, `mana` buat Mage), `__hp` yang private, dan `_damage` yang protected.

Buat buktiin abstract class nggak bisa dibuat objeknya, ada fungsi `bukti_abstraksi()` yang jalan otomatis tiap program dimulai (hasilnya ada di bagian output).

## Polimorfisme

**Lewat pewarisan.** `get_total_damage()` dan `skill_spesial()` di-override sama Fighter dan Mage dengan hasil yang beda (Fighter pakai Shield Bash, Mage pakai Fireball). Dipanggil dalam satu loop di `Arena.adu_skill()`, isinya campuran objek Fighter dan Mage.

**Duck typing.** `KonsolLog` dan `FileLog` nggak ada hubungan pewarisan, tapi dua-duanya punya method `catat(pesan)`. Keduanya dipanggil lewat satu fungsi yang sama, yaitu `catat_ke_semua()`.

**Operator overloading.** Ada tiga: `__str__` dan `__lt__` di Character, sama `__len__` di Arena. `__lt__` dipakai `sorted()` buat ranking damage, `__len__` buat `len(arena)`.

Aku juga ngilangin rantai `if role == "fighter"` yang dulu ada di `create_character`, diganti dictionary `Arena.daftar_role`. Jadi nggak ada pengecekan `type()` atau string role buat nentuin perilaku objek.

## Output

(screenshot dari terminal)

Bukti abstract class nggak bisa diinstansiasi:

![bukti abstraksi](screenshots/bukti_abstraksi.png)

```
=== BUKTI ABSTRAKSI ===
[OK] Character tidak bisa dibuat langsung -> TypeError: Can't instantiate abstract class Character without an implementation for abstract methods 'get_total_damage', 'skill_spesial'
```

Menu 5, battle (Drian si Fighter dan eudora si Mage nyerang Layla):

![battle](screenshots/battle.png)

```
=== SEMUA KARAKTER MENYERANG LAYLA ===
[x] Drian menyerang Layla (-25 HP). Sisa HP Layla: 175
   [LOG-KONSOL] [SKILL] Drian (Fighter) Shield Bash ke Layla (-35 HP). Sisa HP: 140
[x] eudora menyerang Layla (-45 HP). Sisa HP Layla: 95
   [LOG-KONSOL] [SKILL] eudora (Mage) Fireball ke Layla (-90 HP). Sisa HP: 5
```

Hasil skill itu juga ke-catat ke file `riwayat_arena.txt` lewat `FileLog`:

```
[SKILL] Drian (Fighter) Shield Bash ke Layla (-35 HP). Sisa HP: 140
[SKILL] eudora (Mage) Fireball ke Layla (-90 HP). Sisa HP: 5
```

Menu 6, ranking damage:

![ranking](screenshots/ranking.png)

```
=== RANKING TOTAL DAMAGE ===
1. eudora (Mage) Lv.1 | Total Dmg: 45
2. Drian (Fighter) Lv.1 | Total Dmg: 25
Jumlah karakter di arena: 2
```

## SOLIDnya:

- **DIP**: `Arena.__init__` nerima `daftar_pencatat` dari luar, nggak bikin `KonsolLog` atau `FileLog` sendiri. Jadi pencatat bisa diganti tanpa ngubah kelas Arena.
- **OCP**: mau nambah role baru (misal Assassin) tinggal bikin subclass baru dan daftarin di `Arena.daftar_role`, kode `create_character()` dan `adu_skill()` nggak perlu diubah.
- **LSP**: Fighter dan Mage sama-sama nepatin kontrak `Character`, jadi `adu_skill()` bisa makai karakter apa pun tanpa error.

## Perubahan yang ada dari versi sebelumnya

- `Character` sekarang abstract, jadi role selain Fighter dan Mage ditolak waktu bikin karakter.
- `Item.item_starter` yang versi staticmethod aku ganti namanya jadi `validasi_nama_item`, soalnya sebelumnya nimpa classmethod dengan nama yang sama.
- `Arena.ubah_instansi` yang versi staticmethod (duplikat dan salah) aku hapus.
- Level up sekarang sekalian ngisi energy sampai penuh, biar skill nggak macet.
