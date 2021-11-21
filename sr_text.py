import speech_recognition as sr 
from playsound import playsound 

r = sr.Recognizer() 

with sr.Microphone() as source: 
    playsound("sounds/tv.mp3")
    audio = r.record(source, duration=3)
    playsound("sounds/tv.mp3")

    try:
        text = r.recognize_google(audio, language="th")
    except: 
        text = "ขออภัย"
    
    print(text)

    if(text == "ประตูระเบียง"):
        print("Yes!!")