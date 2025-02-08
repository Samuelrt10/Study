from random import randint
import os

const_barra = 10

vida_ini_pika = 90
vida_ini_squirtle = 90
vida_pika = vida_ini_pika
vida_squirtle =  vida_ini_squirtle




print("Que inicie el combate!!")

while vida_pika > 0 and vida_squirtle > 0:
    ataque_pika = randint(1, 3)
    barra_pika = int(vida_pika * const_barra / vida_ini_pika)
    barra_sqrt = int(vida_squirtle * const_barra / vida_ini_squirtle)
    print("turno de pikachu")
    if ataque_pika == 1:
        print("Pikachu usó bola voltio")
        vida_squirtle -= 12
        input("Presiona enter para continuar...")
        os.system("cls")
    elif ataque_pika == 2:
        print("Pikachu usó trueno")
        vida_squirtle -= 15
        input("Presiona enter para continuar...")
        os.system("cls")
    else:
        print("Pikachu no atacó")

    barra_sqrt = int(vida_squirtle * const_barra / vida_ini_squirtle)

    if vida_squirtle <0:
        vida_squirtle = 0

    print("Vida Squirtle [{}{}] ({}/{})".format("*" * barra_sqrt, " " * (const_barra - barra_sqrt), vida_squirtle,
                                                vida_ini_squirtle))
    print("Vida Pikachu [{}{}] ({}/{})".format("*" * barra_pika, " " * (const_barra - barra_pika), vida_pika,
                                               vida_ini_pika))

    if vida_squirtle <= 0:
        break

    print("Turno Squirtle")

    opciones_ata= ["A","B", "C", "D", "x"]
    ataque_sqrt = None
    while ataque_sqrt not in opciones_ata:
        ataque_sqrt= input("Que ataque deseas usar: [A]Placaje, [B]Burbuja, [C]Agua, [x]No atacar")
        if ataque_sqrt == "A":
            vida_pika -= 11
            print("Squirtle uso Placaje ")
            input("Presiona enter para continuar...")
            os.system("cls")
        elif ataque_sqrt == "B":
            vida_pika -= 12
            print("Squirtle uso Burbuja ")
            input("Presiona enter para continuar...")
            os.system("cls")
        elif ataque_sqrt == "C":
            vida_pika -= 15
            print("Squirtle uso Agua ")
            input("Presiona enter para continuar...")
            os.system("cls")
        else:
            print("Squirtle no atacó")
            input("Presiona enter para continuar...")

    barra_pika = int(vida_pika * const_barra / vida_ini_pika)

    if vida_pika <0:
        vida_pika = 0

    print("Vida Squirtle [{}{}] ({}/{})".format("*" * barra_sqrt, " " * (const_barra - barra_sqrt), vida_squirtle, vida_ini_squirtle))
    print("Vida Pikachu [{}{}] ({}/{})".format("*" * barra_pika, " " * (const_barra - barra_pika), vida_pika, vida_ini_pika))

if vida_squirtle > vida_pika:
    print("Gana Squirtle")
    print("...")
else:
    print ("Gana Pikachu")
    print("...")


