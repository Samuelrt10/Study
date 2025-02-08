# Pedir Valores
# Ganados, perdidos, empatados.
# Multiplicar los ganados por 3
# El resutado de los ganados mas los empatados
# Imprimir el resultado

win = int(input("Partidos Ganados: "))
lose = int(input("Partidos Perdidos: "))
tie = int(input("Partidos Empatados: "))

total = ((win * 3) + tie )

print ("los puntos del equipo son", total)
