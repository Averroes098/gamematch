# 🎮 GameMatch

**Temukan Laptop yang Cocok untuk Game Favoritmu**

GameMatch adalah aplikasi rekomendasi laptop berbasis web yang membantu pengguna mencari laptop terbaik sesuai kebutuhan gaming mereka.
Pengguna cukup **memilih game**, lalu sistem akan menampilkan **daftar laptop yang layak** berdasarkan spesifikasi minimum maupun rekomendasi game tersebut.

---

## ✨ Fitur Utama

* **Database Laptop:** Memuat spesifikasi laptop dari file `laptop.csv` menggunakan Pandas.
* **Input Manual:** Pengguna dapat memasukkan spesifikasi CPU, GPU, RAM, dan Storage secara manual.
* **Integrasi Steam API:** Mencari game berdasarkan nama dan mengambil detail persyaratan (Minimum & Recommended).
* **Mesin Analisis:** Menganalisis kompatibilitas (saat ini berdasarkan RAM) dan memberikan status hasil.

---

## 🏗️ Tech Stack

| Komponen | Teknologi |
| --- | --- |
| Backend | **Python (Flask)** |
| Frontend | HTML, Jinja2, **Bootstrap 5** |
| Data | **Pandas** (untuk membaca `.csv`) |
| API Client | **Requests** (untuk Steam API) |
| Server | **Gunicorn** (untuk deployment) |

---

## 📂 Struktur Proyek

```
├── app.py                  # Aplikasi utama Flask
├── data/
│   └── laptop.csv          # Database spesifikasi laptop
├── modules/
│   ├── compatibility.py    # Logika analisis kompatibilitas
│   ├── laptop_reader.py    # Pembaca file CSV laptop
│   ├── recommendations.py  # Logika rekomendasi game
│   └── steam_api.py        # Modul untuk interaksi Steam API
├── templates/
│   ├── base.html           # Template dasar (navbar, footer)
│   ├── compare.html        # Halaman hasil perbandingan
│   ├── dashboard.html      # Halaman utama
│   ├── input_laptop.html   # Form input spesifikasi laptop
│   └── steam_search.html   # Halaman pencarian game
├── Procfile                # Konfigurasi deploy (Gunicorn)
├── requirements.txt        # Daftar dependensi Python
└── README.md               # File yang sedang Anda baca
```

## 🔄 GameMatch System Workflow

```
┌────────────────────┐
│     User / Client  │
│  (Browser/Frontend) │
└─────────┬──────────┘
          │  HTTP Request (Search Game/Laptop)
          ▼
┌────────────────────┐
│   GameMatch API    │
│ (Flask + Gunicorn) │
└─────────┬──────────┘
          │
          ├────────────► Local JSON Database
          │                ├ games.json
          │                └ laptops.json
          │       (Filter, Matching Spec, Ranking)
          │
          ├────────────► External APIs (optional)
          │                ├ Steam API (Game data)
          │                └ TechSpecs API (Laptop data)
          │
          ▼
┌────────────────────┐
│  Response Builder  │
│ (JSON Output API   │
│  Recommended List) │
└─────────┬──────────┘
          │  HTTP Response (JSON)
          ▼
┌────────────────────┐
│   Frontend Render  │
│ (HTML/JS/React/etc)│
└────────────────────┘
```


---

## 🚀 Cara Install & Menjalankan (Lokal)

Berikut adalah panduan langkah demi langkah untuk menjalankan proyek ini di komputer Anda.

### 1. Prasyarat

Pastikan Anda sudah menginstal **Python** di komputer Anda. Anda bisa mengunduhnya dari [python.org](https://www.python.org/downloads/).

### 2. Langkah-langkah Instalasi

Buka **Terminal** (atau Command Prompt di Windows) dan ikuti perintah ini satu per satu.

**a. Clone Repository**
Unduh semua file kode dari GitHub ke komputer Anda.
```bash
git clone [https://github.com/Averroes098/gamematch.git](https://github.com/Averroes098/gamematch.git)


**b. Masuk ke Folder Proyek Pindah ke direktori (folder) yang baru saja Anda unduh.**

'''Bash
**cd gamematch**
c. Buat Virtual Environment Ini adalah praktik terbaik untuk mengisolasi dependensi proyek.

Bash

python -m venv venv
d. Aktifkan Virtual Environment Anda harus melakukan ini setiap kali ingin menjalankan proyek.

Di Windows (CMD):

Bash

venv\Scripts\activate
Di Mac/Linux:

Bash

source venv/bin/activate
(Anda akan melihat (venv) di awal baris terminal Anda jika berhasil).

e. Install Semua Dependensi Perintah ini akan membaca file requirements.txt dan menginstal semua library yang dibutuhkan.

Bash

pip install -r requirements.txt
f. Jalankan Aplikasi

Bash


python app.py


### 3. Buka di Browser

Buka browser Anda (seperti Chrome) dan pergi ke alamat yang muncul di terminal. Biasanya alamatnya adalah:

👉 https://www.google.com/search?q=http://127.0.0.1:8080 (atau http://127.0.0.1:5000)


---


```bash
git clone [https://github.com/Averroes098/gamematch.git](https://github.com/Averroes098/gamematch.git)


## 📸 Preview Tampilan (Opsional)

<img width="1094" height="850" alt="Screenshot 2025-11-16 174148" src="https://github.com/user-attachments/assets/e41bd61f-8054-4bf6-bef7-3bf20bcaed03" />

---

## 🤝 Kontribusi

Pull Request selalu diterima jika saya lagi gabut aja.


![Handshake GIF](https://github.com/user-attachments/assets/eb63af8f-7207-404d-85fa-3ed471ff9e1b)

---

## Link Website
https://gamematch.up.railway.app/

---

## 📄 License
MIT License – Bebas digunakan dan dikembangkan.
