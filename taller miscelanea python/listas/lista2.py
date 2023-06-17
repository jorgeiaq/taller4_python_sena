print("promedio de numeros de la lista")
def average_value(lista):
  addition = sum(lista)
  average = len(lista)
  converter =  addition / average
  return converter
  
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
resultd = average_value(number)
print("el promedio de los numeros es:", resultd)