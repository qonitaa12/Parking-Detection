# 🅿️ Parking Slot Detection System Using YOLOv8

This project builds an **automated detection system** to recognize **empty** and **occupied parking slots** using camera images. It uses the **YOLOv8 object detection algorithm** and datasets labeled via **Roboflow**.

---

## 📌 Project Description

This is a web-based parking detection system powered by **YOLOv8 deep learning model**. The system can detect vehicles from:

- 🖼️ Images  
- 🎥 Videos  
- 📷 Live camera feeds (real-time)

There are two detection modes available:
- 🚗 **Car Parking Detection**
- 🛵 **Motorcycle Parking Detection**

Users can select the desired detection mode before uploading files or using the live camera.

---

## 🎯 Objectives

- Train a YOLOv8 model to detect parking slots.
- Use Roboflow-labeled datasets for both car and motorcycle parking.
- Evaluate the model’s performance in real-world scenarios.
- Prepare the model for future integration in smart parking systems.

---

## 🔑 Key Features

- ✅ Upload images to detect parking slots  
- ✅ Upload video for real-time detection  
- ✅ Live camera detection supported  
- ✅ Choose detection model: Car or Motorcycle  
- ✅ Display vehicle counts:
  - Cars: `Occupied` and `Empty`
  - Motorcycles: `Occupied` only
- ✅ Bounding box visualization of detection results  
- ✅ Modern, responsive UI design

---

## 📂 Dataset Explanation

### 🚗 Car Parking Dataset

Labeled using **Roboflow**, with two object classes:

| Label      | Description                    |
|------------|--------------------------------|
| `empty`    | Empty parking slot             |
| `occupied` | Parking slot currently occupied |

### 🛵 Motorcycle Parking Dataset

Labeled using **Roboflow**, with one object class:

| Label      | Description                    |
|------------|--------------------------------|
| `occupied` | Parking slot currently occupied |

Data was collected by capturing real-world parking area images and manually labeling each slot using bounding boxes.

---
