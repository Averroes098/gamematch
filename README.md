# 🎮 GameMatch

**Temukan laptop terbaik untuk memainkan game favoritmu!**  
GameMatch adalah aplikasi rekomendasi laptop berbasis web yang membantu pengguna mencari laptop yang cocok berdasarkan spesifikasi minimum maupun rekomendasi dari game yang dipilih.

---

## ✨ Fitur Utama

- **Database Laptop**  
  Menggunakan file `laptop.csv` yang dibaca dengan **Pandas**.

- **Input Manual**  
  Pengguna dapat memasukkan spesifikasi CPU, GPU, RAM, dan Storage secara manual.

- **Integrasi Steam API**  
  Mendapatkan data game serta requirement (Minimum & Recommended).

- **Mesin Analisis Kompatibilitas**  
  Sistem membandingkan spesifikasi laptop dengan kebutuhan game.

---

## 🏗️ Tech Stack

| Komponen | Teknologi |
|---------|-----------|
| Backend | **Python (Flask)** |
| Frontend | HTML, Jinja2, **Bootstrap 5** |
| Data | **Pandas** |
| API Client | **Requests** |
| Server | **Gunicorn** |

---

## 📂 Struktur Proyek

```

├── app.py                  # Aplikasi utama Flask
├── data/
│   └── laptop.csv          # Database laptop
├── modules/
│   ├── compatibility.py    # Analisis kompatibilitas
│   ├── laptop_reader.py    # Pembaca file CSV laptop
│   ├── recommendations.py  # Logika rekomendasi
│   └── steam_api.py        # Interaksi dengan Steam API
├── templates/
│   ├── base.html
│   ├── compare.html
│   ├── dashboard.html
│   ├── input_laptop.html
│   └── steam_search.html
├── Procfile                # Konfigurasi deploy Gunicorn
├── requirements.txt        # Dependensi Python
└── README.md               # Dokumentasi proyek

```

---

## 🔄 GameMatch System Workflow

```

┌────────────────────┐
│     User / Client  │
└─────────┬──────────┘
│ HTTP Request
▼
┌────────────────────┐
│   GameMatch API    │
│ (Flask + Gunicorn) │
└─────────┬──────────┘
│
├──► Local CSV / JSON Database
│
├──► External API (Steam API)
│
▼
┌───────────────────────┐
│     Response Builder   │
└─────────┬─────────────┘
│ JSON Response
▼
┌───────────────────────┐
│    Frontend Render     │
└────────────────────────┘

````

---

## 🚀 Cara Install & Menjalankan (Lokal)

Ikuti langkah berikut untuk menjalankan proyek di komputer Anda.

### 1. Prasyarat
Pastikan Python sudah terinstal:  
https://www.python.org/downloads/

---

### 2. Instalasi

#### a. Clone Repository
```bash
git clone https://github.com/Averroes098/gamematch.git
````

#### b. Masuk ke Folder Proyek

```bash
cd gamematch
```

#### c. Buat Virtual Environment

```bash
python -m venv venv
```

#### d. Aktifkan Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Mac/Linux:

```bash
source venv/bin/activate
```

#### e. Install Dependensi

```bash
pip install -r requirements.txt
```

#### f. Jalankan Aplikasi

```bash
python app.py
```

---

## 🌐 Buka di Browser

Aplikasi biasanya berjalan di:

👉 **[http://127.0.0.1:5000](http://127.0.0.1:5000)**

---

## 📸 Preview

<img width="1094" height="850" alt="Screenshot" src="https://github.com/user-attachments/assets/e41bd61f-8054-4bf6-bef7-3bf20bcaed03" />

---

## 🤝 Kontribusi

Pull Request diterima **kalau lagi gabut** 😄
Silakan fork dan ajukan perubahan.

<img src="https://github.com/user-attachments/assets/eb63af8f-7207-404d-85fa-3ed471ff9e1b" width="300">

---

## 🔗 Link Website

[https://gamematch.up.railway.app/](https://gamematch.up.railway.app/)

---

## 📄 License

MIT License — bebas digunakan dan dikembangkan.
