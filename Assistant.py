import os
# print(os.listdir())
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)                                              #to know the voices in pc
engine.setProperty('voices', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening")
    speak("I am your personal Assistant, How can I help you, Rohit")

def takeCommand():
    # It takes microphone input from user    
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language ='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        speak(" dear rohit, It seems like your internet connection is lost, check your lan connection or internet connection for better results, I am unable to process your request, I beg you for pardon ")
        print("""
                     .-''''''''''''''-.            o   o   o
                    :   O         O    :        o             
                    :   .   .V.   .    :         o  
                    :    ' . . . '     :            o   o   o          o o       o ooo   o ooo   o    o
                     '-..............-'                        o     o     o     oo      oo       o  o
                                                              o      o     o     o       o         o
                                                   o   o   o           o o       o       o        o
                                                                                                 o         """)

        quit()
        # print("Say that again, Please!...")
        
    return query

if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()
        
        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query = query.replace('wikipedia', "")
            results = wikipedia.summary(query, sentences = 2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
            quit()
            
        elif 'open google' in query:
            webbrowser.open("google.com")
            quit()
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

            quit()
            
        elif 'play music' in query:
            music_dir = "C:\\Users\\Admin\\OneDrive\\Desktop\\Voice Assistant\\songs"
            songs = os.listdir(music_dir)
            randNo = random.randint(0, 14)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[randNo ]))

            quit()


            
            

    

# from playsound import playsound


# playsound('D:\\movies\\New folder\\All.of.Us.Are.Dead.S01E07.(NKIRI.COM).niovnfodnvoinodfnvondoibngoinbfoigbfgil.mkv')
