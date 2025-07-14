# 🤖 Robotic Vision Detector

A real-time object detection and basic distance estimation system using Python, OpenCV, and MobileNet SSD.  
This project simulates a simple robotic vision system that can detect and track objects in a live video stream and estimate their approximate distance from the camera.

---

## 🚀 Features

- 🔍 Real-time object detection using a pretrained MobileNet SSD model
- 📏 Approximate distance estimation using bounding box width
- 📦 Modular design with reusable utilities
- 🧠 Ideal for robotics, AI infrastructure, or simulation use cases

---

## 🛠️ Tech Stack

- Python
- OpenCV
- NumPy
- MobileNet SSD (Caffe-based model)

---

## 📂 Project Structure

```

robotic-vision-detector/
├── detector.py                # Main app script
├── utils.py                   # Helper functions for drawing and distance logic
├── requirements.txt           # Dependencies
├── README.md                  # This file
├── models/                    # Pretrained MobileNetSSD model files
│   ├── MobileNetSSD\_deploy.prototxt
│   └── MobileNetSSD\_deploy.caffemodel
├── assets/                    # (Optional) Output or reference media
│   └── sample\_output.png      # Not included due to privacy

````

---

## 💻 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/robotic-vision-detector.git
cd robotic-vision-detector
````

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Download model files

Ensure the following files are present in the `models/` directory:

* `MobileNetSSD_deploy.prototxt`
* `MobileNetSSD_deploy.caffemodel`

You can get them from the official repo:
🔗 [https://github.com/chuanqi305/MobileNet-SSD](https://github.com/chuanqi305/MobileNet-SSD)

### 4. Run the detector

```bash
python detector.py
```

Press `q` to quit the webcam window.

---

## ⚙️ How It Works

* The webcam feed is processed in real-time
* A blob is created from each frame and passed to the MobileNet SSD
* Detections above 50% confidence are displayed with bounding boxes
* The width of the bounding box is used to estimate distance (basic method)

---

## 🔒 Note on Privacy

This project does not include screenshots of real-time output due to personal and environmental privacy considerations.

---

## 📈 Future Improvements

* Integrate YOLOv5 or EfficientDet for better accuracy and speed
* Build a web-based UI using Streamlit or Gradio
* Add support for object tracking and voice alerts
* Calibrate distance estimation with real-world object sizes and camera specs

---

## 🧠 What This Project Demonstrates

This project reflects an understanding of:

* Computer Vision fundamentals
* Real-time processing constraints
* DL-based inference in practical robotics use cases
* Clean code modularization and deployment

---

## 📫 Contact

[Kiran Bhowmick](https://www.linkedin.com/in/kiran-bhowmick-67a877281)

```

