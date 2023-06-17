print("numero mayor y minimo")

def tener_ma_mi(tupla):
  maximo = max(tupla)
  minimo = min(tupla)
  return maximo, minimo

list = (1, 2, 3, 4, 5, 6, 7)
maximo, minimo = tener_ma_mi(list)

print("el valor maximo es:", maximo)
print("el producto minimo es:", minimo)