#!/usr/bin/env python3
# Requires PyAudio and PySpeech.

import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS

def speak(audioString):
    print(audioString + "\n")
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3 >/dev/null 2>&1")

def recordAudio():
    # Record Audio
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)

        # Speech recognition using Google Speech Recognition
        data = ""
    try:
        data = r.recognize_google(audio)
        speak("You said: " + data)
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))

    return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")

    if "what time is it" in data:
        speak(ctime())

    if "where is" in data:
        data = data.split(" ")
        location = data[2:]
        speak("Hold on Friend, I will show you where " + location + " is.")
        os.system("open -a 'Google Chrome' https://www.google.com/maps/place/" + location + "/&amp;")
        
    if "what is" in data:
        data = data.split(" ")
        what = data[2]
        speak("Hold on Friend, I will show you what " + what + " is.")
        os.system("open -a 'Google Chrome' https://www.google.com/search?q=" + what)
        
    if "shut down my PC" in data:
        speak("Your PC is shuting down\n")
        os.system("shutdown -h now")

# initialization
time.sleep(2)
speak("Hi, what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data)
