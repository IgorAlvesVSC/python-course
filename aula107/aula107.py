"""
def zipper(list1, list2):
    interval = min(len(list1), len(list2))
    return [
        (list1[i], list2[i]) for i in range(interval)
    ]


cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']
"""

from itertools import zip_longest

cities = ['Salvador', 'Ubatuba', 'Belo Horizonte']
states = ['BA', 'SP', 'MG', 'RJ']

print(list(zip(cities, states)))
print(list(zip_longest(cities, states, fillvalue='SEM CIDADE')))

