print("separar elementos")

def chains(tupla):
    vowels = ("d", "e", "p")
    vowels_chains = []
    vowels_no_chains = []

    for chains in tupla:
      if chains[0].lower() in vowels:
          vowels_chains.append(chains)
      else:
          vowels_no_chains.append(chains)

    return tuple(vowels_chains), tuple(vowels_no_chains)

list = ("chat", "python", "java", "html", "objeto", "caballo")
vowels_chains, vowels_no_chains = chains(list)

print("la cadena que empieza con una vocal:", vowels_chains)
print("cadenas que no empiezan con una vocal:", vowels_no_chains)