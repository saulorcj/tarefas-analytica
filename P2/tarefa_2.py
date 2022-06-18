import re

possiv_deslc = {(-1, 2), (-2, 1), (-2, -1), (-1, -2),
                (1, -2), (2, -1), (2, 1), (1, 2)}
numero_by_letra = dict(zip("abcdefgh", range(1, 9)))

while True:
    entrada = input()
    if entrada == "f":
        break
    if not re.search("^[a-h][1-8] [a-h][1-8]$", entrada):
        print("Input Inválido")
        continue

    posicao1, posicao2 = entrada.split(" ")
    posicao1 = numero_by_letra[posicao1[0]], int(posicao1[1])
    posicao2 = numero_by_letra[posicao2[0]], int(posicao2[1])

    if (posicao2[0] - posicao1[0], posicao2[1] - posicao1[1]) in possiv_deslc:
        print("VÁLIDO")
    else:
        print("INVÁLIDO")

print("Fim...")
