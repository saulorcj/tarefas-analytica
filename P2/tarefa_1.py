import re

while True:
    horario = input()
    if re.search('^([0-1][0-9]|2[0-3]):[0-5][0-9]$', horario):
        horas, minutos = map(int, horario.split(":"))
    else:
        print("Input inválido")

    break
