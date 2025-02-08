import re
from time import sleep
from speak_and_listen import speak, listen

def indentify_name(text):
    nombre = None
    cases = ["me llamo ([A-Za-záéíóú]+)", "mi nombre es ([A-Za-záéíóú]+)", "^([A-Za-záéíóú]+)$"]
    for case in cases:
        i = 0
        try:
            nombre = re.findall(case, text)[0]
        except IndexError:
            pass
    return nombre

def filtro(name, clave, finish):
    if clave != name and name != finish:
        return True
    else:
        return False

def say_name_and_bye(bool, name, clave):
    if bool:
        say = "Hola, {}".format(name)
        print(say)
        speak(say)

    elif bool == False and name == clave:
        cont = 3
        speak("oh, haz usado la palabra prohibida, me voy a autodestruir en:")
        for i in range(3):
            speak("{}".format(cont))
            cont -=1
        speak("BOOOOOOOOOOOOOOOOM, adiosito")

    else:
        speak("adios para ti tambien")


def main():
    speak("hola, como estás?, como te llamas?")
    clave = "taco"
    finish = "adiós"
    confirm = True
    while confirm:
        text = listen()
        text_low = text.lower()
        name = indentify_name(text_low)
        confirm = filtro(name, clave,finish)
        say_name_and_bye(confirm, name, clave)


if __name__ == "__main__":
    main()