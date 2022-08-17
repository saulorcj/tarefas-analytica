import re

# Set possíveis deslocamentos
# possível deslocamento: (final_x - inicio_x, final_y - inicio_y)
possiv_deslc = {(-1, 2), (-2, 1), (-2, -1), (-1, -2),
                (1, -2), (2, -1), (2, 1), (1, 2)}
numero_by_letra = dict(zip("abcdefgh", range(1, 9)))

# Evita ter que compilar a expressão regular para toda string
regex = re.compile("^[a-h][1-8] [a-h][1-8]$")

while True:
    entrada = input()
    if entrada == "f":
        break
    # Verifica a formatação da entrada
    if not regex.search(entrada):
        print("Input Inválido")
        continue

    posicao1, posicao2 = ((numero_by_letra[posicao[0]], int(posicao[1]))
                          for posicao in entrada.split(" "))

    if (posicao2[0] - posicao1[0], posicao2[1] - posicao1[1]) in possiv_deslc:
        print("VÁLIDO")
    else:
        print("INVÁLIDO")

print("Fim...")
