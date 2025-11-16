import json
import os
import pandas as pd

def load_laptops(base_dir=None):
    if base_dir is None:
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    
    laptops_path = os.path.join(base_dir, "data", "laptop.csv") 
    
    print(f"Mencoba memuat data dari: {laptops_path}") 

    try:
        df = pd.read_csv(laptops_path, encoding='utf-8')
    except FileNotFoundError:
        print(f"===========================================================")
        print(f"ERROR: FILE TIDAK DITEMUKAN!")
        print(f"Pastikan file 'laptop.csv' ada di dalam folder 'data'")
        print(f"===========================================================")
        return []
    except Exception as e:
        print(f"ERROR: Gagal membaca laptop.csv: {e}")
        return []

    # --- PENYESUAIAN KOLOM ---
    # Kita akan memetakan kolom dasar dan membuat kolom 'storage' secara manual
    
    # Kolom yang kita butuhkan dari CSV asli
    required_kaggle_cols = [
        'model_name', 
        'processor_name', 
        'graphics', 
        'ram(GB)', 
        'ssd(GB)',       # Kolom storage 1
        'Hard Disk(GB)'  # Kolom storage 2
    ]
    
    # Cek apakah semua kolom yang kita butuhkan ada
    if not all(col in df.columns for col in required_kaggle_cols):
        print(f"===========================================================")
        print("ERROR: Kolom di laptop.csv tidak sesuai.")
        print(f"Kolom yang dibutuhkan (cek di CSV): {required_kaggle_cols}")
        print(f"Kolom yang ditemukan: {list(df.columns)}")
        print("===========================================================")
        return []

    # --- PEMBERSIHAN DATA & KOMBINASI STORAGE ---

    # 1. Bersihkan RAM (ubah jadi angka, hapus teks, isi 0 jika kosong)
    try:
        df['ram'] = df['ram(GB)'].astype(str).str.replace(r'[^0-9]', '', regex=True).fillna(0).astype(int)
    except Exception as e:
        print(f"ERROR: Gagal konversi RAM: {e}")
        return []

    # 2. Bersihkan SSD (ubah jadi angka, isi 0 jika kosong)
    try:
        df['ssd_clean'] = df['ssd(GB)'].astype(str).str.replace(r'[^0-9]', '', regex=True).fillna(0).astype(int)
    except Exception as e:
        print(f"Warning: Gagal konversi ssd(GB): {e}")
        df['ssd_clean'] = 0

    # 3. Bersihkan HDD (ubah jadi angka, isi 0 jika kosong)
    try:
        df['hdd_clean'] = df['Hard Disk(GB)'].astype(str).str.replace(r'[^0-9]', '', regex=True).fillna(0).astype(int)
    except Exception as e:
        print(f"Warning: Gagal konversi Hard Disk(GB): {e}")
        df['hdd_clean'] = 0

    # 4. BUAT KOLOM 'STORAGE' BARU dengan menjumlahkan SSD + HDD
    df['storage'] = df['ssd_clean'] + df['hdd_clean']

    # --- BUAT FINAL DATAFRAME ---
    
    # Sekarang, pilih kolom yang sudah bersih dan ganti namanya
    # agar sesuai dengan yang dibutuhkan aplikasi
    
    df_laptops = df[
        ['model_name', 'processor_name', 'graphics', 'ram', 'storage']
    ].rename(columns={
        'model_name': 'name',
        'processor_name': 'cpu',
        'graphics': 'gpu',
        # 'ram' dan 'storage' sudah benar nama kolomnya
    })

    print("Sukses memuat dan memproses laptop.csv (Storage SSD+HDD digabung)")
    
    # Ubah DataFrame menjadi list of dictionaries
    return df_laptops.to_dict('records')


def find_laptop(name, laptops):
    """
    Fungsi ini tidak perlu diubah.
    """
    name = name.lower()
    return next((l for l in laptops if l["name"].lower() == name), None)