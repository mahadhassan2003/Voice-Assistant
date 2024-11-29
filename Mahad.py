import speech_recognition as sr
import webbrowser
import os
import pyttsx3
import time  

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def listen_to_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        print("Recognizing your command...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}")
        return command.lower()
    except sr.UnknownValueError:
        speak("Sorry, I could not understand the audio.")
        print("Sorry, I could not understand the audio.")
        return ""
    except sr.RequestError:
        speak("Sorry, there was a problem with the recognition service.")
        print("Sorry, there was a problem with the recognition service.")
        return ""

def mahad():
   
    speak("Hi, Mahad!")
    print("HI, Mahad!")
    time.sleep(2) 
    speak("My name is Alex. What can I do for you?")
    print("My name is Alex. What can I do for you?")
    
    while True:  
        command = listen_to_command()

        if "open facebook" in command:
            speak("Opening Facebook... please wait.")
            print("Opening Facebook... please wait.")
            webbrowser.open("https://www.facebook.com")
            break
        elif "open whatsapp" in command:
            speak("Opening WhatsApp... please wait.")
            print("Opening WhatsApp... please wait.")
            webbrowser.open("https://web.whatsapp.com")
            break
        elif "open youtube" in command:
            speak("Opening YouTube... please wait.")
            print("Opening YouTube... please wait.")
            webbrowser.open("https://www.youtube.com")
            break
        elif "play jo tum mere ho" in command:
            speak("Opening the song... please wait.")
            print("Opening the song... please wait.")
            webbrowser.open("https://youtu.be/ilNt2bikxDI?si=HUkEBsWFdvkmGYvq")
            break
        elif "open disk d" in command:
            speak("Opening disk D... please wait.")
            print("Opening disk D... please wait.")
            os.startfile("D:\\")
            break
        elif "open favourite folder" in command:
            speak("Opening favourite folder... please wait.")
            print("Opening favourite folder... please wait.")
            os.startfile("D:\\Scrapbook\\favourite")
            break
        elif "open group photos" in command:
            speak("Opening group photos... please wait.")
            print("Opening group photos... please wait.")
            os.startfile("D:\\Scrapbook\\Group Photos")
            break
        else:
            speak("Sorry, I didn't understand that. Could you please say the command again?")
            print("Sorry, I didn't understand that. Could you please say the command again?")

mahad()
