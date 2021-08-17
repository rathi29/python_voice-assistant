from sys import path_importer_cache
import pyttsx3
import datetime
import speech_recognition as sp
import wikipedia
import pywhatkit as pwt
import webbrowser

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()





def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("good morning")
    elif hour>=12 and hour<18:
        speak("good evening")
    
    speak("I am tom sir. Please tell me how can i help you")

def takeCommand():
    r= sp.Recognizer()
    with sp.Microphone() as source:
        print("Listening.....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("trying...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("say it again...")
        return"None"
    return query

if __name__ == '__main__':
    wishMe()
    while True:
      query= takeCommand().lower()
      if 'wikipedia' in query:
          speak('searching wikipedia...')
          query=query.replace("wikipedia","")
          results =wikipedia.summary(query,sentences=5)
          speak("according to wiki")
          print(results)
          speak(results)
      elif "send message" in query:
          pwt.sendwhatmsg("+919406566445","hi",18,12)
      elif "open youtube" in query:
          webbrowser.open("youtube.com")
      elif "open google" in query:  
          webbrowser.open("google.com")
    
