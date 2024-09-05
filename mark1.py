import pyttsx3
import speech_recognition as sr
import datetime
import random
import os
import webbrowser
import wikipedia
import requests
from bs4 import BeautifulSoup
secret_keyword = "html and css"
import pyaudio
import cv2
from playsound import playsound
# this is for doing many functuon at the same time
from threading import Thread
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(voices[3].id)
engine.setProperty('voice', voices[3].id)
playsound('intro.mp3')
def music():
    playsound('')
def syst():
    playsound('intro1.wav')
greetings ="Allow me to introduce my self, I am,jarvis  ? A virtual artificial intelegence, and, I am here to, Assist you, with variety of task, Since Best I care, Let's say 24 hours a day, 7 days a week,. Importing all prefrences from Home Interface, System now Fully Operational, Sir!"
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone () as source: 
        r.adjust_for_ambient_noise(source, duration=0.2)
        print("listining...")
        #r.pause_threshold = 1
        audio = r.listen(source) 
        # it will make a better recognit
# it is used here for knowing your speech what have youu spoken
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}")
# as name say you have an exception here if jarvis didn'understand anything
    except Exception as e:
        print("say that again please...")
        return"none"
    return query
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour <12:
        speak(" Hello Sir! Good Morning ")
    elif hour >= 12 and hour <18:
        speak(" Hello Sir! Good Afternoon")
    else:
        speak("Hello Sir! Good Evening ")
    if __name__ == '__main__':
        Thread(target = syst).start()
        Thread(speak(greetings)).start()
if __name__ == "__main__":
    wish()
    while True:
        query = takecommand().lower()
#This is the code to search from the wikipedia      
        if 'search' in query:
                speak('searching Internet...')
                results = wikipedia.summary(query, sentences=2)
                speak("According too sources")
                print(results)
                speak(results)
        elif 'the news' in query:
            url = 'https://www.bbc.com/news'
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            headlines = soup.find('body').find_all('h3')
            for x in headlines:
                speak(x.text.strip())
                print(x.text.strip())