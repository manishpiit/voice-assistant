
import datetime

import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
Assistant = pyttsx3.init('sapi5')
voices = Assistant.getProperty('voices')
Assistant.setProperty('voice', voices[0].id)
rate = Assistant.getProperty('rate')
Assistant.setProperty('rate',150)
print(voices)


def speak(audio):
    print("  ")
    Assistant.say(audio)
    print("  ")
    Assistant.runAndWait()
speak('manish  i am jarvesh')

def sptext():
    recognizer=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            print("recognizing....")
            
            #print(data)
            
            query =  recognizer.recognize_google(audio,language='en-in')
            print(f"User said: {query}\n")
            speak(query)
       
        except Exception as e:
          return "None"
    return query 

query = sptext().lower()

if 'hello' in query:
    #name ="hello manish"
    speak("name class") 

elif 'open youtube' in query:
      webbrowser.open("https://www.youtube.com/") 

elif 'wikipedia' in query:
    speak('Searching Wikipedia...')  
    query = query.replace("wikipedia","")  
    results = wikipedia.summary(query,sentence=2)
    speak("According to wikipedia")
    print(results)
    speak(results)

elif 'open google' in query:
      webbrowser.open("https://www.google.co.in/")  


elif 'the time' in query:
    strTime = datetime.datetime.now().strftime("%H:%M:%S") 
    speak(f"Sir,time is {strTime}")
    

else:
       speak("no command found")





































