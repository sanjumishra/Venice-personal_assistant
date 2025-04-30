import time
import pyttsx3
import speech_recognition as sr
import eel
import pywhatkit as kit
import webbrowser
import wikipedia

def speak(text):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    #print(voices)
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170)
    eel.DisplayMessage(text)
    engine.say(text)
    engine.runAndWait()

@eel.expose
def takeCommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening...')
        eel.DisplayMessage('Listening...')
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source, timeout=10, phrase_time_limit=6)
    
    try:
        print('Recognizing...')
        eel.DisplayMessage('Recognizing...')
        query = r.recognize_google(audio, language='en')
        print(f'User said: {query}')
        #speak(query)
        time.sleep(2)
        eel.DisplayMessage(query)
        
        

    except Exception as e:
        return ""
    
    return query.lower()

# text = takeCommand()

# speak(text)
@eel.expose
def allCommands(message=1):

    if message == 1:
        query = takeCommand()
        print(query)
        
    else:
        query = message
        
    try:

        if "open" in query:
            site = query.split("open")[-1].strip()
            url = f"https://{site}.com"
            speak(f"Opening {site}")
            webbrowser.open(url)

        elif "hello" in query:
            speak("Hi Sanju , How are you? ")

        elif "fine"in query:
            speak("Wish you a good day!")
            
        # if play in the query ,play songs on youtube :
        elif "play" in query:
            song=query.split("play")[-1].strip()
            speak(f"playing{song} on youtube")
            kit.playonyt(song)

        # If the query contains "wikipedia", try to search for the topic on wikipedia and speak the answer:
        elif "" in query:
            topic = query.split("wikipedia")[-1].strip()
            speak(f"Searching for {topic} on the web")
            try:
                summary = wikipedia.summary(topic, sentences=2)
                speak(f"According to the web, {summary}")
            except:
                speak(f"Sorry, I could not find any information on {topic} ")

        # If "thanks" in the query,exit the program
        elif "Thank you" in query:
            speak("Happy to help you!")
            exit()

        # Respond with this if nothing found correct:
        else:
            speak("Sorry,i do not understand that")
    except:
        print("something is wrong")

    eel.ShowHood()

    