# 🎧 Emotion-Based AI Music Player

This AI-powered music player detects your facial expression and plays songs based on your current **mood**. Built with OpenCV, FER (Facial Emotion Recognition), TensorFlow, and Streamlit, it’s a real-time, camera-driven, emotion-aware music experience.

---

## 🌟 Features

- 🎥 Real-time webcam-based emotion detection
- 😊 Supports multiple emotions: `happy`, `sad`, `angry`, `neutral`
- 🎵 Emotion-mapped local music playback (via `pygame`)
- 🌐 Streamlit-based modern UI with dark mode
- 🧠 Built using Python, TensorFlow, FER, and OpenCV
- 🖥️ Fully compatible with **Mac M1 / M2**

---

## 🛠️ Tech Stack

| Component         | Library/Tool       |
|-------------------|--------------------|
| Emotion Detection | `fer`, `opencv`    |
| Deep Learning     | `tensorflow`       |
| Audio Playback    | `pygame.mixer`     |
| Frontend UI       | `streamlit`        |
| Web Integration   | `subprocess` (backend calls from UI)

---

## 🗂️ Folder Structure

emotion_music_player/ ├── backend/ │ ├── emotion_detector.py # detects emotion from webcam │ └── music_player.py # plays song mapped to emotion ├── data/ │ └── songs/ # mp3 files sorted by emotion ├── frontend/ │ └── app.py # Streamlit web app ├── test_emotion_music.py # Combines backend to run standalone ├── venv/ # Python virtual environment

yaml
Copy
Edit

---

## ▶️ How to Run

### 1. Clone the repo & install dependencies
```bash
git clone https://github.com/rochitl72/emotion-music-player.git
cd emotion-music-player
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
2. Add songs to folders
Add .mp3 files to data/songs/happy, sad, angry, neutral.

3. Run backend test (optional)
bash
Copy
Edit
python test_emotion_music.py
4. Run the Streamlit Web App
bash
Copy
Edit
cd frontend
streamlit run app.py
🎯 Ideal Use Cases
Hackathon submissions

Mood-based smart speaker prototypes

Mental wellness or therapy demos

AI in music or entertainment startups

🤝 Credits
Made with ❤️ by @rochitl72
Built with OpenCV, TensorFlow, FER, and Streamlit
Inspired by: PartheshSoni/emotion-based-music-player