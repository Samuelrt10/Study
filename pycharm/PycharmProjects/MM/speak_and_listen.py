from types import NoneType
import pyttsx3
import speech_recognition as sr
from winioctlcon import Unknown

engine = pyttsx3.init()
engine.setProperty("voice", "spanish")
engine.setProperty("rate", 175)
r = sr.Recognizer()

def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    while True:
        with sr.Microphone() as source:
            print("Escuchando...")
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio, language = "es_ES" )
                print("Has dicho: {}".format(text))
                return text
            except sr.UnknownValueError:
                print("lo siento, no he entendido")
                pass

if __name__ == "__main__":
    speak("Probando si funciona")
    listen()