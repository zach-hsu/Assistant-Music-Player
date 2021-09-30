import speech_recognition as sr
import os

#Create random seed for picking songs
from random import seed
from random import randint
seed()

#Defining text to speech
def Say(text):
    os.popen ('espeak "'+text+'" --stdout | aplay 2>/dev/null')
    
#Changes from numbers to their corresponding words
num2words = {1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five', \
             6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten', \
            11: 'Eleven', 12: 'Twelve', 13: 'Thirteen', 14: 'Fourteen', \
            15: 'Fifteen', 16: 'Sixteen', 17: 'Seventeen', 18: 'Eighteen', \
            19: 'Nineteen', 20: 'Twenty', 30: 'Thirty', 40: 'Forty', \
            50: 'Fifty', 60: 'Sixty', 70: 'Seventy', 80: 'Eighty', \
            90: 'Ninety', 0: 'Zero'}
def n2w(n):
    try:
        return num2words[n]
    except KeyError:
        try:
            return num2words[n-n%10] + num2words[n%10].lower()
        except KeyError:
            print ('Number out of range')
          

data = None

#CHANGE THESE VALUES
songNum = 7 #Set this number to the number of songs in directory
directory = "/home/pi/Music/" #Set to default directory/playlist to play music from
volume = 5 #Set to prefered default volume

a = sr.Recognizer()
with sr.Microphone() as source:
    while True:
        try:
            #Collect sound data
            print("say something")
            audio = a.listen(source)
            data = a.recognize_google(audio).lower()
            print(data)
            
            if "change directory" in data: #Change to a different directory/playlist
                directory = input()
                
            if "volume" in data: #Set volume for the next song (1-10)
                for x in range(9):
                    if n2w(x+1).lower() in data or str(x+1) in data:
                        volume = x+1
                Say('Volume set to ' + str(volume))
                stay = False
                
            elif "shuffle" in data: #Plays a random song
                num = randint(1,songNum)
                
            elif "play" in data and stay: #Plays a select song in playlist (1- songnum) (see README for info about naming songs)
                for x in range(songNum - 1):
                    if n2w(x+1).lower() in data or str(x+1) in data:
                        num = x+1
                        
            elif "turn off" in data: #Ends program
                break
            
            #Plays selected song (num) at select volume (volume*10)
            os.system('mpg321 -g '+str(volume*10)+' ' + directory + str(num) + '.mp3 &')

        except:        
            print("Error")
            
