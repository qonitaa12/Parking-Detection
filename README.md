🅿️ Parking Slot Detection System Using YOLOv8
This project develops an automated detection system to recognize empty and occupied parking slots from camera images using the YOLOv8 object detection algorithm and a dataset labeled via Roboflow.

📌 Project Description
This application is a web-based parking detection system powered by the deep learning model YOLOv8. The system can detect vehicles from images, videos, and live camera feeds in real time.

There are two types of detection:

Car Parking Detection

Motorcycle Parking Detection

Users can select the desired detection type before uploading an image/video or activating the live camera.

🎯 Objectives
Build a YOLOv8 model to recognize parking slots.

Train the model using a labeled dataset from Roboflow.

Evaluate the model's performance in recognizing parking areas.

Prepare the model for integration into automated systems in the future.

🎯 Key Features
✅ Upload images to detect parking slots
✅ Upload videos for real-time streaming detection
✅ Live camera detection
✅ Choose detection model: Car or Motorcycle
✅ Display vehicle count:

Car: Occupied and Empty

Motorcycle: Occupied only (detected motorcycles)

✅ Visualize detection results with bounding boxes
✅ Modern and responsive user interface

📂 Dataset Description
Car Dataset
The dataset was created by labeling images using Roboflow, consisting of two main labels:

Label	Description
empty	Empty parking slot
occupied	Parking slot currently in use

Motorcycle Dataset
This dataset was also labeled via Roboflow, with one main label:

Label	Description
occupied	Parking slot currently in use

The data was collected manually by capturing images of parking areas and visually labeling each slot using bounding boxes.
