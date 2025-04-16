# Create a Python Streamlit BMI Calculator Web App in just 6 Mins -8
import streamlit as st # type: ignore
# Title of the Web App
st.title("BMI Calculator")


# Introduction
height = st.number_input("Enter your height in meters (e.g., 1.75):", min_value=0.0, format="%.2f")
weight = st.number_input("Enter your weight in Kilograms (e.g., 70):", min_value=0.0, format="%.2f")


# Calculator BMI
if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight /  (height ** 2)
        st.success(f"Your BMI is  : {bmi: .2f}")


        # BMI Category
        if bmi < 18.5:
            st.info("You are underweight")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight")
        elif 25 <= bmi < 29.9:
            st.warning("You are overweight")
        else:
            st.error("You are obese")
    else:
            st.error("Please enter vald height and weight.")
