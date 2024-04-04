pessoa = {
    'nome': 'Igor',
    'sobrenome': 'Alves',
    'idade': 18,
    'altura': 1.7,
    'endereços': [
        {'rua': 'tal tal', 'número': 123},
        {'rua': 'outra rua', 'número': 321}
    ],
}

print(pessoa['nome'])
print(pessoa['sobrenome'])
print()

for chave in pessoa:
    print(chave, pessoa[chave])