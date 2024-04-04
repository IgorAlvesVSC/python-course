"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
import time

entrada = input('Digite o tempo do cronômetro: ')
tempo = int(entrada)
inicio = 0

while inicio <= tempo: 
    print(inicio)
    inicio = inicio + 1
    time.sleep(1)
    
print('Acabou')