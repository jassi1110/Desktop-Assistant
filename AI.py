import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from pygame import mixer
import requests
import webbrowser
import os
import time
import random
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice' , voices[1].id)
name ="Friday"


def musicon(file):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if (hour>=0 and hour<=12):
        speak(f"Good Morning Sir! the time is {datetime.datetime.now()}")

    elif (hour>=12 and hour<=18):
        speak(f"Good afternoon Sir! the time is {datetime.datetime.now()}")

    else:
        speak(f"Good Evening! the time is {datetime.datetime.now()}")

    speak(f"Hey jassi,  I am {name} at your Service")

def take_command():
    """ It Will take a command through user mic """
    r = sr.Recognizer()
    with sr.Microphone() as source:
        musicon("Assistant.mp3")
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 500 # It will take 1 sec gap after completing the phrase
        audio = r.listen(source)

    


    try:
        musicon("recognizing.mp3")
        print("Recognizing...")
        query = r.recognize_google(audio , language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        print(e)
        musicon("Error.mp3")
        print("Try again")
        return "None"

    return query

def sendemail(to , content):
    server = smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    with open("pass.txt" , "r") as f:
        p = f.read()
    server.login('jasnoorsingh11@gmail.com' , p)
    server.sendmail('jasnoorsingh11@gmail.com' , to , content)
    server.close()




if __name__ == "__main__":
    wishme()
    while True:
        
        query = take_command().lower()
        # Logic for executing task based on query
        if('what is your name' in query):
            print(f"My name is {name}. I am your personal assistant")
            speak(f"My name is {name}. I am your personal assistant")

        elif('change your name' in query):
            print(f"Sure!What do you want to call me?")
            speak(f"Sure!What do you want to call me?")
            b = take_command()
            name = b
            speak(f"You can call me {name} now")



        elif('hello' in query):
            print("Hello there , How may i help you")
            speak("Hello there , How may i help you")
        elif('wikipedia' in query):
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia" , "")
            results = wikipedia.summary(query , sentences= 2)
            speak("According to wikipedia")
            print(results)
            speak(results)


        elif('open youtube' in query):
            print("Opening Youtube")
            speak("Opening Youtube")
            webbrowser.open('https://www.youtube.com/')

        elif('open google' in query):
            print("Opening Google")
            speak("Opening Google")
            webbrowser.open('https://www.google.com/')

        elif('play music' in query):
            music = r'C:\Users\jasno\Music'
            songs = os.listdir(music)
            print(songs)
            a = len(songs)-1
            ran = (int(random.random()*a))
            os.startfile(os.path.join(music ,songs[ran]))

        elif('time' in query):
            strt = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Sir, Time is {strt}")
            speak(f"Sir, Time is {strt}")

        elif('open vs code' in query):
            print("Opening VS Code")
            speak("Opening VS Code")
            os.startfile(r"C:\Users\jasno\AppData\Local\Programs\Microsoft VS Code\Code.exe")

        elif('open fifa' in query):
            print("Opening FIFA")
            speak("Opening FIFA")
            os.startfile(r"C:\Program Files (x86)\FIFA19\FIFA19.exe")

        elif('send mail' in query):
            print("Whom do you want to send?")
            speak("Whom do you want to send?")
            to = take_command()
            to = to.replace(" " , "")
            print(to)
            print("What do you want to send?")
            speak("What do you want to send?")
            content = take_command()
            print(f"your message is: {content}")
            speak(f"your message is: {content}")
            print("Do you want to send it?")
            speak("Do you want to send it?")
            conf = take_command()
            if(conf == 'yes'):
                sendemail(to , content)
                print(f"Email has been sent to {to}")
                speak(f"Email has been sent to {to}")
            else:
                print("Your mail has been Cancelled")
                speak("Your mail has been Cancelled")

        
                





         
        # elif('bye' or 'stop' or 'exit' in query):
        #     print("Goodbye!")
        #     speak("Goodbye!")
        #     exit()
        time.sleep(1)