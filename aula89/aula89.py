# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, metodo):
    print(f'Existe {metodo}')
    print(getattr(string, metodo)())
else:
    print(f'Não existe {metodo}')