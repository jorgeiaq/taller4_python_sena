print("combinar diccionarios")

def combinar_diccionarios(diccionario1, diccionario2):
    diccionario_combinado = {}

    for clave, valor in diccionario1.items():
        if clave in diccionario2:
           diccionario_combinado[clave] = valor + diccionario2[clave]
        else:
            diccionario_combinado[clave] = valor

    for clave, valor in diccionario2.items():
        if clave not in diccionario1:
           diccionario_combinado[clave] = valor
          
    return diccionario_combinado

diccionario1 = {"A": 1, "B": 2, "C": 3}
diccionario2 = {"B": 3, "C": 4, "D": 5}

resultado = combinar_diccionarios(diccionario1, diccionario2)
print(resultado)