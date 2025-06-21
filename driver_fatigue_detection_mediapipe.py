import cv2
import numpy as np
import time
import winsound
import mediapipe as mp
from collections import deque

# Mediapipe setup
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=False, max_num_faces=1, refine_landmarks=True, min_detection_confidence=0.5)

# EAR
def eye_aspect_ratio(landmarks, eye_indices):
    eye = np.array([(landmarks[i][0], landmarks[i][1]) for i in eye_indices])
    A = np.linalg.norm(eye[1] - eye[5])
    B = np.linalg.norm(eye[2] - eye[4])
    C = np.linalg.norm(eye[0] - eye[3])
    return (A + B) / (2.0 * C)

# MAR
def mouth_aspect_ratio(landmarks):
    top = np.linalg.norm(np.array(landmarks[13]) - np.array(landmarks[14]))
    bottom = np.linalg.norm(np.array(landmarks[87]) - np.array(landmarks[178]))
    width = np.linalg.norm(np.array(landmarks[78]) - np.array(landmarks[308]))
    return (top + bottom) / (2 * width)

def detect_state(avg_ear, avg_mar):
    eye_closed = avg_ear < 0.22
    mouth_open = avg_mar > 0.30  # More sensitive threshold

    if eye_closed and mouth_open:
        return "CRITICAL", (0, 0, 255), 1200
    elif eye_closed:
        return "DROWSY", (0, 165, 255), 900
    elif mouth_open:
        return "FATIGUE", (0, 255, 255), 700
    else:
        return "ALERT", (0, 255, 0), 500

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Camera not accessible.")
        return

    ear_buffer = deque(maxlen=5)
    mar_buffer = deque(maxlen=5)

    left_eye = [33, 160, 158, 133, 153, 144]
    right_eye = [362, 385, 387, 263, 373, 380]

    print("Driver Fatigue Detection Running - Press 'q' to quit")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = face_mesh.process(rgb)

        if not results.multi_face_landmarks:
            cv2.putText(frame, "No face detected", (20, 30),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 2)
            cv2.imshow("Fatigue Detector", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            continue

        h, w, _ = frame.shape
        landmarks = results.multi_face_landmarks[0].landmark
        coords = [(int(p.x * w), int(p.y * h)) for p in landmarks]

        ear = (eye_aspect_ratio(coords, left_eye) + eye_aspect_ratio(coords, right_eye)) / 2.0
        mar = mouth_aspect_ratio(coords)

        ear_buffer.append(ear)
        mar_buffer.append(mar)

        avg_ear = np.mean(ear_buffer)
        avg_mar = np.mean(mar_buffer)

        status, color, sound_freq = detect_state(avg_ear, avg_mar)

        cv2.putText(frame, f"Status: {status}", (20, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, color, 2)
        cv2.putText(frame, f"EAR: {avg_ear:.2f} | MAR: {avg_mar:.2f}", (20, 60),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

        winsound.Beep(sound_freq, 200)

        cv2.imshow("Fatigue Detector", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        time.sleep(0.1)

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
