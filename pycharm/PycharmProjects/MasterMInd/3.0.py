import random
h = 1
N= random.randint(1,10)

print("intenta adivinar el numero secreto  entre 1 - 10")

for i in range(10):
    I= int(input("digite un numero: "))
    if I==N:
        print("Ganaste, el numero secreto es: ", I)
        break
    else:
        print("Sigue intentando ")