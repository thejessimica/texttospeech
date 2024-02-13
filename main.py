import pyttsx3
from pypdf import PdfReader

engine = pyttsx3.init()
voices = engine.getProperty('voices')       #getting details of current voice
engine.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


reader = PdfReader("pdf/D&D Shop Catalog, V-1.8.pdf")
number_of_pages = len(reader.pages)
page = reader.pages[0]
text = page.extract_text()

engine.save_to_file(text, 'output/test.mp3')

print(text)
engine.say(text)


engine.runAndWait()
