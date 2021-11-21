import speech_recognition as sr 
from gtts import gTTS 
from playsound import playsound 

r = sr.Recognizer() 

with sr.Microphone() as source: 
    playsound("sounds/tv.mp3")
    audio = r.record(source, duration=5)
    playsound("sounds/tv.mp3")

    try: 
        text = r.recognize_google(audio, language="th")
    except: 
        text = "ขออภัย พูดให้มันรู้เรื่องหน่อยสิ"
    
    tts = gTTS(text, lang="th")
    tts.save("sounds/answer.mp3")
    
    playsound("sounds/answer.mp3")