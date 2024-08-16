import os
import random

import streamlit as st
from PIL import Image

# Define the relative path to the approved images folder
approved_images_dir = os.path.join(os.path.dirname(__file__), '../approved_images')

# Define the topics based on sub-folders in the approved_images directory
topics = os.listdir(approved_images_dir)

# Set Streamlit app page configurations - Icon & URL Display
st.set_page_config(
        page_title="Flashcard description",
        page_icon="🪧"
    )

# Set Streamlit sidebar contents
with st.sidebar:
    st.header("Flashcard Hindi description! :left_speech_bubble:")
    st.markdown("""
    Code on [Github](https://github.com/shilpaleo/hindi-bolo/blob/main/code/pages/2_%F0%9F%96%BC%EF%B8%8F_Flash_Card_Description.py)
                
    Here's how this game is designed:
    1. Dynamically takes a set of pre-reviewed child-safe images from a selected topic
    2. The images were generated using OpenAI Image generation API using prompts to generate few child appealing images per word within a given topic, which were then manually reviewed to shortlist one image per word, like a car, bus, ship under the topic "Vehicles"
    3. The word prompt to generate the images were hindi-to-english translated text using Open AI Chat Completions API 
    4. Kids can first select a topic, then answer a few questions to describe the picture to prompt conversation practise in Hindi! "Change Image" button can be clicked to update image to a different one within the same topic       
    """
    )

# Streamlit app title
st.title("Hindi Flashcard Activity")

# Apply CSS
st.markdown('''
<style>
    .stApp {
        background-color: #f4f69e;
    }
    p {
        color: black;
        font-size: 20px !important;
    }
    div {
        font-size: 20px !important;
    }
        .stButton>button {
        background-color: #A09EF6 !important;
        border: none !important;
    }
    .stButton>button:hover {
        border: 1px solid #000000 !important;
    }
    # .st-bq {
    #     height: 80px;
    #     line-height: 60px;
    #     padding: 1px;
    # }        
</style>
''', unsafe_allow_html=True)

# Define instructions for activity
st.write('''
:one: Select a topic from the dropdown first.<br>
:two: Once you're done answering the questions, <br>
Click Change Picture button for a new picture! :arrow_down_small:
''', unsafe_allow_html=True)

# Format topic selection and image change button
col1, col2 = st.columns(2)
with col1:
    # Dropdown for topic selection
    selected_topic = st.selectbox("Select a Topic :point_down:", topics, label_visibility='collapsed')

# Reset session state when the topic is changed
if 'previous_topic' not in st.session_state:
    st.session_state.previous_topic = None

if selected_topic != st.session_state.previous_topic:
    st.session_state.selected_image = None  # Reset selected image
    st.session_state.previous_topic = selected_topic  # Update the previous topic

if selected_topic:
    # Get the list of images in the selected topic's folder
    topic_folder = os.path.join(approved_images_dir, selected_topic)
    images = [img for img in os.listdir(topic_folder) if img.endswith(".png")]

    # Always show the "Change Image" button
    with col2:
        change_image_clicked = st.button("Change Picture")

    if images:
        # Initialize or update session state to store the selected image
        if st.session_state.selected_image is None or change_image_clicked:
            st.session_state.selected_image = random.choice(images)

        # Get the selected image from session state
        image_path = os.path.join(topic_folder, st.session_state.selected_image)

        # Display the image
        image = Image.open(image_path)
        st.image(image)

        st.subheader("Describe the picture! :microphone:", divider=True)

        # Display Hindi questions with English translations inside expanders
        with st.expander(":question: यह कौन सा चित्र है?"):
            st.write("What picture is this?")

        with st.expander(":rainbow: इस चित्र का रंग क्या है?"):
            st.write("What color is the picture?")

        with st.expander(":loud_sound: इस चित्र के बारे में कुछ कहो।"):
            st.write("Say something about this picture.")