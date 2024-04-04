# Métodos úteis dos dicionários em Python
# len - quantas chaves
# keys - iterável com as chaves
# values - iterável com os valores
# items - iterável com chaves e valores
# setdefault - adiciona valor se a chave não existe
# copy - retorna uma cópia rasa (shallow copy)
# get - obtém uma chave
# pop - apaga um item com a chave especificada (del)
# popitem - apaga o último item adicionado
# update - atualiza um dicionário com outro

pessoa = {
    'nome': 'Luiz Otávio',
    'sobrenome ': 'Miranda',
    'idade': 100
}

pessoa.setdefault('idade', 0)
print(pessoa['idade'])
#print(len(pessoa))
#print(list(pessoa.keys()))
#print(list(pessoa.values()))
#print(list(pessoa.items()))

#for valor in pessoa.values():
#    print(valor)

#for chave, valor in pessoa.items():
#    print(chave, valor)