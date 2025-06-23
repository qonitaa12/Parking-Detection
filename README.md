# 🅿️ Parking Slot Detection System Using YOLOv8

A smart web-based system that detects **empty** and **occupied** parking slots for both **cars** and **motorcycles**, using **YOLOv8 object detection models**. The system allows users to upload images, videos, or use a live camera to analyze parking areas in real time.

---

## 🧱 Background

Urban areas with high traffic often face challenges in managing limited parking spaces. Drivers struggle to find available parking slots, which increases fuel consumption, congestion, and time wastage. To address this issue, this project introduces an automated parking slot detection system using computer vision. By analyzing static images, videos, or live camera feeds, the system provides instant information about parking slot availability to support parking efficiency and planning.

---

## 🎯 Objectives

- ✅ Build a dual-mode detection system for car and motorcycle parking areas.
- ✅ Enable slot status detection from various input sources: images, videos, and live cameras.
- ✅ Provide real-time feedback to users through a clean, accessible web interface.
- ✅ Analyze parking density automatically with high detection accuracy.

---

## 📂 Dataset Information

### 🚗 Car Parking Dataset
- **Owner**: Qonita Milla Hanifa  
- **Source**: [Roboflow Universe](https://universe.roboflow.com/deteksiparkir/parking-detection-39fgv/dataset/3)  
- **Classes**: `empty`, `occupied`  
- **Images**: 654 (train/valid/test)  
- **Boxes**: 13,915 labeled bounding boxes  
- **Format**: YOLOv8-compatible

### 🛵 Motorcycle Parking Dataset
- **Owner**: Qonita Milla Hanifa  
- **Source**: [Roboflow Universe](https://universe.roboflow.com/skripsi-lcybh/kepadatan-parkir-motor)  
- **Classes**: `occupied`  
- **Images**: ~510+  
- **Format**: YOLOv8-compatible

---

## ⚙️ Implementation Process

1. **Dataset Preparation** – Images collected and labeled using Roboflow.
2. **Model Training** – YOLOv8 trained separately for car and motorcycle datasets.
3. **Web Development** – Flask used to create upload, detection, and streaming endpoints.
4. **Model Integration** – System switches model based on selected mode (mobil/motor).
5. **Visualization** – Outputs rendered with bounding boxes and slot count.

---

## 🚀 How to Use the System (Web-Based)

### 📦 1. Install Requirements
```bash
pip install flask ultralytics opencv-python roboflow numpy
```

### 🛠️ 2. Place YOLOv8 Weights
```
weights/best.pt           # Car detection model
weights/best_motor.pt     # Motorcycle detection model
```

### 🖥️ 3. Run the Application
```bash
python app.py
```
Then open:  
🔗 `http://localhost:5000/`

### 🧪 4. Choose Detection Mode
- Upload Image (JPG/PNG) → Detect status in static image.
- Upload Video (MP4/AVI) → Analyze each frame.
- Activate Camera → Run real-time detection via webcam.

> ✅ Best suited for parking administrators, system testers, or research in parking management.

---

## 🧩 Detection Modes

| Mode        | Purpose                     | Classes Detected         | Model File           |
|-------------|------------------------------|---------------------------|----------------------|
| Car         | Parking lot for cars         | `empty`, `occupied`       | `best.pt`            |
| Motorcycle  | Motorbike parking areas      | `occupied` only           | `best_motor.pt`      |

> The system automatically selects the appropriate model based on user mode: `mobil` or `motor`.

---

## 📊 Model Accuracy

### 🚗 Car Detection Model
- **Precision**: 97.76%
- **Recall**: 94.70%
- **mAP@0.5**: 97.57%
- **mAP@0.5:0.95**: 91.98%
- **Fitness**: 92.54%

### 🛵 Motorcycle Detection Model
- **Precision**: 97.04%
- **Recall**: 91.43%
- **mAP@0.5**: 97.83%
- **mAP@0.5:0.95**: 72.12%
- **Fitness**: 74.69%

---

## 🌟 Features & Goals

- 🖼️ Image upload with annotated detection
- 🎥 Video frame-by-frame detection
- 📷 Real-time webcam slot recognition
- 🔁 Car/Motor model switch
- 🧮 Live slot counter (empty & occupied)
- 🧘 Responsive UI for mobile and desktop

---

## 🧠 System Overview

```plaintext
[User Uploads Image/Video or Starts Camera]
        ↓
[System Loads YOLOv8 Model (Car or Motorcycle)]
        ↓
[Detection Results with Annotated Boxes]
        ↓
[Slot Count Output (empty / occupied)]
        ↓
[Rendered to Web Interface]
```

---

## 🖼️ UI Preview

> Sample layout (add screenshots if needed):

![image](https://github.com/user-attachments/assets/643da7ce-9e2d-480a-b35e-bf3b9b94d2f2)


---

## 👩‍💻 Developed By

**Qonita Milla Hanifa**  
Final Year Project – 2025  
Smart Parking Analysis using YOLOv8 & Flask

---

## 📌 Suggestions for Future Work

- Add database integration for logging
- Enable multi-camera support
- Extend to multi-floor or large-scale facilities
- Embed with edge devices like Raspberry Pi

---
