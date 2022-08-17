import re

notas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]

# Evita ter que compilar a expressão regular para toda string
regex = re.compile("^\d+.\d{2}$")

while True:
    entrada = input()
    if entrada == "f":
        break
    # Verifica a formatação da entrada
    if not regex.search(entrada):
        print("Input Inválido")
        continue
    # Transformo em int para evitar erros de arredondamento
    total = (float(entrada) * 100)

    print("NOTAS:")
    for nota in notas:
        qtd = total // (100 * nota)
        total -= nota * qtd * 100
        print("{0:.0f} nota(s) de R$ {1:.2f}".format(qtd, nota))

    print("\n"
          "MOEDAS:")
    for moeda in moedas:
        qtd = total // moeda
        total -= moeda * qtd
        print("{0:.0f} moeda(s) de R$ {1:.2f}".format(qtd, moeda / 100))
