# Exercícios com funções
"""
def multiplicacao(*args):
    total = 1
    for numero in args:
        total *= numero
    return total

resultado = multiplicacao(1,2,3,4)
print(resultado)
"""

def par_impar(numero):
    multiplo_de_dois = numero % 2 == 0

    if multiplo_de_dois:
        return f'{numero} é par'
    
    return f'{numero} é ímpar'

print(par_impar(2))
print(par_impar(3))
print(par_impar(15))
print(par_impar(16))

