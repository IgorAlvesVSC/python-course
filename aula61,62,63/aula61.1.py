import re
import sys



entrada = input('CPF: ')
cpf_enviado_user = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_e_sequencial = entrada == entrada[0] * len(entrada)

if entrada_e_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_user[:9]
contador_regressivo_1 = 10

resultado_digito_1 = 0
for digito in nove_digitos:
    resultado_digito_1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito_1 * 10) % 11
digito_1 = digito_1 if digito_1 <= 9 else 0

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito2 = (resultado_digito_2 * 10) % 11
digito2 = digito2 if digito2 <= 9 else 0

cpf_gerado_pelo_calc = f'{nove_digitos}{digito_1}{digito2}'

if cpf_enviado_user == cpf_gerado_pelo_calc:
    print(f'{cpf_enviado_user} é válido')
else:
    print('CPF inválido')