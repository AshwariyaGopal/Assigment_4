# # Hangman Game Python CLI
# import random

# #words list 
# words = ["python","programming","hangman","computer","development","frontend","backened","javascript","typescript"]

# # choose a random word
# secret_word = random.choice(words)
# guessed_word = ["_"] * len(secret_word)
# attempts = 6
# guessed_letters = []

# #Introduction
# print("Welcome to the Hangman Game!")
# print("Guess the secret word letter by letter.")
# print(f"The word has {len(secret_word)} letters.")
# print("You hav 6 chances. Good Luck\n")

# while attempts > 0:
#     #Display current progress
#     print("word:", "".join(guessed_word))
#     print(f"Guessed letters: {', '.join(guessed_letters)}")
#     print(f"Remaining attempts: {attempts}")

#     # User Input
#     guess = input("Guess a letter: ").lower()

#     # Input Validation
#     if len(guess) != 1 or not guess.isalpha():
#         print("Invalid input! Please enter a single letter.\n")
#         continue

#     # Check is the letter already guessed
#     if guess in guessed_letters:
#         print("You already guessed that letter! Try again.\n")
#         continue


#     # Add guessed letter to the list
#     guessed_letters.append(guess)

#     # Check is the guessed letter is in the secret word
#     if guess in secret_word:
#         print(f"Good Job! '{guess}' is in the word.\n")
#         for i in range(len(secret_word)):
#             if secret_word[i] == guess:
#                 guessed_word[i] = guess
#     else: 
#         print(f"Oops! '{guess}' is not in the word.\n")
#         attempts -= 1

#             # Check is the user has guessed the word
#     if "_" not in guessed_word:
#         print("Congratulations! you guessed the word:", secret_word)
#         break
        


# # If the user runs out of attempts
# if "_" in guessed_word:
#     print("Game Over! You ran out of attempts.")
#     print(f"The secret word was: {secret_word}")




import streamlit as st # type: ignore
import random

# --- Session state to keep game data ---
if 'secret_word' not in st.session_state:
    st.session_state.secret_word = random.choice(
        ["python", "programming", "hangman", "computer", "development", "frontend", "backend", "javascript", "typescript"]
    )
    st.session_state.guessed_word = ["_"] * len(st.session_state.secret_word)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = []
    st.session_state.game_over = False

# --- Title and Instructions ---
st.title("🎮 Hangman Game")
st.write("🎯 **Guess the secret word letter by letter.** ")
st.write(f"📏 The word has **{len(st.session_state.secret_word)}** letters.")
st.write("💡 You have **6 chances**. Good luck!")

# --- Display word progress ---
st.subheader("🔠 Word:")
st.write(" ".join(st.session_state.guessed_word))

st.write(f"🔤 **Guessed Letters:** {', '.join(st.session_state.guessed_letters)}")
st.write(f"❤️ **Remaining Attempts:** {'❤️' * st.session_state.attempts}")

# --- User Input ---
if not st.session_state.game_over:
    guess = st.text_input("Enter a letter", max_chars=1)

    if st.button("Submit Guess"):
        guess = guess.lower()

        if not guess.isalpha() or len(guess) != 1:
            st.warning("Please enter a single valid letter.")
        elif guess in st.session_state.guessed_letters:
            st.info("You've already guessed that letter!")
        else:
            st.session_state.guessed_letters.append(guess)

            if guess in st.session_state.secret_word:
                for i, char in enumerate(st.session_state.secret_word):
                    if char == guess:
                        st.session_state.guessed_word[i] = guess
                st.success(f"✅ Good job! '{guess}' is in the word.")
            else:
                st.session_state.attempts -= 1
                st.error(f"❌ Oops! '{guess}' is not in the word.")

            # Check for win
            if "_" not in st.session_state.guessed_word:
                st.success(f"🏆 Congratulations! You guessed the word: {st.session_state.secret_word}")
                st.session_state.game_over = True

            # Check for loss
            elif st.session_state.attempts == 0:
                st.error("💀 Game Over! You ran out of attempts.")
                st.info(f"The secret word was: {st.session_state.secret_word}")
                st.session_state.game_over = True

# --- Restart Game ---
if st.button("🔄 Restart Game"):
    st.session_state.secret_word = random.choice(
        ["python", "programming", "hangman", "computer", "development", "frontend", "backend", "javascript", "typescript"]
    )
    st.session_state.guessed_word = ["_"] * len(st.session_state.secret_word)
    st.session_state.attempts = 6
    st.session_state.guessed_letters = []
    st.session_state.game_over = False
    st.rerun()
