import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import webbrowser



listener = sr.Recognizer()
engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def talk(text):
    print("Shiv:", text)
    engine.say(text)
    engine.runAndWait()


talk("Hello, I am Shiv. Your personal voice assistant is now active.")


def take_command():
    command = ""
    try:
        with sr.Microphone() as source:
            print('Listening... Say "Shiv"')
            listener.adjust_for_ambient_noise(source)
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'shiv' in command:
                command = command.replace('shiv', '').strip()
    except:
        print("Sorry, I didn't catch that.")
    return command


def run_shiv():
    command = take_command()
    print("Command:", command)

    if 'play' in command:
        song = command.replace('play', '')
        talk('Playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1)
        talk(info)

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'search' in command:
        query = command.replace('search', '')
        talk('Searching for ' + query)
        pywhatkit.search(query)

    elif 'open youtube' in command:
        talk("Opening YouTube")
        webbrowser.open("https://youtube.com")

    elif 'open google' in command:
        talk("Opening Google")
        webbrowser.open("https://google.com")

    elif 'shutdown' in command:
        talk('Shutting down the system')
        os.system('shutdown /s /t 1')

    elif 'restart' in command:
        talk('Restarting the system')
        os.system('shutdown /r /t 1')

    elif command != "":
        talk('Please say the command again.')


while True:
    run_shiv()
