print("suma de numeros de una lista")
def suma_numeros(lista):
    suma = sum(lista)
    return suma


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20]
result = suma_numeros(numbers)
print("la suma de todos los numeros de la lista es:", result)