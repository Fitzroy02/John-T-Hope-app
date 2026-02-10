import streamlit as st
import auth
from data import FILMS
from utils import get_film_status, get_early_access_status

st.page_link("streamlit_app.py", label="⬅ Back to Home")

st.title("🎬 Film Page")

# Get first film from data
film = FILMS[0]

st.header(film["title"])
st.subheader(f"By {film['artist']}")

status, days = get_film_status(film["release_date"])

st.write(f"**Status:** {status}")
if days:
    st.write(f"⏳ **Time remaining in this phase:** {days} days")

st.write(f"**Genre:** {film['genre']}")
st.write(f"**Runtime:** {film['runtime']}")
st.write(f"**Country:** {film['country']}")
st.write(f"**Release Date:** {film['release_date'].strftime('%d %B %Y')}")
st.write(f"**Event:** {film['event']}")

st.divider()

st.subheader("Synopsis")
st.write(film["synopsis"])

st.divider()

if not st.session_state.get("user"):
    st.warning("Sign in to access early viewing and moment capture.")
else:
    st.subheader("Early Access")
    ea_status, ea_days = get_early_access_status(film["release_date"])
    st.write(f"**Early Access Status:** {ea_status}")
    if ea_days:
        st.write(f"⏳ **Starts/ends in:** {ea_days} days")

    st.divider()

    st.subheader("Moment Capture")

    if "moments" not in st.session_state:
        st.session_state.moments = []

    moment = st.text_area("Capture your moment (thoughts, feelings, scene that stayed with you):")

    if st.button("Save Moment"):
        if moment.strip():
            st.session_state.moments.append(
                {"film": film["title"], "text": moment.strip()}
            )
            st.success("Moment saved.")
        else:
            st.warning("Write something before saving.")

    st.write("### Your captured moments for this film")
    for m in st.session_state.moments:
        if m["film"] == film["title"]:
            st.write(f"- {m['text']}")
