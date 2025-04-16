import streamlit as st  # type: ignore
import random

# css

st.markdown("""

  <style>
     .stApp {
            background-color: #f5f6fa;
            color: #2f3542;
            font-family: 'Arial' , sans-serif;
      }
      h1,h2,h4 {
            text-align: center;
            color: #ff4757;
      }
     .stButton>button {
            width: 100%;
            font-size:18px;
            padding:10px;
            border-radius: 10px;
            background-color: #70a1ff;
            color: white;
            transition: 0.3s ease-in-out;
            border: none;
            
        }
      .stButton<button:hover {
            background-color: #1e90ff !important;
            color: white !important;
            transform: scale(1.03);
            
        }

    </style>
""", unsafe_allow_html=True)

# Game Title

st.markdown("<h1>✊ 🖐 ✌️ Rock, Paper, Scissors Game</h1>", unsafe_allow_html=True)
st.write("### 🤖 Play against the Computer!")

choices = ["✊ Rock", "🖐 Paper", "✌️ Scissors"]
user_choice = st.selectbox("🔘 Select your move:", choices)


# play button
if st.button("🎮 Play Now!"):
    computer_choice = random.choice(choices)


# Determine Winner

    user_clean = user_choice.split(" ")[1]
    comp_clean = computer_choice.split(" ")[1]

    if user_clean == comp_clean:
        result = "🤝 It's a tie!"
    elif (
        (user_clean == "Rock" and comp_clean == "Scissors") or
        (user_clean == "Paper" and comp_clean == "Rock") or
        (user_clean == "Scissors" and comp_clean == "Paper")
    ): 
        result = "🎉 You win!"

    else:
        result = "💻 Computer wins!"


   # display result

    st.markdown(f"<h2>{result}</h2>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center;'>You chose: <strong>{user_choice}</strong> | Computer chose: <strong>{computer_choice}</strong></p>", unsafe_allow_html=True)

    if st.button("🔄 Reset Game"):
        st.rerun()

   

st.markdown("<h4 style='text-align: center; color: #2f3542;'>💖 Made by Ashwariya Gopal</h4>", unsafe_allow_html=True)
