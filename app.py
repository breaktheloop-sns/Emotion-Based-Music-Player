# frontend/app.py

import streamlit as st
import subprocess
import os

st.set_page_config(page_title="Emotion-Based Music Player", page_icon="🎧", layout="centered")

st.markdown("<h1 style='text-align: center; color: #00c4ff;'>🎧 Emotion-Based Music Player</h1>", unsafe_allow_html=True)
st.markdown("This app detects your mood and plays a matching song using AI and facial emotion recognition.")

if st.button("▶️ Detect Emotion & Play Music"):
    st.write("Running Emotion Detector...")
    result = subprocess.run(["python", "../test_emotion_music.py"], capture_output=True, text=True)

    # Extract output
    output = result.stdout.splitlines()
    emotion_line = [line for line in output if "Detected Emotion:" in line]
    song_line = [line for line in output if "Playing" in line]

    if emotion_line:
        st.success(emotion_line[0])
    if song_line:
        st.info(song_line[0])
    if not (emotion_line or song_line):
        st.warning("No face detected. Try again.")

if st.button("🛑 Stop Music"):
    os.system("pkill afplay || pkill mpg123 || pkill pygame")
    st.info("Music stopped.")
