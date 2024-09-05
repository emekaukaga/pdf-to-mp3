# This is a sample Python script.

# Press ⌃F5 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press F9 to toggle the breakpoint.

# Clearing contents of my finalText.txt file
open('finalText.txt', 'w').close()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('Emeka')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Import the required module for text
# to speech conversion
from gtts import gTTS

# This module is imported so that we can
# play the converted audio
import os

# importing required modules for pdf reading
from pypdf import PdfReader

# creating a pdf reader object
# add launch to browser html page and allow for pdf upload to replace "example.pdf"
reader = PdfReader('example.pdf')

# printing number of pages in pdf file
#print(len(reader.pages))
pageLength = len(reader.pages)

#NEW VERSION
# Initialize an empty string to collect all text
all_text = ""

# Loop through each page in the PDF
for i in range(len(reader.pages)):
    # Getting a specific page from the pdf file
    page = reader.pages[i]

    # Extracting text from the page
    text = page.extract_text()

    # Append text from this page to the cumulative string
    all_text += text #+ "\n/////////////////NEXT PAGE///////////////////\n"

# After the loop, print all text
print(all_text)


#OLD VERSION
#for i in range(len(reader.pages)):
#    # getting a specific page from the pdf file
#    page = reader.pages[i]
#    # extracting text from page
#    text = page.extract_text()
#    print (text)
#    print("/////////////////NEXT PAGE///////////////////")


    #finalText = open('finalText.txt', 'a')
    #finalText.write("/////////////////NEXT PAGE///////////////////")
    #finalText.write(text)

#Printing text
#print(text)

# The text that you want to convert to audio
# mytext = 'Welcome to the future kid!'
mytext = all_text

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
#os.system("welcome.mp3")
