import streamlit as st  # type: ignore

# Page configuration
st.set_page_config(
    page_title="My Cool Python Website",
    page_icon="🌐",
    layout="centered",
    initial_sidebar_state="auto"
)
with st.sidebar:
    st.header("📞 Contact")
    st.write("👩 Ashwariya Gopal")
    st.write("✉️ ashwariyagopal@gmail.com")
    st.write("💻 [GitHub](https://github.com)")
# Custom CSS for better visuals
st.markdown("""
    <style>
        .stApp {
            background-color: #f0f8ff;
            padding: 20px;
            border-radius: 10px;
        }
        h1 {
            color: #1f77b4;
        }
        h2 {
            color: #ff7f0e;
        }
    </style>
""", unsafe_allow_html=True)

# Title and subtitle
st.title("🌐 Welcome to My Python Website")
st.subheader("🚀 Explore Amazing Features")

# Intro text
st.write("This is a simple yet beautiful Streamlit app built in just 15 minutes!")

# Divider
st.markdown("---")

# Button interaction
if st.button("✨ Click Me"):
    st.success("Thank You for clicking the button! 😊")

# User input
st.markdown("### 👤 Tell me about you:")
name = st.text_input("What is your name?")
if st.button("🚀 Greet Me"):
    if name:
        st.balloons()
        st.success(f"Hello **{name}**! Welcome to my Website! 🎉")
    else:
        st.warning("Please enter your name first!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Python & Streamlit")

