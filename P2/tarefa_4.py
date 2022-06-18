from collections import defaultdict
import re

freq_by_numero = defaultdict(int)

numero = input()
while numero != "f":
    # Verifica a formatação da entrada
    if re.search("^\d+$", numero):
        freq_by_numero[numero] += 1
    numero = input()

# Itera o dicionário de forma ordenada
for numero in sorted(freq_by_numero):
    frequencia = freq_by_numero[numero]
    print("O número {0} apareceu {1} {2}".format(numero,
                                                 frequencia,
                                                 "vez" if frequencia == 1 else "vezes"))

print("Fim...")
