print("buscar indices")

def indices(tupla, elemento):
  indices = []
  for i in range(len(tupla)):
    if tupla[i] == elemento:
      indices.append(i)
  return indices

list = (1, 2, 3, 4, 3, 5, 5, 6, 2)
mi_element = 2
result = indices(list, mi_element)
print(result)