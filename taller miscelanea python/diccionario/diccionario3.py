print("filtrar")

def filtro(diccionario, valor):
    value = {}
    for llave, val in diccionario.items():
        if val == valor:
           value[llave] = val
    return value

diccionario = {"A": 2, "B": 2, "Z": 3, "X": 4, "M": 4}
valor = 4

resultado = filtro(diccionario, valor)
print(resultado)