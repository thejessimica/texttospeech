import pyttsx3

import pyttsx3
engine = pyttsx3.init()

voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female

engine.say("I will speak this text")

engine.runAndWait()
