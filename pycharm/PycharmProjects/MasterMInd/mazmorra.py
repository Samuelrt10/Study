import random

print("Estás atrapado en un celda por un crimen que no cometiste :(\n")
print("luego de tres largas noches se presenta una oportundad que no podias perder\n")
print("Un guardia se vuelve loco y deja salir a los 3 prisioneros que estan en dicha carcel\n")
print("Tu no te fias del todo del guardia y prefieres tomarte un momento para pensar si debes seguir al guardia o quedarte en la celda\n")
salir = input("Decides salir (S/N)\n")

if salir == "S":
    print("decides salir y seguir al guardia a un cuarto oscuro junto con los otros prisioneros\n")
    print("El guardia les dice que va a dejar escapar a quienes resulevan el siguiente problema\n")
    pregunta1 = random.randint(1, 10)
    pregunta2 = random.randint(1, 10)
    respuesta = pregunta1 * pregunta2 - 1
    res_usuario = int(input("La pregunta es cuanto es {} X {} - 1 = ". format(pregunta1, pregunta2)))

    if respuesta == res_usuario:
        print("Felicidades haz logrado dar la respuesta correcta\n")
        print("Ahora elige un arma con la que podras escapar")
        arma_elegida = input("Que arma quieres: A) Pistola B) Banano C) Eres un valiente o estupido y eliges no tomar ninguna \n")
        print("Es una interesante elección, espero te sea util\n")
        print("El guardia te lleva a otra sala, la cual tiene una puerta enorme\n")

        if arma_elegida == "A":

            print("De esta puerta sale un enorme gorila, aunque no quieras deberas disparar para sobrevivir\n")
            print("Oops! La pistola es de agua, el gorila te golpea y mueres al instante\n")
            print("GAME OVER!")
            input("...")

        elif arma_elegida == "B":

            print("De esta puerta sale un enorme gorila, corre hacia ti de manera agresiva\n")
            print("Tu unico reflejo es tirar el banano a su cabeza, esta accion hizo que el gorila te amara por darle de comer")
            print("El guardia al ver esto te felicita, y te libera")
            print("Felicidades, GANASTE!")
            input("...")

        elif arma_elegida == "C":

            print("De esta puerta sale un enorme gorila, corre hacia ti de manera agresiva\n")
            print("Parece que si eres estupido, el gorila de un golpe te mando al otro mundo :(\n")
            print("GAME OVER!")
            input("...")

        else:
            print("Eres mas tonto de lo que creía, por lastima terminemos la historia.\n")
            print("Felicidades, GANASTE!")
            input("...")

    else:
        print("Pues lamento informar que la respuesta es incorrecta\n")
        print("Regresa a tu celda\n")
        print("Al no aprovechar tu opotunidad pasas el resto de tu vida encerrado\n")
        print("GAME OVER!")
        input("...")
elif salir == "N":
    print("Decides quedarte y esperar otra forma de salir\n")
    print("Al no aprovechar tu opotunidad pasas el resto de tu vida encerrado\n")
    print("GAME OVER!")
    input("...")

else:
    print("Bro si no vas a seguir instrucciones no juegues :(")
    input("...")