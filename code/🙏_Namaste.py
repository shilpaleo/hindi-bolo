import streamlit as st

st.set_page_config(
    page_title="Hindi Bolo",
    page_icon="🦄",
)

st.title("Hindi Bolo mein aapka swagat hai!🙏")

st.sidebar.success("Select a practise activity above :point_up_2:")

st.markdown(
    """
    The above translates to "Welcome to Hindi Bolo". Hindi Bolo is a hobby project app created by a mummy to find fun ways to engage my kid in conversing in Hindi, the Indian language. I found this a fun way for myself, too, to apply my data science knowledge to help with my kid's education. 
    
    This app intends to include and continuously expand on various activities inspired by Singapore Hindi school curriculum for Primary kids.

    ### What activities can you find here today? :open_book:
    (:point_left: Select from the sidebar to your left)
    - Pronunciation practise :microphone:
    - Flash card description practise :frame_with_picture: _(development ongoing..:hammer:)_
    - More to come..:mega:

    ### Have feedback or ideas to make this better? :writing_hand:
    - Connect on [LinkedIn](https://www.linkedin.com/in/shilpa-sindhe/)
    - Find my code on [Github](https://github.com/shilpaleo/hindi-bolo)
"""
)