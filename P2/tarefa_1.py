import re

while True:
    horario = input()
    if horario == "f":
        break
    if not re.search('^([0-1][0-9]|2[0-3]):[0-5][0-9]$', horario):
        print("Input inválido")
        continue
    horas, minutos = map(int, horario.split(":"))

    # Formatando como ângulos
    horas = (horas % 12) * 30
    minutos *= 6

    # ordena os ângulos
    maior_ang, menor_ang = (horas, minutos) if horas > minutos else (minutos, horas)

    # Verifica qual dos dois graus entre eles é o menor
    grau_min = min(360 - maior_ang + menor_ang, maior_ang - menor_ang)

    print("O menor ângulo é de {0}º".format(grau_min))
