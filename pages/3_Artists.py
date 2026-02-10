import streamlit as st
import auth
from datetime import datetime
from data import ARTISTS, FILMS, MUSIC
from utils import get_music_status, get_film_status

st.page_link("streamlit_app.py", label="⬅ Back to Home")

st.title("🎨 Artist Pages")

# Build artist data with works
artists_data = {}
for artist_name, artist_info in ARTISTS.items():
    works = []
    for work_id in artist_info["works"]:
        # Check if it's a film
        film = next((f for f in FILMS if f["id"] == work_id), None)
        if film:
            works.append({
                "title": film["title"],
                "type": "film",
                "release_date": film["release_date"]
            })
        else:
            # Check if it's music
            music = next((m for m in MUSIC if m["id"] == work_id), None)
            if music:
                works.append({
                    "title": music["title"],
                    "type": "music",
                    "release_date": music["release_date"]
                })
    
    artists_data[artist_name] = {
        "bio": artist_info["bio"],
        "works": works
    }

choice = st.selectbox("Choose an artist", list(artists_data.keys()))
data = artists_data[choice]

st.subheader(choice)
st.write(f"**Bio:** {data['bio']}")

st.divider()
st.subheader("Works")

for w in data["works"]:
    st.write(f"### {w['title']} ({w['type']})")

    if w["type"] == "music":
        status, days = get_music_status(w["release_date"])
    else:
        status, days = get_film_status(w["release_date"])

    st.write(f"**Status:** {status}")
    if days:
        st.write(f"⏳ {days} days remaining")

    st.write(f"**Release Date:** {w['release_date'].strftime('%d %B %Y')}")
st.divider()