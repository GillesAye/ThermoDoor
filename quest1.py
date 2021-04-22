# Import the required module for text 
# to speech conversion
from gtts import gTTS
  
# This module is imported so that we can 
# play the converted audio
import os
  
# The text that you want to convert to audio
mytext = ' Please listen carefully. Do not enter if you or anyone in your home had contact within the last fourteen days with any person under screening/testing for COVID-19, or with known or suspected COVID-19. If you currently have any of the following symptoms :\nFever , or a sense of having a fever.\nNew cough, \nNew shortness of breath \nNew sore throat \nNew muscle aches (myalgias) ,that you can not attribute to another health condition or that may have been caused by a specific activity. Make sure your face mask is on'   
  
# Language in which you want to convert
language = 'en'
  
# Passing the text and language to the engine, 
# here we have marked slow=False. Which tells 
# the module that the converted audio should 
# have a high speed
myobj = gTTS(text=mytext, lang=language, slow=False)
  
# Saving the converted audio in a mp3 file named
# welcome 
myobj.save("welcome.mp3")
  
# Playing the converted file
os.system("mpg321 welcome.mp3")
