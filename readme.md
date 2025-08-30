# 🕵️‍♂️ Whois Lookup Automation

Sebuah tool sederhana untuk melakukan **WHOIS & RDAP Lookup** secara otomatis pada daftar domain.  
Script ini akan membaca daftar domain dari file `wordlist.txt`, melakukan **resolving domain → IP**, kemudian mengambil data ASN, provider, country, hingga informasi registrant dan abuse contact.  
Hasil akan disimpan dalam file **Excel (.xlsx)** agar mudah dianalisis lebih lanjut.

---

## ✨ Fitur
- Resolve domain → IP secara otomatis
- WHOIS & RDAP Lookup menggunakan [`ipwhois`](https://pypi.org/project/ipwhois/)
- Menampilkan informasi penting:
  - ASN, Provider, Country, ASN Date
  - Registrant Name, Address, Registration Date, Last Changed
  - Abuse Contact (Email & Phone)
- Export hasil ke **Excel** lengkap dengan timestamp
- Tampilan output lebih rapi dengan warna (menggunakan `termcolor`)

---

## 📂 Struktur Proyek
├── whois_lookup.py # main script<br>
├── wordlist.txt # daftar domain yang akan dicek<br>
├── requirements.txt # file dependency<br>
├── output/ # folder hasil export Excel<br>
└── README.md # dokumentasi<br>

---

## ⚡ Instalasi
Clone repo ini lalu masuk ke direktori project:

```bash
git clone https://github.com/username/whois-lookup.git
cd whois-lookup
pip install -r requirements.txt
```

## 🚀 Cara Menggunakan

1. Tambahkan daftar domain yang ingin dicek ke dalam file `wordlist.txt` (satu domain per baris).
   ```txt
   google.com
   yahoo.com
   example.org

2. Jalankan script
```python3 scan.py```

3. Hasil akan ditampilkan di terminal, dan otomatis tersimpan dalam file:
```output/whois_output_DD_MM_YYYY_HH_MM_SS.xlsx```

## 📊 Contoh Output Excel
| domain      | ip             | asn   | provider     | country | asn_date   | registrant_name | registrant_address             | registrant_registered | registrant_last_changed | abuse_email      | abuse_phone  |
|-------------|----------------|-------|--------------|---------|------------|-----------------|-------------------------------|-----------------------|--------------------------|------------------|--------------|
| google.com  | 142.250.190.14 | 15169 | GOOGLE LLC   | US      | 2000-03-30 | Google LLC      | 1600 Amphitheatre Parkway ... | 1997-09-15T00:00:00Z  | 2021-02-10T08:00:00Z     | abuse@google.com | +1-650-253-0000 |

---

## ⚠️ Catatan
- Gunakan tool ini hanya untuk **tujuan legal & edukasi**.
- Beberapa domain mungkin tidak menampilkan informasi registrant lengkap karena aturan privasi (misalnya GDPR).
- Untuk dataset besar, gunakan dengan bijak agar tidak diblokir oleh server RDAP/WHOIS.

---

## 👨‍💻 Author
Copyright (c) 2025 **0xbilly**

