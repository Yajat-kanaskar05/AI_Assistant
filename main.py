import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclib
import pyjokes

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):

    if "open youtube" in c.lower():
        speak("Opening Youtube")
        webbrowser.open("https://www.youtube.com")

    elif "open google" in c.lower():
        speak("Opening Google")
        webbrowser.open("https://www.google.com")

    elif "open stack overflow" in c.lower():
        speak("Opening Stack Overflow")
        webbrowser.open("https://www.stackoverflow.com")

    elif c.lower().startswith("play"):
        # Split the command and remove 'play', then join remaining words
        song = " ".join(c.lower().split(" ")[1:])
        link = musiclib.music[song]
        webbrowser.open(link)
    
    elif "tell a joke" in c.lower():
        joke = pyjokes.get_joke()
        print(joke)
        speak(joke)


if __name__ == "__main__": 
    speak("Initializing Jarvis")

    while True:
        r = sr.Recognizer()
        print("Recognizing...")
        try:

            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source , timeout=2 , phrase_time_limit=2)
            word = r.recognize_google(audio)

            if (word.lower() == "jarvis"):
                speak("How can I help you today?")

                with sr.Microphone() as source:
                    print("Listening...")
                    audio = r.listen(source , timeout=2 , phrase_time_limit=2)
                    command = r.recognize_google(audio)

                    process_command(command)
                
        except Exception as e:
            print("Error; {0}".format(e))
