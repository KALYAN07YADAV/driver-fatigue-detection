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
| ![](screenshots/status_alert.png) | ![](screenshots/status_drowsy.png) | ![](screenshots/status_fatigue.png) | ![](screenshots/status_critical.png) |

---

## 🚀 Getting Started

```bash
git clone https://github.com/KALYAN07YADAV/driver-fatigue-detection.git
cd driver-fatigue-detection
pip install -r requirements.txt
python fatigue_detector_mediapipe.py

