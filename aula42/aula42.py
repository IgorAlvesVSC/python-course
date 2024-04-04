frase = 'O Python é uma linguagem de programação multiparadigma. Pthon foi criado por Guido van Rossum.'

i = 0
qtd_apareceu_mais_vezes = 0
letra_apareceu_mais_vezes = ''
while i < len(frase):
    letra_atual = frase[i]
    quantas_vezes_apareceu = frase.count(letra_atual)

    if qtd_apareceu_mais_vezes < quantas_vezes_apareceu:

    print(letra_atual, quantas_vezes_apareceu)
    i += 1

#PULEI ESSA AULA