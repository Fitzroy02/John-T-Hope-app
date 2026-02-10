import streamlit as st
import auth

st.page_link("streamlit_app.py", label="⬅ Back to Home")

st.title("🎉 Events & Parties")

events = [
    {"id": 1, "name": "Tokyo Release Party", "date": "28 Feb 2026", "location": "Tokyo"},
    {"id": 2, "name": "Oslo Premiere", "date": "10 Mar 2026", "location": "Oslo"},
    {"id": 3, "name": "London Indie Night", "date": "22 Mar 2026", "location": "London"},
]

if "rsvps" not in st.session_state:
    st.session_state.rsvps = []

for e in events:
    st.subheader(e["name"])
    st.write(f"📅 {e['date']}  |  📍 {e['location']}")

    if not st.session_state.get("user"):
        st.warning("Sign in to RSVP for this event.")
    else:
        with st.form(f"rsvp_{e['id']}"):
            name = st.text_input("Your name", value=st.session_state.user["name"])
            email = st.text_input("Your email", value=st.session_state.user["email"])
            attending = st.checkbox("I will attend")
            submitted = st.form_submit_button("RSVP")

            if submitted and attending and name and email:
                st.session_state.rsvps.append(
                    {"event_id": e["id"], "name": name, "email": email}
                )
                st.success("RSVP recorded.")

    st.divider()