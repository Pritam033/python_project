# 🎯 Real-Time Face Recognition System

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-4.x-green.svg)](https://opencv.org/)
[![face_recognition](https://img.shields.io/badge/face--recognition-%F0%9F%94%8D-brightgreen)](https://github.com/ageitgey/face_recognition)

A real-time face recognition system built using **Python**, **OpenCV**, and the **`face_recognition`** library. It identifies people through webcam video by matching faces with a pre-trained database.

---

## 🔍 Key Features

✅ Real-time face detection & recognition  
✅ Simple & efficient face encoding  
✅ Name labeling with bounding boxes  
✅ Scalable to multiple known individuals  
✅ Easy customization for personal or security projects

---

## 🚀 Demo Preview

> Replace with your GIF or image
![Demo Placeholder](https://via.placeholder.com/600x350?text=Demo+GIF+Here)

---

## 🧠 Tech Stack

- 🐍 Python 3.8+
- 🎥 OpenCV
- 🤖 face_recognition (built on top of dlib)
- 🧮 Numpy

---

## 📦 Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/Pritam033/face-recognition-opencv.git
cd face-recognition-opencv

Install Dependencies
bash
pip install -r requirements.txt
```


📁 Project Structure
```bash
face-recognition-opencv/
├── images/
│   ├── person1.jpg
│   └── person2.jpg
├── face_recognition_app.py
├── requirements.txt
└── README.md
```

How It Works:

Loads known faces from image files and encodes them.

Captures video from your webcam.

For each frame:

Detects all face locations.

Encodes detected faces.

Compares with known encodings.

Draws rectangles & labels names.

📜 [License](https://github.com/Pritam033/python_project/blob/main/License.txt)
This project is licensed under the MIT License – see the LICENSE file for details.

🙋‍♂️ Author
Pritam Som
GitHub | LinkedIn

