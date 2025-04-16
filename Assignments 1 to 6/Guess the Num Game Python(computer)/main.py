import streamlit as st  # type: ignore
import random

# Page config
st.set_page_config(page_title="Computer Guesses Your Number", page_icon="🤖", layout="centered")

# Custom Styling
st.markdown(
    """
    <style>
        .stApp {
            background: #f0f8ff;
            padding: 20px;
            border-radius: 15px;
        }
        .stButton>button {
            background: #4682b4;
            color: white;
            font-weight: bold;
            padding: 10px;
            border-radius: 10px;
        }
        .stButton>button:hover {
            background: #5a9bd5;
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Game Header
st.markdown("<h1 style='text-align: center; color: black;'>🤖 Computer Guesses Your Number</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: #3498db;'>Think of a number between 1 and 10. Don't tell me! I'll guess it. 😉</h4>", unsafe_allow_html=True)

# Session state
if 'low' not in st.session_state:
    st.session_state.low = 1
if 'high' not in st.session_state:
    st.session_state.high = 10
if 'guess' not in st.session_state:
    st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
if 'attempts' not in st.session_state:
    st.session_state.attempts = 1

# Show the computer's guess
st.subheader(f"My guess is: 🎯 **{st.session_state.guess}**")

# Feedback buttons
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🔽 Too Low"):
        st.session_state.low = st.session_state.guess + 1
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
        st.session_state.attempts += 1
        st.rerun()

with col2:
    if st.button("🎯 Correct"):
        st.success(f"Yay! I guessed your number in {st.session_state.attempts} attempts. 😎")

with col3:
    if st.button("🔼 Too High"):
        st.session_state.high = st.session_state.guess - 1
        st.session_state.guess = random.randint(st.session_state.low, st.session_state.high)
        st.session_state.attempts += 1
        st.rerun()

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.low = 1
    st.session_state.high = 10
    st.session_state.guess = random.randint(1, 10)
    st.session_state.attempts = 1
    st.rerun()
