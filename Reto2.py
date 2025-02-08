def nota_quices(codigo, nota1, nota2, nota3, nota4, nota5):  
    nota_r1 = (5 * nota1)/100
    nota_r2 = (5 * nota2)/100
    nota_r3 = (5 * nota3)/100
    nota_r4 = (5 * nota4)/100
    nota_r5 = (5 * nota5)/100   
    minimo = min(nota_r1, nota_r2, nota_r3, nota_r4, nota_r5)    
    prom = (nota_r1 + nota_r2 + nota_r3 + nota_r4 + nota_r5 - minimo)/4 
    redondear = round(prom, 2)    
    imprimir = ('El promedio ajustado del estudiante ' + codigo + ' es: ' + str(redondear))
    
    return imprimir



codigo = input("codigo: ")
nota1 = int(input("codigo"))
nota2 = int(input("codigo"))  
nota3 = int(input("codigo")) 
nota4 = int(input("codigo"))       
nota5 = int(input("codigo"))           
          
    


    
    









