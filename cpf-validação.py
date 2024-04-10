# Validação e geração de CPF.

# Primeiro dígito:
cpf1 = '74682489070'
nove_digitos = cpf1[:9]  # Range até o index 9, que não é incluído.
regressivo1 = 10  # Contagem regressiva 

resultado1 = 0 
for digito1 in nove_digitos:
    resultado1 += int(digito1) * regressivo1
    regressivo1 -= 1
digito1 = (resultado1 * 10) % 11
digito1 = digito1 if digito1 <= 9 else 0


# Segundo dígito:
cpf2 = f'{nove_digitos + str(digito1)}'
dez_digitos = cpf1[:10]
regressivo2 = 11

resultado2 = 0
for digito2 in dez_digitos:
    resultado2 += int(digito2) * regressivo2
    regressivo2 -= 1
digito2 = (resultado2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpf_calculo = f'{nove_digitos}{digito1}{digito2}'

if cpf1 == cpf_calculo:
    print(f"O CPF {cpf1} é válido.")
else:
    print("CPF inválido.")