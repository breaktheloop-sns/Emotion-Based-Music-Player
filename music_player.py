import os
import random
import pygame

pygame.mixer.init()

EMOTION_FOLDER_MAP = {
    "happy": "data/songs/happy",
    "sad": "data/songs/sad",
    "angry": "data/songs/angry",
    "neutral": "data/songs/neutral"
}

def play_song(emotion):
    folder_path = EMOTION_FOLDER_MAP.get(emotion.lower(), EMOTION_FOLDER_MAP["neutral"])

    if not os.path.exists(folder_path):
        print(f"[ERROR] Folder {folder_path} not found.")
        return

    songs = [song for song in os.listdir(folder_path) if song.endswith(".mp3")]

    if not songs:
        print(f"[INFO] No songs found for emotion: {emotion}")
        return

    selected_song = random.choice(songs)
    song_path = os.path.join(folder_path, selected_song)

    print(f"[🎵 Playing] {selected_song} for emotion: {emotion}")
    pygame.mixer.music.load(song_path)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        continue
