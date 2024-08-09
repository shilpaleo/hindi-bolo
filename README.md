:woman_teacher: 
# hindi-pronunciation
This started as an idea where I wanted to create a fun and engaging way for my toddler to boost confidence in speaking the indian language, Hindi. 
I prompted ChatGPT for ideas build something using Python and start simple, which can be scaled and enhanced later. 
The simple `Streamlit` app currently does the following:
  - Takes a pre-defined target word
  - Uses Google's text-to-speech (gTTS) to take the target word and covert to audio
  - That audio is played as an input for children to listen to the "proper/target" pronunciation
  - Then, record their way of pronouncing the same target word - which undergoes speech-to-text transformation (Streamlit Mic Recorder with Google API)
  - Both target and response words are compared, and a celebratory or encouraging try-again message is finally displayed to prompt further practice!
