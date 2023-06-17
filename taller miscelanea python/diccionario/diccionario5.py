print("palabras frecuentes")

def contar(texto):
    contador = {}
    word = texto.lower().split()

    for palabra in word:
        if palabra in contador:
            contador[palabra] += 1
        else:
            contador[palabra] = 1

    return contador

palabras = "hello hello HELLO java JAVA"
resultado = contar(palabras)
print(resultado)