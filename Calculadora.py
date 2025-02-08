def calculadora(numero1, numero2, operacion):
    
    if operacion == "+":
        suma = numero1 + numero2
        return suma
    elif operacion  == "-":
        resta = numero1 - numero2
        return resta 
    elif operacion  == "/":
        dividir = numero1 / numero2
        return dividir
    elif operacion  == "*":
        multiplicar = numero1 * numero2
        return multiplicar 
    else:
        print("No usaste las operaciones difinadas :(")
                

numero1 = int(input("ingrasa el numero 1: "))
operacion = input("ingresa la operacion: ")
numero2 = int(input("ingresa el numero 2: "))


calculator = calculadora(numero1, numero2, operacion)
print("El resultado es: ", calculator)
