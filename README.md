# 🎮 GameMatch

**Temukan Laptop yang Cocok untuk Game Favoritmu**

GameMatch adalah aplikasi rekomendasi laptop berbasis web yang membantu pengguna mencari laptop terbaik sesuai kebutuhan gaming mereka.
Pengguna cukup **memilih game**, lalu sistem akan menampilkan **daftar laptop yang layak** berdasarkan spesifikasi minimum maupun rekomendasi game tersebut.

---

## ✨ Fitur Utama

### 🔍 1. Cari Game

Pengguna dapat mencari game berdasarkan nama. Sistem menyediakan informasi lengkap, seperti:

* Minimum Specs
* Recommended Specs
* CPU & GPU Requirements
* RAM & Storage Needed

### 💻 2. Input Laptop – *Dua Opsi*

#### 🧩 a. **Input Otomatis via API**

Pengguna cukup memasukkan *nama laptop*.
Sistem akan memanggil API dan mengisi spesifikasi laptop secara otomatis (CPU, GPU, RAM, Storage).

#### 🧩 b. **Input Manual**

Pengguna dapat mengisi spesifikasi laptop sendiri terutama jika:

* Laptop tidak tersedia di API
* Laptop custom / modifikasi
* Ingin memasukkan laptop lama

### ⚙️ 3. Mesin Rekomendasi

GameMatch membandingkan spesifikasi laptop dengan persyaratan game, lalu memberikan hasil:

* ✔️ **Cocok (Recommended)**
* ⚠️ **Bisa Jalan, tapi di Setting Rendah**
* ❌ **Tidak Memenuhi Minimum Spec**

### 📊 4. Simpan Database Laptop & Game

Semua data disimpan dalam database sehingga:

* Pengguna dapat melihat laptop sebelumnya
* Admin bisa menambah, mengedit, dan menghapus data

---

## 🏗️ Tech Stack

GameMatch dibangun dengan teknologi modern:

| Komponen | Teknologi                            |
| -------- | ------------------------------------ |
| Backend  | Laravel 10                           |
| Frontend | Blade / Bootstrap / AdminLTE         |
| Database | MySQL                                |
| API      | GameSpec API / Laptop API (opsional) |

---

## 📂 Struktur Proyek (Simplified)

```
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   │   └── GameController.php
│   │   │   └── LaptopController.php
│   ├── Models/
│       └── Game.php
│       └── Laptop.php
│
├── resources/
│   ├── views/
│       └── game/
│       └── laptop/
│
├── routes/
│   └── web.php
│
└── README.md
```

---

## 🚀 Cara Install & Menjalankan

1. **Clone repository**

```bash
git clone https://github.com/username/gamematch.git
```

2. **Masuk folder proyek**

```bash
cd gamematch
```

3. **Install dependency**

```bash
composer install
npm install
```

4. **Buat file environment**

```bash
cp .env.example .env
```

5. **Generate key**

```bash
php artisan key:generate
```

6. **Konfigurasi database di `.env`**

```
DB_DATABASE=gamematch
DB_USERNAME=root
DB_PASSWORD=
```

7. **Migrasi database**

```bash
php artisan migrate
```

8. **Jalankan server**

```bash
php artisan serve
```

Buka di browser:
👉 `http://127.0.0.1:8000`

---

## 📸 Preview Tampilan (Opsional)

*(Tambahkan screenshot aplikasi jika ada)*

---

## 🤝 Kontribusi

Pull Request selalu diterima!
Buat issue jika menemukan bug atau ingin request fitur baru.

---

## 📄 License

MIT License – Bebas digunakan dan dikembangkan.
