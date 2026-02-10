import streamlit as st
import auth

st.set_page_config(page_title="Film Platform", page_icon="🎬", layout="wide")

st.title("🎬 Welcome to the Film Platform Prototype")

st.page_link("pages/1_Release_Hub.py", label="Go to Release Hub", icon="📅")
st.page_link("pages/2_Genres.py", label="Browse Genres", icon="🎭")
st.page_link("pages/3_Artists.py", label="Artist Pages", icon="🎨")
st.page_link("pages/5_Film_Page.py", label="Sample Film Page", icon="🎬")
st.page_link("pages/4_Events.py", label="Events & Parties", icon="🎉")
