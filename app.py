from PIL import Image
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
# animations here: https://lottiefiles.com/getting-started
# lottie_header = load_lottierurl("https://lottie.host/529b8118-d6d6-44bc-b7e1-b5e95efe65b6/wGuM1kIVUZ.json")
# lottie_header = load_lottierurl("https://lottie.host/6db12b0a-a80f-4f8b-b256-116dc39e2fea/7FTo39uCwx.json")
# lottie_header = load_lottierurl("https://lottie.host/e5c828f1-36cd-4297-a5e0-89b0b1f8a154/ZqciHXPNuS.json")
# lottie_header = load_lottierurl("https://lottie.host/225b30c5-5a13-4573-81da-4451ae06e6c4/NlOhWl7tyn.json")
lottie_header = load_lottierurl("https://lottie.host/8c902199-8b9f-4fbc-a62d-0e0aa521dd28/FUzKZjM2AF.json")
lottie_coding = load_lottierurl("https://lottie.host/caf3346a-1dc0-4c02-9860-cf96e7d66e76/stwyAojHpV.json")
# img_contact_form = Image.open("images/logo-j.jpg")
# img_lottie_animation = Image.open("images/logo-j.jpg")
coming_soon_1 = load_lottierurl("https://lottie.host/225b30c5-5a13-4573-81da-4451ae06e6c4/NlOhWl7tyn.json")
coming_soon_2 = load_lottierurl("https://lottie.host/225b30c5-5a13-4573-81da-4451ae06e6c4/NlOhWl7tyn.json")

# --- HEADER SECTION ---
with st.container():
    left_column, right_column = st.columns(2)
    with right_column:
        st.write("##")
        st.write("##")
        st.subheader("Hi, I am Jonathan Meza :wave:")
        st.title("Backend Developer from Colombia " + "\N{grinning face}")
        st.write("I am passionate about finding ways to use Python and Django")
        st.write("[Learn More >>>](https://www.jonathanmeza.com.co)")
    

    with left_column:
        st_lottie(lottie_header, height=400, key="header")  

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

# ---- PROJECTS ----

# ---- Project 1 ----

with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        # st.image(img_lottie_animation)
        st_lottie(coming_soon_1, height=300, key="comingsoon1")
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie File in Streamlit
            """
        )
        st.markdown("[Watch Video ...](https://www.youtube.com/live/Sj57a1mP_n0?feature=share)")

# ---- Project 2 ----        

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        # insert image
        # st.image(img_lottie_animation)
        st_lottie(coming_soon_2, height=300, key="comingsoon2")
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie File in Streamlit
            """
        )
        st.markdown("[Watch Video ...](https://www.youtube.com/live/Sj57a1mP_n0?feature=share)")             