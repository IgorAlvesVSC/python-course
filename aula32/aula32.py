"""
entrada = input ('Digite um número: ')

if entrada.isdigit():
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    if par_impar is True:
        par_impar_texto = 'par'
    elif par_impar is False:
            par_impar_texto = 'ímpar'

    print(f'O número {entrada_int} é {par_impar_texto}')
else:
    print('Você não digitou um número inteiro')
"""

"""
entrada = input('Digite a hora em números inteiros: ')

try:
    hora = int(entrada)

    if hora >= 0 and hora <= 11:
        print('Bom dia!')
    elif hora >= 12 and hora <= 17:
        print('Boa tarde!')
    elif hora >= 18 and hora <= 23:
        print('Boa noite!')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros.')
"""

"""
nome = input('Digite seu primeiro nome: ')
tamanho_nome = len(nome)

if tamanho_nome >= 1 and tamanho_nome <= 2:
    print('Digite seu primeiro nome inteiro.')
elif tamanho_nome <= 4:
    print('Seu nome é curto!')
elif tamanho_nome >= 5 and tamanho_nome <= 6:
    print('Seu nome é médio!')
elif tamanho_nome >6:
    print('Seu nome é grande!')
else:
    print('Digite alguma coisa.')
"""


