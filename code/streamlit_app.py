from io import BytesIO

import streamlit as st
from gtts import gTTS
from streamlit_mic_recorder import speech_to_text

target_word = "नमस्ते"  # Example target word

tts = gTTS(text=target_word, lang='hi')

# Convert gTTS object to byte stream
audio_bytes = BytesIO()
tts.write_to_fp(audio_bytes)
audio_bytes.seek(0)

st.title("Hindi Pronunciation Practice")
st.text("Please try to pronounce the following:")
st.audio(audio_bytes, format='audio/mpeg')

# Apply the CSS for background color and targeted button width
st.markdown('''
<style>
    .stApp {
        background-color: #FFB6C1;
    }
    .custom-button {
        width: auto;
        display: inline-block;
        background-color: #333;
        color: white;
        padding: 0.5em 1em;
        border-radius: 5px;
        text-align: center;
        margin: 0 auto;
    }
</style>
''', unsafe_allow_html=True)

# Wrap the button in a div with a custom class
st.markdown('<div class="custom-button">', unsafe_allow_html=True)

recognized_word = speech_to_text(
    language='hi',
    start_prompt="Start recording",
    stop_prompt="Stop recording",
    just_once=False,
    use_container_width=False,  # Ensure the button width matches its content
    callback=None,
    args=(),
    kwargs={},
    key=None  # No unique key needed
)

st.markdown('</div>', unsafe_allow_html=True)

if recognized_word:
    if recognized_word == target_word:
        st.text(f"Great job! You pronounced {recognized_word} correctly.")
        st.balloons()
    else:
        st.text("Hmm, that wasn't quite right. Let's try again.")