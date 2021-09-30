#Simple script component to test voice recognition

#Using a speech regonition library
import speech_recognition as sr
a = sr.Recognizer()

#Using attached USB microphone
with sr.Microphone() as source:
    try:
        print("say something")
        audio = a.listen(source)
        data = a.recognize_google(audio)
        print(data)
        
    except:
        print("couldnt recognize")
