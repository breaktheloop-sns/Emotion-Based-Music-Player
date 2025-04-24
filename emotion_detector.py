# backend/emotion_detector.py

import cv2
from fer import FER

def detect_emotion():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    detector = FER()  # ✅ Correct usage

    print("[INFO] Webcam started. Press 'q' to capture your emotion.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("[ERROR] Could not access webcam.")
            break

        # Show the webcam feed
        cv2.imshow("Webcam - Press Q", frame)

        # Press 'q' to capture and analyze
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    # Analyze the captured frame
    emotions = detector.detect_emotions(frame)

    if emotions:
        top_emotion = max(emotions[0]["emotions"], key=emotions[0]["emotions"].get)
        print(f"[INFO] Detected Emotion: {top_emotion}")
        return top_emotion
    else:
        print("[INFO] No face detected. Defaulting to 'neutral'")
        return "neutral"
