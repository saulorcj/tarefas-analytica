import re

# Evita ter que compilar a expressão regular para toda string
regex = re.compile('^([0-1][0-9]|2[0-3]):[0-5][0-9]$')

while True:
    entrada = input()
    if entrada == "f":
        break
    # Verifica a formatação da entrada
    if not regex.search(entrada):
        print("Input inválido")
        continue
    horas, minutos = map(int, entrada.split(":"))

    # Converte para ângulos
    horas = (horas % 12) * 30
    minutos *= 6

    # Ordena os ângulos
    maior_ang, menor_ang = (horas, minutos) if horas > minutos else (minutos, horas)

    # Verifica qual dos dois graus entre eles é o menor
    grau_min = min(360 - maior_ang + menor_ang, maior_ang - menor_ang)

    print("O menor ângulo é de {0}º".format(grau_min))

print("Fim...")