# Praktikum PBO - Sistem Manajemen Karakter dan Pertarungan Arena MMORPG

## Tema
Tema program ini adalah **Sistem Manajemen Karakter dan Pertarungan Arena MMORPG** dengan judul game **Dworian Arena**.

Program dibuat menggunakan pendekatan Object-Oriented Programming (OOP). Versi Posttest 2 mengembangkan program sebelumnya dengan inheritance, method overriding, polymorphism, serta contoh relasi antarobjek.

---

## Deskripsi Program
Program ini mensimulasikan pengelolaan karakter di arena MMORPG sederhana. Pengguna dapat membuat karakter berdasarkan role, melihat daftar karakter, meningkatkan level, mengganti nama atau equipment, dan menghapus karakter. Karakter juga memiliki method untuk menyerang karakter lain.

Class utama yang digunakan:
- `Item` untuk menyimpan equipment dan bonus damage.
- `Character` sebagai class dasar karakter.
- `Fighter` dan `Mage` sebagai subclass dengan atribut serta perilaku khusus.
- `Arena` untuk menyimpan dan mengelola karakter.

---

## Pembaruan pada Posttest 2
Dibandingkan program sebelumnya, pembaruan yang terlihat pada kode saat ini meliputi:
- Penambahan subclass `Fighter` dan `Mage` yang mewarisi `Character`.
- Pembuatan karakter memilih class `Fighter` atau `Mage` berdasarkan role; role lain dibuat sebagai objek `Character` biasa.
- Penerapan **method overriding** pada `info()` untuk menampilkan armor atau mana sesuai role.
- `Mage` meng-override `get_total_damage()` sehingga damage mencakup bonus dari mana.
- Penambahan method `serang(target)` untuk menyerang karakter lain dan mengurangi HP target.
- Penambahan atribut khusus `armor` pada `Fighter` dan `mana` pada `Mage`.
- Equipment diberikan ke `Character` melalui parameter konstruktor sebagai contoh relasi objek.
- Atribut `damage` kini menggunakan atribut protected `_damage`, sedangkan `hp` tetap private dan diakses melalui property.

Menu utama masih menyediakan operasi CRUD karakter, level-up, penggantian nama, dan penggantian equipment. Pertarungan melalui `serang()` sudah tersedia pada class, tetapi belum dipanggil dari menu interaktif.

---

## Struktur Class

### 1. Class `Item`
Merepresentasikan equipment yang dipakai karakter.

Atribut:
- Class attribute: `total_item`
- Instance attributes: `nama`, `__bonus_damage`

Fungsi:
- Property `bonus_damage` untuk membaca dan mengubah bonus damage.
- Setter memastikan bonus damage negatif disimpan sebagai `0`.
- Method statis `item_starter(nama)` memeriksa apakah nama memiliki minimal tiga karakter setelah spasi di awal dan akhir dihapus.

### 2. Class `Character`
Class dasar yang menyimpan data dan perilaku umum karakter.

Atribut kelas:
- `total_character`
- `max_level = 15`
- `game_title = "Dworian Arena"`

Atribut instance:
- `name`, `role`, `level`, `hp`, `energy`, `damage`, dan `equipment`

Fungsi utama:
- `get_total_damage()` menghitung damage dasar ditambah bonus equipment.
- `serang(target)` mengurangi HP target berdasarkan total damage penyerang.
- `upgrade_level()` menaikkan level, HP, dan damage hingga batas `max_level`.
- `info()` menampilkan informasi dasar karakter.
- `validasi_nama(nama)` memeriksa nama minimal tiga karakter setelah whitespace di awal dan akhir dihapus.
- `reset_counter()` mengatur ulang `total_character`.

`hp` disimpan sebagai atribut private `__hp` dan diakses melalui property. Nilai HP atau damage negatif diubah menjadi `0`. Damage disimpan sebagai atribut protected `_damage`, yang juga digunakan subclass.

### 3. Class `Fighter`
Subclass `Character` untuk karakter role Fighter.

Atribut khusus:
- `armor`, dengan nilai default `10`.

Method `info()` di-override untuk menampilkan informasi umum dari `Character` dan nilai armor.

### 4. Class `Mage`
Subclass `Character` untuk karakter role Mage.

Atribut khusus:
- `mana`, dengan nilai default `50`.

Method yang di-override:
- `get_total_damage()` menambahkan bonus damage equipment dan `mana // 10` ke damage dasar.
- `info()` menampilkan informasi umum dari `Character` dan nilai mana.

### 5. Class `Arena`
Merepresentasikan arena yang mengelola daftar karakter.

Atribut:
- Class attribute: `nama_instansi = "Dworian Battle Arena"`
- Instance attributes: `nama_arena` dan `__daftar_karakter`

Fungsi utama:
- `create_character()` memvalidasi nama, membuat equipment awal, lalu membuat karakter sesuai role.
- `read_character()` menampilkan karakter terdaftar.
- `update_character()` menyediakan level-up, ganti nama, atau ganti equipment.
- `delete_character()` menghapus karakter berdasarkan indeks.
- `estimasi_durasi_match(jumlah_peta)` menghitung estimasi durasi dalam menit dengan rumus jumlah peta dikali lima.
- `ubah_instansi(cls, nama_baru)` adalah implementasi statis yang tersedia pada kode saat ini.

---

## Penerapan Konsep OOP

### Class dan Object
Program menggunakan objek `Arena` untuk mengelola objek karakter. Setiap karakter memiliki objek `Item` sebagai equipment.

### Encapsulation dan Property
Atribut `__hp`, `__bonus_damage`, dan `__daftar_karakter` bersifat private. Property digunakan untuk mengakses HP dan bonus damage dengan validasi. Daftar karakter Arena juga disediakan melalui property `daftar_karakter`.

### Inheritance
`Fighter` dan `Mage` mewarisi atribut serta method umum dari `Character`. Keduanya menggunakan `super()` untuk menjalankan konstruktor class induk.

### Polymorphism dan Method Overriding
Pemanggilan `info()` pada karakter menampilkan rincian tambahan sesuai jenis objeknya. `Mage` juga memiliki implementasi `get_total_damage()` sendiri, sedangkan `Fighter` menggunakan perhitungan damage dari `Character`.

### Relasi Antarobjek
- **Komposisi:** `Arena` membuat karakter di dalam `create_character()` dan menyimpan objeknya di daftar private Arena.
- **Agregasi:** `Character` menerima objek `Item` melalui parameter `equipment`; item dibuat sebelum diteruskan ke konstruktor karakter.
- **Asosiasi:** `serang(target)` menggunakan objek karakter lain sebagai target serangan. Penyerang dan target merupakan objek yang berdiri sendiri.

---

## Validasi dan Catatan Perilaku
- Nama karakter harus memiliki panjang minimal tiga karakter setelah spasi di awal dan akhir dihapus.
- HP dan damage negatif akan menjadi `0`; bonus damage equipment negatif juga menjadi `0`.
- Input HP, damage, nomor karakter, dan bonus equipment pada menu harus berupa angka sesuai permintaan program.
- Role yang bukan `Fighter` atau `Mage` tetap dapat dibuat sebagai karakter umum dengan nilai role yang diberikan.
- Atribut `armor` ditampilkan pada Fighter, tetapi kode saat ini belum menggunakannya untuk mengurangi damage serangan.
- Atribut penghitung `total_item` dan `total_character` tersedia, tetapi kode saat ini belum menambah nilainya saat objek dibuat.
- Method `serang()` dapat digunakan langsung pada objek karakter, tetapi belum tersedia sebagai pilihan di menu.
- Pada `Item` dan `Arena` terdapat dua method bernama sama (`item_starter` dan `ubah_instansi`). Di Python, definisi kedua menggantikan definisi pertama; karena itu method class dengan nama tersebut tidak tersedia seperti yang mungkin dimaksudkan oleh definisi awalnya.

---

## Pengujian Program (Main Code)
Saat dijalankan, program membuat dua karakter awal:
- `Drian` dengan role `Fighter`, HP `150`, dan damage dasar `25`.
- `eudora` dengan role `Mage`, HP `100`, dan damage dasar `40`.

Menu interaktif menyediakan:
1. Membuat karakter baru.
2. Menampilkan daftar karakter.
3. Memperbarui karakter (level-up, mengganti nama, atau mengganti equipment).
4. Menghapus karakter.
5. Keluar dari program.

---

## Cara Menjalankan Program
Buka terminal pada folder utama repository, lalu jalankan:

```bash
python Posttest/Posttest2/pbo_posttest2.py
```

Atau gunakan:

```bash
python3 Posttest/Posttest2/pbo_posttest2.py
```

## File Utama
- `pbo_posttest2.py` - program utama Posttest 2.
- `README.md` - dokumentasi program Posttest 2.

---

## Kesimpulan
Program Posttest 2 mempertahankan fitur pengelolaan karakter dari versi sebelumnya dan menambahkan pewarisan class, overriding, perilaku polymorphism, interaksi serangan, serta contoh relasi antarobjek. Struktur tersebut memperluas simulasi Dworian Arena sekaligus menunjukkan penerapan konsep OOP pada Python.
