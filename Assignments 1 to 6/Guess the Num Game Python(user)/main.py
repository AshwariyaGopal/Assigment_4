# # Guess the number Game  - User Guesses  -3
# import random
# number = random.randint(1,100)
# guesses = 0

# while True:
#     user_guess = input("Enter your guess: ")

#     try:
#         user_guess = int(user_guess)
#         guesses += 1

#         if user_guess < number:
#             print("Too low! Try again")
#         elif user_guess > number:
#             print("Too high! Try again")
#         else:
#             print(f"Congratulations! You guesses the number in {guesses} tries.")
#             break
#     except ValueError:
#         print("Please enter a valid number.")

import streamlit as st  # type: ignore
import random

# CSS
st.markdown("""
    <style>
       .stApp {
            background-color: #f0f8ff;
            font-family: 'Arial', sans-serif;
        }
        .stTextInput>div>div>input {
            background-color: #f0f8ff;
            color: #333333;
            border-radius: 5px;
            padding: 12px 20px;
            font-size: 16px;
            border: 2px solid #b0c4de

        }    
        .stTextInput>div>div>input:focus {
            border-color: #4682b4;
            box-shadow: 0 0 10px rgba(70,130,180,0.5);
            
        } 
            
        .stButton>button {
            background-color: #4682b4;
            color: white;
            font-size: 16px;
            padding: 10px 20px;
            border-radius: 5px;
            border: none;
            
        }
        
            
        .stButton>button:hover {
             background-color: #5a9bd5; 
        }
        
            
        .stMarkdown {
            color: #333333;
            font-size: 18px;
        }
        .stAlert {
            font-size: 18px;
            color: #4682b4; /* Steel blue for messages */
        }
    </style>

""", unsafe_allow_html=True)

# Initialize game variables in session state
if 'number' not in st.session_state:
    st.session_state.number = random.randint(1,10)
    st.session_state.guesses = 0

# Page title
st.title("🎯 Guess the Number Game")

# Add some description
st.markdown("""

Welcome to the **Guess the Number** game!
🧠 **Rules:**
- I am thinking of a number between **1 and 10**.
- Can you guess it?
- Enter your guess below and I will tell you if it's too high or too low.
""")




# Input box to get user guess
user_guess = st.text_input("🔢 Enter your guess: ",  key="guess_input", label_visibility="visible")

# Initialize result message
result = ""


# Check user guess
if user_guess:
    try:
        user_guess = int(user_guess)
        st.session_state.guesses += 1

        # Check if the guess is correct or not
        if user_guess < st.session_state.number:
            result = "⬇️ Too Low! Try Again."
        elif user_guess > st.session_state.number:
            result = "⬆️ Too High! Try Again."
        else:
            result = f"🎉 Congratulations! You guessed the number in **{st.session_state.guesses}** tries!"
            # reset the game after winning
            st.session_state.number = random.randint(1,10)
            st.session_state.guesses = 0
    except ValueError:
        result = "⚠️ Please enter a valid number."
        
# display the result and number of guesses
st.markdown(f"**Result:** {result}")
st.markdown(f"📊 **Number of guesses:** {st.session_state.guesses}")


# Add a button to restart the game
if st.button("🔄 Restart Game"):
    st.session_state.number = random.randint(1,10)
    st.session_state.guesses = 0
    
    # st.session_state.guess_input = ""  # Clear the input box()
    st.session_state.clear()

