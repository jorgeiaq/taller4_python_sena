print("contar elemntos repetidos")

def contar_ocurrencias(tupla):
    occurrences = {}
    for element in tupla:
        if element in occurrences:
              occurrences[element] += 1
        else:
              occurrences[element] = 1
    return occurrences

list = (1, 3, 3, 2, 4, 2, 5, 7, 6, 6, 9, 8)
result = contar_ocurrencias(list)

print("cuantas veces aparece una ocurrencia:", result)