from backend.emotion_detector import detect_emotion
from backend.music_player import play_song
import time

if __name__ == "__main__":
    emotion = detect_emotion()
    if emotion:
        play_song(emotion)
        # ⏸️ Wait for 15 seconds or length of the song
        time.sleep(15)
    else:
        print("No emotion detected.")
