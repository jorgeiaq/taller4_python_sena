print("palabra mas larga")
def long_word(lista):
    word = max(lista, key=len)
    return word

word_list = ["hola", "adios", "banana", "hey", "cun", "odioso"]
word = long_word(word_list)
print("la palabra mas larga es:", word)