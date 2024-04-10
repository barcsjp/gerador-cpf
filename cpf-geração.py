import random
import sys

nove_digitos = ''
for i in range(9):
    nove_digitos += str(random.randint(0, 9)) 

regressivo1 = 10  
resultado1 = 0 
for digito1 in nove_digitos:
    resultado1 += int(digito1) * regressivo1
    regressivo1 -= 1
digito1 = (resultado1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0


dez_digitos = f'{nove_digitos + str(digito1)}'
regressivo2 = 11

resultado2 = 0
for digito2 in dez_digitos:
    resultado2 += int(digito2) * regressivo2
    regressivo2 -= 1
digito2 = (resultado2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpf_calculo = f'{nove_digitos}{digito1}{digito2}'

print(cpf_calculo)
