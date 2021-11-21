import speech_recognition as sr 
from gtts import gTTS 
from playsound import playsound 
from datetime import datetime

r = sr.Recognizer() 

with sr.Microphone() as source: 
    playsound("sounds/tv.mp3")
    audio = r.record(source, duration=5)
    playsound("sounds/tv.mp3")

    try: 
        text = r.recognize_google(audio, language="th")

        if "ผม" in text: 
            text = text.replace("ผม","ฉันเองก็")
        if "ครับ" in text:
            text = text.replace("ครับ","ค่ะ")

        if text == "กี่โมงแล้ว": 
            now = datetime.now() 
            text = now.strftime("ขณะนี้เวลา%Hนาฟิกา%Mนาที%Sวินาที")
            
    except: 
        text = "ขออภัย พูดให้มันรู้เรื่องหน่อยสิ"
    
    tts = gTTS(text, lang="th")
    tts.save("sounds/answer.mp3")
    
    playsound("sounds/answer.mp3")