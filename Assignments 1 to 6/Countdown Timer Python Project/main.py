# # Countdown Timer CLI
# import time

# # Introduction
# print("Welcome to the Countdown Timer!")
# print("Enter the time in Seconds, and I'll count down for you.\n")

# # User se input lena
# try:
#     total_time = int(input("Enter the count down timer in seconds. "))
# except ValueError:
#     print("Invalid input! Please enter a valid number. ")

#     # Count down logic
# while total_time > 0:
#     minutes, seconds = divmod(total_time,60)
#     timer = f"{minutes:02d}:{seconds:02d}"
#     print(timer, end="\r")
#     time.sleep(1)
#     total_time -= 1

#     # times up
# print("Time's Up!")

import streamlit as st # type: ignore
import time

# Title
st.title("⏳ Countdown Timer")

# Instruction
st.write("Enter the countdown time in **seconds**, and watch the timer tick!")

# User input
total_time = st.number_input("Enter time in seconds:", min_value=1, step=1)

# Start button
if st.button("Start Countdown"):
    placeholder = st.empty()
    for remaining in range(total_time, 0, -1):
        minutes, seconds = divmod(remaining, 60)
        timer = f"{minutes:02d}:{seconds:02d}"
        placeholder.markdown(f"## ⏰ {timer}")
        time.sleep(1)
    placeholder.markdown("## 🎉 Time's Up!")
