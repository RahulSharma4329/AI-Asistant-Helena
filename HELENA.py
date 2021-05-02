import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import smtplib
import datetime
import wikipedia
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

# pip install -Iv pyttsx3==2.6 -U

option = Options()
option.binary_location = "D:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"

print("initialising Hellena")

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 150)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")

    elif hour >= 12 and hour < 18:
        speak("Good afternoon")

    else:
        speak("Good evening")

    speak("I am Hellena , How can i help you ?")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        print("recognising")
        query = r.recognize_google(audio, language='en-in')
        print("user said: " + query + "\n")

    except Exception as e:
        print(e)
        print("say that again please...")
        return "None"
    return query


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("searching in wikipedia..")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            speak("opening Youtube")
            print("opening Youtube")
            webbrowser.open("https://www.youtube.com/")

        elif 'open google' in query:
            speak("opening Google")
            print("opening Google")
            webbrowser.open("https://www.google.co.in/")

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak("Sir the time is " + strtime)
            print("Sir the time is " + strtime)

        
        elif 'email' in query:
            try:

                speak("who should i send it to")
                recipient = take_command().lower()
                speak("what should im say")
                content = take_command()
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('guitarfreaks1423@gmail.com', '8092434459')
                if "Rahul" in recipient:
                    mail.sendmail('guitarfreaks1423@gmail.com', 'rahulsharma4329@gmail.com', content)
                mail.close()
                speak("Email sent")

            except Exception as e:
                print(e)
                speak("the email can not be sent, i am very sorry")

        elif 'search in google about' in query:
            search_element = query.replace('search in google about', '')
            speak("searching ")
            driver = webdriver.Chrome(chrome_options=option)
            driver.get('https://google.co.in')
            searchbox = driver.find_element_by_xpath('//*[@id="tsf"]/div[2]/div[1]/div[1]/div/div[2]/input')
            searchbox.send_keys(search_element)
            searchbox.send_keys(Keys.ENTER)



        elif 'search in youtube about' in query:
            search_element = query.replace('search in youtube about', '')
            speak("searching ")
            driver = webdriver.Chrome(chrome_options=option)
            driver.get('https://youtube.com')
            driver.find_element_by_xpath('//*[@id="container"]').click()
            searchbox = driver.find_element_by_xpath(
                '/html/body/ytd-app/div/div/ytd-masthead/div[3]/div[2]/ytd-searchbox/form/div/div[1]/input')
            searchbox.send_keys(search_element)
            searchbox.send_keys(Keys.ENTER)
            selectionbox = driver.find_element_by_xpath('//*[@id="video-title"]')
            selectionbox.click()

        elif 'quit' in query:
            speak("happy to help, quitting ")
            exit()
