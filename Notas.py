cmaterias= int(input("Ingrese la cantidad de materias: "))
mat = []
creditos = []
notas = []
suma = 0
sumap = 0
for i in range(cmaterias):
    mat.append(str(input("nombre de la materia ")))
    creditos.append(int(input("creditos de la materia ")))
    notas.append(float(input("notas de la materia ")))

for i in range(cmaterias):
    suma += creditos[i]
    sumap += notas[i] * creditos[i]
resultado = sumap/suma
print(resultado)
