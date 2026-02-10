import streamlit as st

st.title("🎉 Events & Parties")

events = [
    {"name": "Tokyo Release Party", "date": "28 Feb 2026", "location": "Tokyo"},
    {"name": "Oslo Premiere", "date": "10 Mar 2026", "location": "Oslo"},
    {"name": "London Indie Night", "date": "22 Mar 2026", "location": "London"}
]

for e in events:
    st.subheader(e["name"])
    st.write(f"📅 {e['date']}")
    st.write(f"📍 {e['location']}")
    st.divider()