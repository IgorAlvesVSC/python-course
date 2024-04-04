"""
def duplicar(numero):
    dup = numero * 2
    return dup

def triplicar(numero):
    trip = numero * 3
    return trip

def quadriplicar(numero):
    quad = numero * 4
    return quad
"""
def criar_multiplicador(multiplicador):
    def multiplicar(numero):
        return numero * multiplicador
    return multiplicar


duplicar = criar_multiplicador(2)
triplicar = criar_multiplicador(3)
quadriplicar = criar_multiplicador(4)


print(duplicar(5))
print(triplicar(5))
print(quadriplicar(5))
