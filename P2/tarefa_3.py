import re

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]

while True:
    entrada = input()
    if entrada == "f":
        break
    # Verifica a formatação da entrada
    if not re.search("^\d+.\d{2}$", entrada):
        print("Input Inválido")
        continue
    total = float(entrada)

    print("NOTAS:")
    for nota in notas:
        qtd = total // nota
        total -= nota * qtd
        print("{0:.0f} nota(s) de R$ {1:.2f}".format(qtd, nota))

    print("\n"
          "MOEDAS:")
    for moeda in moedas:
        qtd = total // moeda
        total -= moeda * qtd
        print("{0:.0f} moeda(s) de R$ {1:.2f}".format(qtd, moeda))
