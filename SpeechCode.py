#Simple script component to test text to speech
import os

#Using the eSpeak speech synthesizer C library
def Say(text):
        os.popen ('espeak "'+text+'" --stdout | aplay 2>/dev/null')
        
#Takes input from the user and says it out loud
while True:
    typedString = input()
    Say(typedString)
