import playsound
import  speech_recognition as sr
from gtts import gTTS
import random
from datetime import datetime
import webbrowser
import time
from email.mime import audio
from random import choice


r = sr.Recognizer()

def record(ask = False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice = ''
        try:
            voice = r.recognize_google(audio , language='tr-TR')
        except sr.UnknownValueError:
            speak('Sizi anlayamadım efendim')
        except sr.RequestError:
            speak('sistem çalışmıyor')
        return(voice)

def response(voice):
    if 'nasılsın' in voice:
        speak('İyiyim efendim. Siz nasılsınız')

    if 'Ben de iyiyim' in voice:
        speak('Sizin için ne yapabilirim efendim')

    if 'saat kaç' in voice or 'saati söyle' in voice:
        speak(datetime.now().strftime('%H:%M:%S'))

    if 'arama yap' in voice or 'Google' in voice:
        search = record('ne aramak istersiniz')
        url = 'https://google.com/search?q='+search
        webbrowser.get().open(url)
        print(search + 'için bulduklarım bunlar efendim')

    if 'tamamdır' in voice:
        speak('tekrardan görüşmek üzere efendim')
        exit()

    if 'espri yap' in voice:
        speak('Masada hangi örtü kullanılmaz. Bitki Örtüsü')

    if 'hey' in voice or 'hey jarvis' in voice:
        speak('Sizi dinliyorum')

    if 'ne haber' in voice:
        speak('iyiyim efendim')
        
    if 'Korku Hikayesi' in voice:
        speak('Bir hayalet varmış... Bir de başsız süvari... Birde ölü kedi... Birde tost makinesinden çıkan kız... Yoksa televizyondan mı çıkıyordu?')

    if 'espri' in voice:
        speak('Hangi macunla diş fırçalanmaz. Lahmacun')

    if 'ne vereceksin bana' in voice:
        speak('Ne veriyim abime?')

    if 'napıyorsun' in voice:
        speak('Sizi dinliyorum efendim')
        

def speak(yazı):
    tts = gTTS(text = yazı, lang= "tr")
    dosya_ismi = "ses"+ str(random.randint(0,10000000000000000000)) + ".mp3"
    tts.save(dosya_ismi)
    playsound.playsound(dosya_ismi)

speak('İyi günler efendim')

while 1:
    voice = record()
    print(voice)
    response(voice)