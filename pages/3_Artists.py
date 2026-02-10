import streamlit as st

st.title("🎨 Artist Pages")

artists = {
    "Aiko Tanaka": {
        "bio": "Japanese filmmaker known for minimalist emotional storytelling.",
        "upcoming": "The Silent Path – 1 March 2026",
        "event": "Tokyo Release Party – 28 February 2026"
    },
    "Jonas Ravn": {
        "bio": "Norwegian director exploring isolation and landscape.",
        "upcoming": "Night Train to Oslo – 12 March 2026",
        "event": "Oslo Premiere – 10 March 2026"
    }
}

choice = st.selectbox("Choose an artist", list(artists.keys()))

data = artists[choice]

st.subheader(choice)
st.write(f"**Bio:** {data['bio']}")
st.write(f"**Upcoming Release:** {data['upcoming']}")
st.write(f"**Event:** {data['event']}")