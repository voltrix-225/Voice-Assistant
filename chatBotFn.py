
import speech_recognition as sr
import pyttsx3
import wikipedia    #used in main
from datetime import *
from pywhatkit import  *
import requests
import time         #used in main
import keyboard     #used in main
import webbrowser
import os           #used in main

contact_list = {}#add whatsapp contacts here{"name" : "number"}

engine = pyttsx3.init()

#start_server()

curr_td = datetime.now()

def speak(op_txt):
    engine.say(op_txt)
    engine.runAndWait()

def listen():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("LISTENING...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        user_said = r.recognize_google(audio, language = 'en-in')
        print(f"USER: {user_said}")    
    
    except Exception as e:
        #speak("say that again please..")
        return "none"
    return user_said

def op_query(answer):
    print(answer)
    speak(answer)

def greet():
    #curr_td = datetime.now()
    hour = int(curr_td.strftime("%H"))
    if hour>=4 and hour<12:
        return speak("Good Morning!")
    if hour>=12 and hour<16:
        return speak("Good Afternoon!")
    else:
        return speak("Good Evening!")

def send_Message(contact, message):
    contact = contact
    message = message
    sendwhatmsg_instantly(contact,message)
    return 

def play_video(vid_name):
    playonyt(vid_name)

def open_site(site):
    if requests.head(f"https://www.{site}.in")==200:
        webbrowser.open(f"https://www.{site}.in")
    else:
        webbrowser.open(f"https://www.{site}.com")

def general_search(term):
    webbrowser.open(f"www.google.com/search?q=%{term}")

def news(term):
    term = term
    webbrowser.open(f"https://news.google.com/search?q=%{term}")

