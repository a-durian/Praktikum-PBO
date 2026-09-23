# Praktikum PBO - Sistem Manajemen Karakter dan Pertarungan Arena MMORPG

## Tema
Tema yang digunakan dalam program ini adalah **Sistem Manajemen Karakter dan Pertarungan Arena MMORPG** dengan judul game utama **Dworian Arena**.

Program ini dibuat dengan pendekatan Object-Oriented Programming (OOP) dan mengimplementasikan materi dari tiga modul yang telah dipelajari:
- Class & Object (Modul 1)
- Atribut & Method (Modul 2)
- Encapsulation & Property (Modul 3)

---

## Deskripsi Program
Program ini mengangkat konsep arena game MMORPG sederhana di mana pengguna dapat membuat karakter, menampilkan daftar karakter, melakukan update seperti level-up dan penggantian equipment, serta menghapus karakter dari arena. Sistem ini mencakup beberapa entitas utama, yaitu:
- Item
- Character
- Arena

Tujuan program ini adalah untuk memodelkan dunia game dalam bentuk objek nyata agar proses pengembangan lebih terstruktur, mudah dipelihara, dan sesuai dengan prinsip OOP.

---

## Kesesuaian Tugas
Berikut adalah ringkasan yang sesuai dengan instruksi tugas:
- Tema tetap menggunakan **Dworian Arena** seperti yang telah disepakati.
- Program memiliki **3 class utama**: `Item`, `Character`, dan `Arena`.
- Terdapat atribut kelas dan atribut instance yang digunakan bersama maupun unik per objek.
- Terdapat atribut **Public** dan atribut **Private** (`__bonus_damage`, `__hp`, `__damage`, `__daftar_karakter`).
- Terdapat method **instance**, **class method**, dan **static method**.
- Akses ke data private menggunakan `@property` dan setter dengan validasi data.
- Terdapat demo program untuk dua objek per class dan pengujian input valid serta tidak valid.

---

## Struktur Class

### 1. Class Item
Class `Item` merepresentasikan equipment atau item yang bisa digunakan oleh karakter.

Atribut yang dimiliki:
- Atribut kelas:
  - `total_item` (counter item umum)
- Atribut instance:
  - `nama`
  - `__bonus_damage`

Fungsi utama:
- Menyimpan data item yang digunakan karakter.
- Menentukan bonus damage dari equipment.
- Menyediakan pembuatan item default melalui class method.

### 2. Class Character
Class `Character` merepresentasikan pemain yang berpartisipasi dalam arena.

Atribut yang dimiliki:
- Atribut kelas:
  - `total_character`
  - `max_level`
  - `game_title = "Dworian Arena"`
- Atribut instance:
  - `name`
  - `role`
  - `level`
  - `hp`
  - `energy`
  - `damage`
  - `equipment`

Fungsi utama:
- Membuat karakter baru
- Menaikkan level karakter
- Menampilkan informasi karakter
- Menghitung total damage karakter dengan tambahan equipment

### 3. Class Arena
Class `Arena` merepresentasikan arena tempat karakter ditempatkan dan dikelola.

Atribut yang dimiliki:
- Atribut kelas:
  - `nama_instansi = "Dworian Battle Arena"`
- Atribut instance:
  - `nama_arena`
  - `__daftar_karakter`

Fungsi utama:
- Menambah karakter baru
- Menampilkan daftar karakter
- Memperbarui data karakter
- Menghapus karakter
- Mengelola konfigurasi umum arena

---

## Penerapan OOP

### Class & Object
Program ini menggunakan 3 class utama yang berdiri sendiri namun saling berinteraksi.

Contoh:
- Satu objek `Character` dibuat untuk karakter seperti `Drian` dan `Eudora`.
- Masing-masing karakter memiliki `equipment` berupa objek `Item`.
- Objek `Arena` mengelola beberapa objek `Character` di dalam daftar `__daftar_karakter`.

### Atribut & Method
Program ini menerapkan atribut dan method pada tiap class.

Contoh atribut:
- `name`, `role`, `hp`, `damage` untuk `Character`
- `nama`, `bonus_damage` untuk `Item`
- `nama_arena` dan `__daftar_karakter` untuk `Arena`

Contoh method:
- Instance method: `upgrade_level()`, `info()`, `get_total_damage()`, `create_character()`, `read_character()`, `update_character()`, `delete_character()`
- Class method: `item_starter()`, `reset_counter()`, `ubah_instansi()`
- Static method: `validasi_nama()`, `estimasi_durasi_match()`

### Encapsulation & Property
Program ini juga menerapkan encapsulation dengan atribut private.

Contoh atribut private:
- `__bonus_damage`
- `__hp`
- `__damage`
- `__daftar_karakter`

Akses ke atribut private dilakukan menggunakan property getter dan setter, misalnya:
- `@property` untuk mengambil nilai
- `@nama_property.setter` untuk mengubah nilai

Contoh validasi yang diterapkan:
- Nilai `hp` dan `damage` tidak boleh bernilai negatif.
- Nilai `bonus_damage` jika negatif akan otomatis diubah ke 0.
- Nama karakter harus memiliki panjang minimal 3 karakter.

---

## Getter, Setter, dan Validasi Data
Salah satu prinsip penting dalam modul 3 adalah penggunaan decorator `@property` serta setter untuk menjaga agar data tetap valid.

Contoh validasi dalam program:
- `hp` tidak boleh kurang dari 0
- `damage` tidak boleh kurang dari 0
- `bonus_damage` tidak boleh kurang dari 0
- nama karakter harus minimal 3 huruf

Jika input tidak valid:
- sistem akan menolak perubahan data,
- menampilkan peringatan,
- atau mengembalikan nilai default sesuai logika yang ditentukan.

---

## Contoh Method yang Digunakan

### Instance Method
- `upgrade_level()`
- `info()`
- `get_total_damage()`
- `create_character()`
- `read_character()`
- `update_character()`
- `delete_character()`

### Class Method
- `item_starter()`
- `reset_counter()`
- `ubah_instansi()`

### Static Method
- `validasi_nama()`
- `estimasi_durasi_match()`

---

## Pengujian Program (Main Code)
Pada bagian bawah program terdapat menu utama yang menjalankan simulasi nyata sistem. Fungsinya adalah:
1. Membuat minimal 2 objek karakter, misalnya `Drian` dan `Eudora`
2. Menampilkan daftar karakter
3. Melakukan update level, ganti nama, dan ganti equipment
4. Menghapus karakter
5. Menjalankan validasi apabila input tidak sesuai

Contoh pengujian valid/invalid:
- Valid: `hp = 150`, `damage = 25`, `nama = "Drian"`
- Tidak valid: `damage = -10`, `nama = "ab"`, `hp = -5`

Semua pengujian tersebut dilakukan untuk membuktikan bahwa setter dan validasi data berhasil bekerja dengan benar.

---

## Cara Menjalankan Program
Buka terminal lalu jalankan perintah berikut:

```bash
python Posttest/Posttest1/pbo_posttest1.py
```

Atau jika menggunakan Python 3:

```bash
python3 Posttest/Posttest1/pbo_posttest1.py
```

---

## File Utama
- `Posttest/Posttest1/pbo_posttest1.py` - file program utama
- `README.md` - dokumentasi dan penjelasan program

---

## Kesimpulan
Program ini berhasil mengimplementasikan prinsip OOP dengan jelas, terutama:
- penggunaan class dan object,
- penggunaan atribut kelas dan instance,
- penerapan method instance, class method, dan static method,
- serta encapsulation dan property untuk menjaga validitas data.

Dengan demikian, program ini sesuai dengan kebutuhan tugas praktikum PBO dan dapat digunakan sebagai referensi dalam pembuatan proyek OOP yang lebih kompleks.
