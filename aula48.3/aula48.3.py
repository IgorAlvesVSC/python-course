"""
Listas em Python
Tipo list- Mutável
Suporta vários valores de qualquer tipo
Conhecimentos reutilizáveis - índices e fatiamento
Métodos úteis: 
    append - Adiciona um item ao final
    insert - Adiciona um item ao índice escolhido
    pop - Remove do final ou do índice escolhido
    del - Apaga um índice
    clear - Limpa a lista 
    extend - Estende a lista
    + - Concatena listas
Create  Read  Update   Delete
Criar   ler  alterar   apagar = lista[i] (CRUD)
"""
lista_1 = [1,2,3]
lista_2 = [4,5,6]
lista_3 = lista_1 + lista_2
lista_1.extend(lista_2)
print(lista_3)