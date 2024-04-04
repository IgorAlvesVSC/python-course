import os
import sys

lista = []
indices = range(len(lista))

while True:
    lista_enumerada = list(enumerate(lista))
    print('Selecione uma opção')
    resposta = input('[i]nserir, [a]pagar, [l]istar, [s]air: ')

    if resposta == 'i':
        os.system('cls')
        item_inserido = input('Digite o que você quer inserir: ')
        lista.append(item_inserido)

    elif resposta == 'a':
        os.system('cls')
        apagar_ou_nao_a_lista_toda = input('Quer apagar a lista [t]oda ou apenas um [i]ndice?: ')
        if apagar_ou_nao_a_lista_toda == 'i':
            try:
                indice_apagar = int(input('Digite o índice do item que quer apagar: '))
                lista.pop(indice_apagar)
                print(f'Feito! O item de índice {indice_apagar} foi apagado da lista.')
            except:
                print('Não foi possível encontrar o índice requerido!')
        elif apagar_ou_nao_a_lista_toda == 't':
            lista.clear()
            print('Feito! A lista toda foi apagada!')
        else:
            print('Digite uma opção válida.')

    elif resposta == 'l':
      os.system('cls')
      if lista == []:
         print('Nada para listar')
      for i, resposta in enumerate(lista):
          print(i,resposta)

    elif resposta == 's':
        print("Obrigado por acessar!")
        sys.exit(0)

    else:
        print("Selecione uma opção válida.")
        continue 


    

