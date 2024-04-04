# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado verdadeiro, 
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é 
# usado para representar um não valor

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or 'e') and senha_digitada == senha_permitida:
    print('Entrar')
else:
    print('Sair')



senha = input('Senha: ') or 'Sem senha'
print(senha)

"""
q1 = input('Você está com fome? ')
q2 = input('Quer sair pra comer? ')

if q1 == 'sim' and q2 == 'sim':
    print('Vamos sair pra comer, então!')
elif q1 == 'sim' and q2 == 'não':
    print('Então fica com fome!')
elif q1 == 'não' and q2 == 'sim':
    print('Mas você é guloso em!')
"""



