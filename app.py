import requests
import streamlit as st
from streamlit_lottie import st_lottie

# emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Portfolio", page_icon=":tada:", layout="wide")

def load_lottierurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()    

# --- LOAD ASSETS ---
lottie_coding = load_lottierurl("https://lottie.host/caf3346a-1dc0-4c02-9860-cf96e7d66e76/stwyAojHpV.json")

# --- HEADER SECTION ---
with st.container():
    st.subheader("Hi, I am Jonathan Meza :wave:")
    st.title("Backend Developer from Colombia")
    st.write("I am passionate about finding ways to use Python and Django :snake:")
    st.write("[Learn More >>>](https://www.jonathanmeza.com.co)")

# --- WHAT I DO ---
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            As a backend developer with Django in Python, my skills and responsibilities include:

            - Creating microservices using the Django framework to build robust and scalable web applications.
            - Implementing CRUD requests using the Django REST Framework to develop RESTful APIs and handle communication logic between the frontend and backend.
            - Design and creation of relational and non-relational database models using tools such as Django ORM and databases such as PostgreSQL, MySQL or MongoDB.
            - Use of code version control using platforms such as GitHub and Bitbucket to manage collaborative development and track changes in the source code.
            - Implementation of unit and functional tests to ensure code quality and performance, using tools such as pytest or Django's testing framework.           

            """
        )
        st.write("[GitHub >>> ](https://github.com/jonma0107)")

    with right_column:
        st_lottie(lottie_coding, height=550, key="coding")    