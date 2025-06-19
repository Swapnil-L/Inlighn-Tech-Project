import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import subprocess

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

def speak(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good morning!")
    elif 12 <= hour < 18:
        speak("Good afternoon!")
    else:
        speak("Good evening!")
    speak("I am your voice assistant. How can I help you today?")

def takeCommand():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except Exception as e:
        print("Sorry, I did not understand. Please say that again.")
        return "None"
    return query.lower()

def runChatbot():
    wishMe()
    while True:
        query = takeCommand()

        if "wikipedia" in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif "open google" in query:
            speak("Opening Google")
            webbrowser.open("https://www.google.com")

        elif "open youtube" in query:
            speak("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "what is the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif "shutdown" in query:
            speak("Shutting down the system")
            os.system("shutdown /s /t 1")

        elif "restart" in query:
            speak("Restarting the system")
            os.system("shutdown /r /t 1")

        elif "exit" in query or "bye" in query:
            speak("Goodbye!")
            break

        elif "note" in query:
            speak("What should I write?")
            note = takeCommand()
            with open("note.txt", "w") as f:
                f.write(note)
            speak("Note saved.")

        else:
            speak("Sorry, I don't understand that command yet.")

if __name__ == "__main__":
    runChatbot()
