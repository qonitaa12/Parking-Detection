# 🅿️ Sistem Deteksi Slot Parkir Menggunakan YOLOv8

Proyek ini membangun sistem deteksi otomatis untuk mengenali **slot parkir kosong** dan **slot parkir terisi** dari citra kamera menggunakan algoritma deteksi objek YOLOv8 dan dataset yang telah dilabeli melalui Roboflow.

---

## 📌 Deskripsi Proyek

Aplikasi ini adalah sistem deteksi parkir berbasis web yang memanfaatkan model deep learning **YOLOv8**. Sistem mampu mendeteksi kendaraan baik dari **gambar**, **video**, maupun **live kamera** secara real-time.

Tersedia dua jenis deteksi:
- **Deteksi Parkir Mobil**
- **Deteksi Parkir Motor**

Pengguna dapat memilih jenis deteksi yang diinginkan sebelum mengunggah gambar/video atau mengaktifkan kamera.

---

## 🎯 Tujuan

- Membangun model YOLOv8 untuk mengenali slot parkir.
- Melatih model berdasarkan dataset berlabel dari Roboflow.
- Mengevaluasi performa model dalam mengenali area parkir.
- Mempersiapkan model untuk integrasi sistem otomatis di masa depan.

---
## 🎯 Fitur Utama

✅ Upload gambar untuk mendeteksi slot parkir  
✅ Upload video dan deteksi parkir secara streaming  
✅ Deteksi langsung via live kamera  
✅ Pilih model deteksi: **mobil** atau **motor**  
✅ Tampilkan jumlah kendaraan:
- Mobil: `Occupied` dan `Empty`
- Motor: hanya `Occupied` (motor yang terdeteksi)

✅ Visualisasi bounding box hasil deteksi  
✅ Antarmuka modern dan responsif

## 📂 Penjelasan Dataset

**Dataset Mobil**
Dataset dibuat melalui proses labeling menggunakan **Roboflow**, yang terdiri dari dua label utama:

| Label        | Deskripsi                    |
|--------------|------------------------------|
| `empty`      | Slot parkir kosong           |
| `occupied`   | Slot parkir yang sedang dipakai |

**Dataset Motor**
Dataset dibuat melalui proses labeling menggunakan **Roboflow**, yang terdiri dari satu label utama:

| Label        | Deskripsi                    |
|--------------|------------------------------|
| `occupied`   | Slot parkir yang sedang dipakai |


Sumber data berasal dari pengambilan gambar area parkir secara manual yang kemudian dilabeli secara visual menggunakan bounding box untuk tiap slot parkir.

---


