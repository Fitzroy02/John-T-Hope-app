import streamlit as st
from datetime import datetime, timedelta

st.title("📅 Release Hub")

st.write("Upcoming releases, countdowns, and event information.")

# Example data
releases = [
    {"title": "The Silent Path", "artist": "Aiko Tanaka", "release_date": datetime(2026, 3, 1)},
    {"title": "Night Train to Oslo", "artist": "Jonas Ravn", "release_date": datetime(2026, 3, 12)},
    {"title": "Dust & Honey", "artist": "Marisol Vega", "release_date": datetime(2026, 4, 5)},
]

for r in releases:
    days_left = (r["release_date"] - datetime.now()).days
    st.subheader(r["title"])
    st.write(f"**Artist:** {r['artist']}")
    st.write(f"**Release Date:** {r['release_date'].strftime('%d %B %Y')}")
    st.write(f"⏳ **Countdown:** {days_left} days remaining")
    st.divider()