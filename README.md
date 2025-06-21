# Driver Fatigue Detection 🚗💤

A real-time driver drowsiness and fatigue detection system using **MediaPipe**, **OpenCV**, and **Python** — capable of identifying signs like closed eyes, open mouth, and critical fatigue states. Alerts are triggered using sound alarms based on eye and mouth activity.

> 💡 This was built as a **Minor Project** under the guidance of faculty and developed in a team of 4. I proudly led the team as **Team Leader**, overseeing the integration of computer vision, logic design, and testing phases.

---

## 🔍 What It Detects

| Eye Status | Mouth Status | Detection Result |
|------------|--------------|------------------|
| Open       | Closed       | ✅ Alert          |
| Closed     | Closed       | ⚠️ Drowsy         |
| Open       | Open         | ⚠️ Fatigued       |
| Closed     | Open         | 🔴 Critical       |

---

## 🎯 Features

- 👁️ Eye Aspect Ratio (EAR) detection
- 👄 Mouth Aspect Ratio (MAR) detection
- 🎯 Real-time classification into Alert, Drowsy, Fatigued, or Critical
- 🔊 Gradually increasing alarm system based on fatigue level
- 🎥 Works in real-time with webcam
- ✅ Pure Python + MediaPipe (no `.dat` file or dlib headaches)

---

## 🛠 Tech Stack

- Python 3.10+
- OpenCV
- MediaPipe
- NumPy

---

## 🧠 How It Works

1. MediaPipe detects facial landmarks.
2. EAR and MAR are computed from eye and mouth keypoints.
3. Fatigue state is determined based on thresholds:
   - EAR < 0.2 → drowsy
   - MAR > 0.35 → fatigued
4. Alert types are shown on screen and an audible beep is played.

---

## 📸 Demo Screenshots

| Alert Mode | Drowsy Mode | Fatigue Mode | Critical Mode |
|------------|-------------|--------------|----------------|
| ![](![Screenshot 2025-06-21 162717](https://github.com/user-attachments/assets/cfbb9ebc-44f2-4d6a-96aa-1d80710958e8)
) | ![](![Screenshot 2025-06-21 162830](https://github.com/user-attachments/assets/d24a5a5d-5b40-4671-a106-fe6369e7ab2a)
) | ![](![Screenshot 2025-06-21 162612](https://github.com/user-attachments/assets/ccf43215-19b7-4b7b-a9ef-82f492f42f78)
) | ![](![Screenshot 2025-06-21 162624](https://github.com/user-attachments/assets/b799335b-77e8-4b9c-b849-609be5dff640)
) |

---

## 🚀 Getting Started

```bash
git clone https://github.com/KALYAN07YADAV/driver-fatigue-detection.git
cd driver-fatigue-detection
pip install -r requirements.txt
python fatigue_detector_mediapipe.py

