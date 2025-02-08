b = []

for i in range (0, 3):
    a= int(input("Enter a number: "))
    b.append(a)
print("El numero mayor es {} y el numero menor es {}".format(max(b),min(b)))