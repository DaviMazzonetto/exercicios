# Faça um programa que peça uma nota, entre zero e dez.
#  Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

nota = int(input("Informe uma nota de 0 a 10: "))

while(nota > 10) or (nota < 0):
    nota = int(input("Valor inválido, informe um valor válido"))
print("valor válido")


def verifica(nota:int):
    if nota <= 10 and nota >= 0:
        return True
    else:
        return False

while(True):
    nota = int(input())

    if verifica(nota=nota):
        break


