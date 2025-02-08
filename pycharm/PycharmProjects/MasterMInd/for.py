"""

texto_usuario = input("Ingrese el texto que desea usar: ")
espacios = 0
puntos = 0
comas = 0

rango = len(texto_usuario)

for i in range (0, rango):
    if texto_usuario[i] == " ":
        espacios += 1
    elif texto_usuario[i] == ",":
        comas += 1
    elif texto_usuario[i] == ".":
        puntos += 1
    else:
        pass

print("Espacios: ", espacios)
print("Puntos: ", puntos)
print("Comas: ", comas)


import string

texto_usuario = input("Ingrese el texto que desea usar: ")
mayus = 0

for letra in texto_usuario:
    if letra in string.ascii_uppercase:
        mayus += 1


print("Mayus: ", mayus)

"""

tabla = int(input("Ingrese la tabla que desea saber: "))

for i in range(1,11):
    resultado = tabla*(i)
    if resultado % 2 == 0:
        print(tabla," X ", i ," = ", resultado)
