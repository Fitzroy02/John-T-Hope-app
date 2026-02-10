import streamlit as st
import auth

st.page_link("streamlit_app.py", label="⬅ Back to Home")

st.title("🎭 Genre Rotation")

genres = [
    "Drama", "Comedy", "Thriller", "Horror", "Sci‑Fi", "Fantasy",
    "Romance", "Documentary", "World Cinema", "Indie",
    "Experimental", "Animation", "Crime", "Mystery", "Adventure",
    "Noir", "Biographical", "Historical", "Political", "Art House"
]

st.write("Daily rotation mockup for 20 genres.")

for g in genres:
    st.subheader(g)
    st.write("• Film 1")
    st.write("• Film 2")
    st.write("• Film 3")
    st.write("• Film 4")
    st.divider()