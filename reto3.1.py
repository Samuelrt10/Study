def Seleccion(info:dict):

    h1 = info.keys()
    h2 = list(h1)
    h3 = len(h2)

    lista_notas = []
    creditos_lista = []
    suma_notas = 0
    suma_creditos = 0
    nombre_notas = {}
    estudiante1 = []


    for i in range(0, h3):

        p = h2[i]
        h4 = len( info[p]["materias"])
        for i in range(0, h4):

            if info[p]["materias"][i]["retirada"] == "No" :

                creditos = info[p]["materias"][i]["creditos"]
                notas = info[p]["materias"][i]["nota"]
                nota_credito =(notas) * (creditos)
                lista_notas.append(nota_credito)
                creditos_lista.append(creditos)
            elif info[p]["materias"][i]["retirada"] == "Si":
                continue

        for nota in lista_notas:
            suma_notas += nota

        for credito in creditos_lista:
            suma_creditos += credito

        for i in range(0, 1):
            if suma_creditos >= 1:
                promedio_ponderado = suma_notas / suma_creditos
                nota_total = round(promedio_ponderado, 2)
                nombre_notas[f"{p}"] = nota_total
                lista_notas.clear()
                creditos_lista.clear()
                suma_notas = 0
                suma_creditos = 0
            elif suma_creditos < 1:
                promedio_ponderado = suma_notas / 1
                nota_total = round(promedio_ponderado, 2)
                nombre_notas[f"{p}"] = nota_total
                lista_notas.clear()
                creditos_lista.clear()
                suma_notas = 0
                suma_creditos = 0

    for i in range(0, h3):

        j = 1
        l = nombre_notas
        llaves_finales = l.keys()
        valores_finales = l.values()
        llaves_finales_2 = list(llaves_finales)
        valores_finales = list(valores_finales)
        persona = llaves_finales_2[i]
        persona_ = str(persona)
        nota_maxima = max(valores_finales)
        if l[persona_] == nota_maxima :
            estudiante1.append(persona_)


        elif  l[persona_] != nota_maxima :
           continue


        j = j+1

    for i in info:
        estudiantemin = min(estudiante1)
        estudiante = [estudiantemin, nota_maxima]
        nombre_est = info[int(estudiante[0])]["nombres"]
        apellidos_est = info[int(estudiante[0])]["apellidos"]
        documento_est = info[int(estudiante[0])]["documento"]
        programa_est = info[int(estudiante[0])]["programa"]
        nota_est = estudiante[1]
        codigo_est = int(estudiante[0])
    espacio = nombre_est.find(" ")
    espacioap = apellidos_est.find(" ")
    espacio2 = " "
    docu = str(documento_est)
    docu_l = len(docu)

    while espacio2 in apellidos_est:
        apellido = apellidos_est[0 : espacioap]

        break
    else:
        apellido = apellidos_est




    while espacio2 in nombre_est:
        correo = nombre_est[0]+ nombre_est[espacio+1] + "."+ apellido + docu[docu_l-2] + docu[docu_l-1]
        break
    else:
        correo = nombre_est[0]+ apellido + docu[docu_l-2] + docu[docu_l-1]

    correo = correo.lower()

    while "á" or "é" or "í" or "ó" or "ú" in correo:
        correo.replace("á" , "a")
        correo.replace("é" , "e")
        correo.replace("í" , "i")
        correo.replace("ó" , "o")
        correo.replace("ú" , "u")
        break


    final = [codigo_est, nombre_est, apellidos_est, documento_est, programa_est, nota_est, correo]




    return final

diccionario = { 67891:{"nombres" : "Samuel",
                        "apellidos": "Rubio T",
                        "documento" : 1031805413,
                        "programa" : "MEC",
                        "materias" : [{"facultad" : "Ingenieria",
                                       "codigo" : "pro",
                                       "nota" : 5.00,
                                       "creditos" :1,
                                       "retirada" : "No"},

                                      {"facultad" : "Ingenieria",
                                       "codigo" : "fisica",
                                       "nota" : 3.70,
                                       "creditos" : 4,
                                       "retirada" : "No"},

                                        {"facultad" : "Ingenieria",
                                       "codigo" : "materiales",
                                       "nota" : 3.00,
                                       "creditos" : 3,
                                       "retirada" : "No"},

                                        {"facultad" : "Ingenieria",
                                       "codigo" : "progra",
                                       "nota" : 3.50,
                                       "creditos" :3,
                                       "retirada" : "No"},

                                        {"facultad" : "Ingenieria",
                                       "codigo" : "calculo",
                                       "nota" : 2.80,
                                       "creditos" : 4,
                                       "retirada" : "No"},

                                        {"facultad" : "Ingenieria",
                                       "codigo" : "algebra",
                                       "nota" : 3.60,
                                       "creditos" : 3,
                                       "retirada" : "No"},

                                      

                                      ]
                      },
               

               }






funcion = Seleccion(diccionario)
print(funcion)
