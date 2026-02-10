import streamlit as st

USERS = {
    "demo@user.com": {"password": "password123", "name": "Demo User"},
}

def login():
    st.sidebar.subheader("Login")
    email = st.sidebar.text_input("Email")
    password = st.sidebar.text_input("Password", type="password")
    if st.sidebar.button("Sign in"):
        user = USERS.get(email)
        if user and user["password"] == password:
            st.session_state.user = {"email": email, "name": user["name"]}
            st.sidebar.success(f"Welcome, {user['name']}")
        else:
            st.sidebar.error("Invalid credentials")

if "user" not in st.session_state:
    st.session_state.user = None

if st.session_state.user:
    st.sidebar.write(f"Signed in as {st.session_state.user['name']}")
    if st.sidebar.button("Sign out"):
        st.session_state.user = None
else:
    login()