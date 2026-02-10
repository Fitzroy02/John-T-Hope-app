import streamlit as st
import auth
from data import FILMS, MUSIC
from utils import get_music_status, get_film_status

st.page_link("streamlit_app.py", label="⬅ Back to Home")

st.title("📅 Release Hub")

# Combine films and music
releases = []
for film in FILMS:
    releases.append({
        "title": film["title"],
        "artist": film["artist"],
        "type": "film",
        "release_date": film["release_date"]
    })

for music in MUSIC:
    releases.append({
        "title": music["title"],
        "artist": music["artist"],
        "type": "music",
        "release_date": music["release_date"]
    })

for r in releases:
    st.subheader(r["title"])
    st.write(f"**Artist:** {r['artist']}")
    st.write(f"**Type:** {r['type'].capitalize()}")
    st.write(f"**Release Date:** {r['release_date'].strftime('%d %B %Y')}")

    if r["type"] == "music":
        status, days = get_music_status(r["release_date"])
    else:
        status, days = get_film_status(r["release_date"])

    st.write(f"**Status:** {status}")
    if days:
        st.write(f"⏳ **Time remaining:** {days} days")

    st.divider()