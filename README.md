# 🅿️ Parking Spot Detector with YOLOv5

Proyek ini membangun sistem deteksi otomatis untuk mengenali **slot parkir kosong** dan **slot parkir terisi** dari citra kamera menggunakan algoritma deteksi objek YOLOv5 dan dataset yang telah dilabeli melalui Roboflow.

---

## 📌 Deskripsi Proyek

Dengan meningkatnya mobilitas dan kepadatan kendaraan, pengelolaan area parkir menjadi salah satu tantangan utama. Sistem ini dirancang untuk:

- Mendeteksi kondisi slot parkir (empty / occupied).
- Memanfaatkan citra statis (gambar) sebagai sumber input.
- Melatih model deteksi objek dengan performa tinggi menggunakan YOLOv5.
- Memberikan hasil evaluasi akurasi model untuk pengembangan lebih lanjut.

---

## 🎯 Tujuan

- Membangun model YOLOv5 untuk mengenali slot parkir.
- Melatih model berdasarkan dataset berlabel dari Roboflow.
- Mengevaluasi performa model dalam mengenali area parkir.
- Mempersiapkan model untuk integrasi sistem otomatis di masa depan.

---

## 📂 Penjelasan Dataset

Dataset dibuat melalui proses labeling menggunakan **Roboflow**, yang terdiri dari dua label utama:

| Label        | Deskripsi                    |
|--------------|------------------------------|
| `empty`      | Slot parkir kosong           |
| `occupied`   | Slot parkir yang sedang dipakai |

### 🔢 Jumlah Dataset

| Tipe Data | Jumlah Gambar | Jumlah Label |
|-----------|----------------|---------------|
| Train     | 476            | 10.120        |
| Validasi  | 119            | 2.536         |
| Test      | 59             | 1.259         |
| **Total** | 654            | 13.915        |

Sumber data berasal dari pengambilan gambar area parkir secara manual yang kemudian dilabeli secara visual menggunakan bounding box untuk tiap slot parkir.

---

## 🧰 Teknologi & Tools

| Teknologi     | Keterangan                                       |
|---------------|--------------------------------------------------|
| Python        | Bahasa pemrograman utama                         |
| YOLOv5        | Model deteksi objek ringan dan akurat            |
| Roboflow      | Tool labeling data dan manajemen dataset         |
| PyTorch       | Framework deep learning                          |
| Google Colab  | Lingkungan pelatihan model (training pipeline)   |
| OpenCV        | Prosesing gambar                                 |

## 📅 Progress Proyek

Berikut adalah perkembangan proyek yang telah dilakukan hingga saat ini:

| Fase | Deskripsi                                   | Status      | Persentase |
|-------|---------------------------------------------|-------------|------------|
| 1     | Pengumpulan dan Pra-Pemrosesan Dataset Parkir | ✅ Selesai  | 100%       |
|       | - Upload data ke Roboflow                     |             |            |
|       | - Labeling (empty dan occupied)               |             |            |
| 2     | Setup Environment dan Download Dataset Format YOLOv5 | ✅ Selesai  | 100%       |
|       | - Clone repo YOLOv5                           |             |            |
|       | - Install dependencies                        |             |            |
|       | - Download dataset via Roboflow SDK           |             |            |
| 3     | Training Model YOLOv5 dengan Dataset          | ✅ Selesai  | 100%       |
|       | - Training selama 30 epoch                    |             |            |
|       | - Menggunakan weights awal yolov5s.pt          |             |            |
| 4     | Evaluasi Model dan Validasi                   | ✅ Selesai  | 100%       |
|       | - Validasi hasil training (precision, recall, mAP) |          |            |
| 5     | Deteksi Slot Parkir pada Test Set / Gambar    | ⏳ Dalam Proses | 0%         |
|       | - Menggunakan model hasil training (best.pt)  |             |            |

