import streamlit as st
import pandas as pd
from PIL import Image
import io

st.set_page_config(page_title="About Me", page_icon=":smiley:", layout="wide")

st.title("Welcome!")
st.header("Hi")

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("About Me")
    st.write("""
    I am Keung Pui Shing 
    """)

    st.subheader("Get in Touch")
    user_input = st.text_input("Enter your name:", placeholder="Type your name here___")
    if user_input:
        st.success(f"Hi, {user_input}! ")
    else:
        st.warning("Please enter your name to connect with me!")

with col2:

    try:
        image = Image.open("profile.png") 
        st.image(image, caption="Hi!", width=300)
    except FileNotFoundError:
        st.error("Profile image not found. ")


st.subheader(" My Interests")
if st.button("Show My Skills"):
    st.info("Skills: Python, Streamlit, JavaScript, SQL, and Data Visualization")

    skills_data = {
        "Skill": ["Python", "Streamlit", "JavaScript", "SQL", "Data Visualization"],
        "Proficiency": [2, 2, 2, 3, 4]
    }
    df = pd.DataFrame(skills_data)
    st.table(df)
else:
    st.write("Click the button to see my skills!")

