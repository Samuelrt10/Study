verificador = None
lista = []

while True:
    art = input("Que desea comprar?? [Q] para salir: ")
    if art == 'Q':
        break
    else:
        comprobacion = input("seguro que desea agregar {} a la lista?? (S/N): ".format(art))
        if comprobacion == 'S':
            art.upper()
            lista.append(art)
        else:
            art= None

if len(lista) == 0:
    print("No se agrgaron articulos a la lista")
else:
    print(lista)