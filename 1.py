from gtts import gTTS
import os

# Input text
text = "Hello, how are you?"

# Convert text to speech
tts = gTTS(text=text, lang='en')

# Save the converted audio to a file
tts.save("output.mp3")

# Play the converted file
os.system("start output.mp3")  
