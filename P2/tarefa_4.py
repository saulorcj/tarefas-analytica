from collections import defaultdict
import re

# Dicionário frequência por número
# Se a chave não existir, ele a cria ligada a um inteiro com valor zero
# Evita ter que criar um if só para saber se a chave existe e realiza somente uma busca no HashMap
freq_by_numero = defaultdict(int)

# Evita ter que compilar a expressão regular para toda string
regex = re.compile("^\d+$")

numero = input()
while numero != "f":
    # Verifica a formatação da entrada
    if regex.search(numero):
        freq_by_numero[int(numero)] += 1
    numero = input()

# Itera o dicionário de forma ordenada
for numero in freq_by_numero:
    frequencia = freq_by_numero[numero]
    print("O número {0} apareceu {1} {2}".format(numero,
                                                 frequencia,
                                                 "vez" if frequencia == 1 else "vezes"))

print("Fim...")
