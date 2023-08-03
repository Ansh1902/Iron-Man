import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import os
import webbrowser
import smtplib
engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('anshk2002.ak@gmail.com', 'ansh1902')
    server.sendmail('anshk2002.ak@gmail.com')
    server.close()
def WishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<=18: 
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")    
     
    speak("My name is Iron Man. Tell me how may I help you?")

def takeCommand():
    #takes mic input from user and returns string output
    
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening..")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User Said: {query}\n")

    except Exception as e:
        print(e)

        print("I couldn't understand what you meant by that.")
        return "None"
    return query

if __name__ == "__main__":
    WishMe()
    if 1:
   
        query = takeCommand().lower()

        if 'wikipedia' in query:
            print("Searching Wikipedia...")
            query = query.replace("wikipedia","")
            results= wikipedia.summary(query, sentences=2)
            speak("According to wikipedia!")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            
        elif 'open coding' in query:
            webbrowser.open("codingninjas.com")
        
        elif 'open leetcode' in query:
            webbrowser.open("Leetcode.com")
        


        elif 'play sidhu moose wala' in query:
            webbrowser.open("https://music.youtube.com/watch?v=3BRcwbq8x50&feature=share")

        elif 'play karan aujla' in query:
            webbrowser.open("https://music.youtube.com/watch?v=tMgEYaclnQ0&feature=share")    

        elif 'time' in query:
            strTime= datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")  

        elif 'open code' in query:
            codePath = "C:\\Users\\ANSH\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email ' in query:
            try:
                speak("What should I say?")
                content=takeCommand()
                to="anshabc9@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                speak("I cannot send the email right now.")  