print("contar palabras")

def count(lista_palabras):
   contador = {}
   for word in lista_palabras:
     if word in contador:
         contador[word] += 1
     else:
         contador[word] = 1
   return contador

lista = ["hello", "java", "java", "java", "php", "php"]
result = count(lista)
print("la cuenta de las palabras es:", result)