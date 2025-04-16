# CLI CODE
# # Mad libs Python Project
# print("Welcome to Mad Libs Game! Please provide the following words: ")
# name = input("Enter a name: ")
# place = input("Enter a place: ")
# adjective = input("Enter an adjective: ")
# noun = input("Enter a noun: ")
# verb = input("Enter a verb: ")

# # Mad libs Story Paragraph
# story = f"one day, {name} went to {place}. It was a {adjective} place. There, {name} found a {noun} and decided to {verb} with it."

# print("/nHere is your Mad Libs story: ")
# print(story)

import streamlit as st # type: ignore

# CSS
st.markdown("""
    <style>
        .stApp {
        background-color: #fbeeff;
    }
        .title {
            font-size: 40px;
            color: #25A9FC;
            text-align: center;
            font-family:'Montserrat', sans-serif
        }
        .subhead {
            font-size: 20px;
            text-align: center;
            color: #555;
        }
        input[type="text"] {
            background-color: #ffffff !important;
            color: #000000 !important; 
            border-radius: 5px;
            padding: 10px;
            border: 1px solid #25A9FC;
        }
     
        .stButton>button {
            background-color:  #25A9FC;
            color: white;
            padding: 10px 24px;
            border: none;
            border-radius: 8px;
            font-weight: bold;
            cursor: pointer;
        } 
        .stButton>button:hover {
             background-color: #1e90ff;
        }
            
    </style> 
""", unsafe_allow_html=True)


# title and subhead
st.markdown('<div class="title">✨Welcome to Mad Libs Game!</div>' ,unsafe_allow_html=True)

st.markdown('<div class="subhead">Please provide the following words and get your fun story!</div>', unsafe_allow_html=True)

# user inputs
name = st.text_input("Enter a name: ")
place = st.text_input("Enter a place: ")
adjective = st.text_input("Enter an adjective: ")
noun = st.text_input("Enter a noun: ")
verb = st.text_input("Enter a verb: ")

#button to generate story
if st.button("Generate My Story"):
    if name and place and adjective and noun and verb:
        story = f"ond day, {name} went to {place}. It was a {adjective} place. There, {name} found a {noun} and decided to {verb} with it. "
        st.markdown("### 📝 Here is your Mad Libs Story: ")
        st.success(story)
    else:
        st.error("⚠️ Please fill in all the fields.")

