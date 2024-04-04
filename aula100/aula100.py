import copy

produtos = [
    {'nome': 'Produto 1', 'preco': 10.00},
    {'nome': 'Produto 2', 'preco': 5.00},
    {'nome': 'Produto 5', 'preco': 8.00},
    {'nome': 'Produto 3', 'preco': 11.00},
    {'nome': 'Produto 4', 'preco': 9.00},
]

novos_produtos = [ 
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
    
]

produtos_ordenados_por_nome = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)

produtos_ordenados_por_preco = sorted(
    copy.deepcopy(produtos),
    key=lambda p: p['preco'],
)

print(*produtos, sep='\n')
print()
print(*novos_produtos, sep='\n')
print()
print(*produtos_ordenados_por_nome, sep='\n')
print()
print(*produtos_ordenados_por_preco, sep='\n')