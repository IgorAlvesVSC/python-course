"""
idade_entrada = input('Digite aqui sua idade: ')
idade_corte = 18
idade_int = int(idade_entrada)

if idade_int >= idade_corte:
    print('Você é maior de idade, então é elegível para tirar sua carta de habilitação!')
else: 
    print('Você é menor de idade, então é inelegível para tirar sua carta de habilitação!')
"""

##############################################################

"""entrada = input('Digite o ano do seu nascimento: ')
ano_nascimento = int(entrada)
ANO_ATUAL = 2024
idade = ANO_ATUAL - ano_nascimento

print(idade)
"""

##############################################################


num1 = float(input("Digite o primeiro número: "))
operacao = input("Escolha a operação (+, -, *, /): ")
num2 = float(input("Digite o segundo número: "))


if operacao == '+':
    resultado = num1 + num2
elif operacao == '-':
    resultado = num1 - num2
elif operacao == '*':
    resultado = num1 * num2
elif operacao == '/':
    if num2 != 0:
        resultado = num1 / num2
    else:
        print("Erro: Divisão por zero!")
        resultado = None
else:
    print("Operação inválida!")
    resultado = None

if resultado is not None:
    print(f"Resultado: {num1} {operacao} {num2} = {resultado}")


##############################################################

"""
peso = float(input('Digite o seu peso em kg (ex: 70): '))
altura = float(input('Digite a sua altura em m (ex: 1.50): '))

imc = peso / altura**2

if imc < 18.5:
    print(f'Seu IMC é = {imc:.2f}, você está abaixo do peso!')
elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é = {imc:.2f}, você está no peso normal!')
elif imc >= 25 and imc < 30:
    print(f'Seu IMC é = {imc:.2f}, você está com sobrepeso!')
elif imc >= 30:
    print(f'Seu IMC é = {imc:.2f}, você está obeso!')
"""

##############################################################

"""
palavra = input('Digite a palavra que será consultada: ')
contrario = palavra[::-1]

if palavra == contrario:
    print('Essa palavra é um palíndromo!')
else: 
    print('Essa palavra não é um palíndromo, tente outra.')
"""

##############################################################

"""
print('Calculadora de média.')
num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
num3 = float(input('Digite a terceira nota: '))
media = (num1 + num2 + num3) / 3
print(f'A média das notas é: {media:.2f}')
"""

##############################################################

"""

print('Conversor de temperatura.')
print('Escolha o tipo de conversão:')
print('1. Celsius para Fahrenheit') 
print('2. Fahrenheit para Celsius')
escolha = input('Escolha (1 ou 2): ')

if escolha == '1':
    temp_celsius = float(input('Digite a temperatura em Celsius: '))
    conv_fahrenheit = (9/5) *temp_celsius + 32
    print(f'{temp_celsius:.2f} graus Celsius é igual a {conv_fahrenheit:.2f} graus Fahrenheit!')

elif escolha == '2':
    temp_fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
    conv_celsius = (5/9) * (temp_fahrenheit - 32)
    print(f'{temp_fahrenheit:.2f} graus Fahrenheit é igual a {conv_celsius:.2f} graus Fahrenheit!')
"""

"""
def verificar_primo(numero):
    if numero <= 1:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def main():
    numero = int(input("Digite um número inteiro positivo: "))
    if verificar_primo(numero):
        print("O número inserido é primo.")
    else:
        print("O número inserido não é primo.")

if __name__ == "__main__":
    main()
"""

##############################################################

"""
import os

playlist = []

while True:
    print('----------------------------- \n Sua Playlist!')
    entrada = input('[a]dicionar música / [m]ostrar playlist / [d]eletar / [b]arra de pesquisa: ')

    if entrada == 'm':
        os.system('cls')
        for indice, elemento in enumerate(playlist):
            print(f"{indice} - {elemento}")
        if playlist == []:
            print('Sua playlist está vazia!')
    
    elif entrada == 'a':
        os.system('cls')
        novo_item = input('Digite a música para adicionar: ')
        if novo_item == '':
            print('Você não digitou nada.')
        else:
            playlist.append(novo_item)
            print(f'"{novo_item}" foi adicionada!')

    elif entrada == 'd':
        os.system('cls')
        escolha_deletar = input('Quer apagar a playlist [i]nteira ou só uma [m]úsica?: ')
        if escolha_deletar == 'i':
            playlist.clear()
            print('Sua playlist foi apagada!')
        elif escolha_deletar == 'm':
            os.system('cls')
            indice = input('Qual índice da música quer deletar?: ')
            try:
                indice_num = int(indice)
                playlist.pop(indice_num)
                print(f'A música de índice {indice_num} foi apagada')
            except ValueError:
                print('Digite o número referente ao índice.')
        else:
            print('Escolha uma opção válida.')

    elif entrada == 'b':
        os.system('cls')
        palavras_encontradas = []
        busca_digitada = input("Faça sua busca: ")

        for musica in playlist: 
            if busca_digitada in musica:
                palavras_encontradas.append(musica)
            
        if palavras_encontradas:
            print(f'As seguintes músicas foram encontradas:')
            for palavra in palavras_encontradas:
                print(palavra)
        else:
            print('Não foi encontrado nada referente a sua busca.')

    elif entrada == 's':
        break
    
    else:
        print('Por favor, escolha uma opção válida.')
"""

##############################################################

"""
while True:

    entrada = input('Digite a palavra da forca: ')

    if entrada == '' or entrada == ' ':
        print('Comece de novo e digite uma palavra.') 

    chute = input('Tente uma letra: ')
    letras_encontradas = ''

    for letra in entrada:
        print('*', end='')

    if chute in entrada:
        letras_encontradas += chute
        print(letras_encontradas)
"""

##############################################################

"""
import os

while True:
    

    print('Digite sua senha (obs: mais de 8 caracteres; sem sequências como: "abc" ou "123"; sem espaços.)')
    print()
    senha = input('Senha: ')

    os.system('cls' if os.name == 'nt' else 'clear')
    if senha == '':
        print('Você precisa digitar algo.')
    elif len(senha) < 8:
        print('Sua senha precisa ter 8 ou mais caracteres.')
    elif 'abc' in senha or '123' in senha:
        print('Para sua segurança, não coloque sequências como "abc" ou "123".')
    elif ' ' in senha or '  ' in senha:
        print('Não dê espaços na sua senha.')
    else:
        print('Bem vindo(a)!')
        break
"""

##############################################################

"""
import os

conta_cliente = []

produtos = {
    'água': 4,
    'coca': 6,
    'pastel': 13,
    'camarão': 84,
    'caipirinha': 22,
    'suco': 10,
}


while True:
    entrada = input('[M]arcar - [F]echar: ')

    if entrada.lower() == 'm':
        os.system('cls' if os.name == 'nt' else 'clear')
        item_marcar = input('Escreva o item que vai marcar: ')
        if item_marcar in produtos:
            conta_cliente.append(item_marcar)

    elif entrada.lower() == 'f':
        print('Sua conta foi:')
        quantidade_itens = {} 
        for item in conta_cliente:
            if item in quantidade_itens:
                quantidade_itens[item] += 1
            else:
                quantidade_itens[item] = 1
        for item, quantidade in quantidade_itens.items():
            print(f'{quantidade} {item}')
        total = sum(produtos[item] * quantidade for item, quantidade in quantidade_itens.items())
        print('Total gasto:', total, 'reais.')
        pagamento = float(input('Me dê o dinheiro para pagar: '))

        if pagamento < total:
            restante_negativo = pagamento - total
            restante_positivo = abs(restante_negativo)
            print(f'Você ainda me deve {restante_positivo} reais! Fica anotado pra próxima.')

        elif pagamento == total:
            print('Certinho! Obrigado e volte sempre.')

        elif pagamento > total:
            troco = pagamento - total
            print(f'Obrigado! Aqui está seu troco de {troco} reais.')
        break
"""

##############################################################

"""
import os

estoque_total = {}
valor_total_estoque = 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    entrada = input('[A]dicionar produtos / [R]etirar produtos / [V]er estoque / [F]echar programa: ')
    
    if entrada.lower() == 'a':
        while True:
            continuar = input('"menu" para voltar ao menu, ou deixe em branco para continuar: ')
            if continuar == 'menu':
                break
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                nome_produto = input('Digite o nome do produto: ')
                preco_produto = float(input('Digite o preço do produto: '))
                qtd_produto = int(input('Digite a quantidade no estoque atual: '))

                estoque_total[nome_produto] = {'preco': preco_produto, 'qtd': qtd_produto}

                valor_item = preco_produto * qtd_produto
                valor_total_estoque += valor_item


    elif entrada.lower() == "v":
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Estoque Total:")
            print()
            for nome, valores in estoque_total.items():
                print("Produto:", nome)
                print("Preço:", valores['preco'])
                print("Quantidade:", valores['qtd'])
                print(f'O estoque desse item está avaliado em {valores['preco'] * valores['qtd']} reais.')
                print()

            print(f'O valor TOTAL do estoque está avaliado em {valor_total_estoque}')
            input('"menu" para voltar: ') 
            break

    elif entrada.lower() == 'r':
        while True:
            continuar_2 = input('"menu" para voltar ao menu, ou deixe em branco para continuar: ')
            if continuar_2 == 'menu':
                break
            else:
                retirar_nome = input('Qual produto quer retirar?: ')
                retirar_qtd = int(input('Qual quantidade quer retirar?: '))

                if retirar_nome in estoque_total:
                    estoque_total[retirar_nome]['qtd'] -= retirar_qtd
                    print(f'{retirar_qtd} unidades do produto {retirar_nome} retiradas do estoque.')
                else:
                    print('Produto não encontrado no estoque.')

    if entrada.lower() == 'f':
        break
"""

##############################################################

"""
class Pessoa():
    calculador = 23.6
    
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

    def calorias_diarias(self):
        return self.peso * Pessoa.calculador 


igor = Pessoa('Igor', 80)
victor = Pessoa('Victor', 60)

print(igor.calorias_diarias())
print(victor.calorias_diarias())
"""

##############################################################

"""
class Carro:
    marca = 'Honda'
    modelo = 'Civic'
    ano = 2020
    cor = 'Prata'
    quilometragem = 18542

    def informacoes(self):
        print(f'Marca = {Carro.marca}')
        print(f'Modelo = {Carro.modelo}')
        print(f'Ano = {Carro.ano}')
        print(f'Cor = {Carro.cor}')
        print(f'Quilometragem = {Carro.quilometragem}km')
        

    def dirigir(self, km):
        print(f'O carro tinha {Carro.quilometragem}km, mas como você dirigiu por {km}km, agora ele tem', Carro.quilometragem + km, 'km')
        Carro.quilometragem += km



carro1 = Carro()
carro1.informacoes()
print()
carro1.dirigir(32)
carro1.dirigir(100)
"""

##############################################################

"""
class Animal:
    def contar_patas(self):
        print('Normalmente, um animal genérico possui 4 patas')

    def emitir_som(self):
        print('*Mugido genérico*')
        

class Cachorro(Animal):
    def emitir_som(self):
        print('O som do cachorro é "au-au"')

    def contar_patas(self):
        print('Cachorro tem 4 patas')


animal_generico = Animal()
cachorro = Cachorro()

animal_generico.contar_patas()
animal_generico.emitir_som()
cachorro.emitir_som()
cachorro.contar_patas()
"""

##############################################################

"""
class Pagamento:
    def _calcular_desconto(self): 
        raise NotImplementedError('Implemente o método calcular_desconto')
    

class PagamentoCartao(Pagamento):
    taxa_cartao = 3.2

    def calcular_desconto(self, valor):
        print(f'Pagando no cartão, o valor que era de R${valor}, agora passa a ser de R${valor + (valor * PagamentoCartao.taxa_cartao) / 100}')


class PagamentoBoleto(Pagamento):
    taxa_atraso = 5
    taxa_adianto = 5
    DIA_HOJE = 15

    def __init__(self, valor, dia_de_vencimento):
        self.valor = valor
        self.dia_de_vencimento = dia_de_vencimento

    def calcular_desconto(valor, dia_de_vencimento):
        if dia_de_vencimento > PagamentoBoleto.DIA_HOJE:
            print(f'O valor era R${valor}, mas como você atrasou o boleto, agora o valor é R${(valor * PagamentoBoleto.taxa_atraso) / 100}')

        elif dia_de_vencimento < PagamentoBoleto.DIA_HOJE:
            print(f'O valor era R${valor}, mas como você adiantou o boleto, agora o valor é R${valor - (valor * PagamentoBoleto.taxa_atraso) / 100}')
        
        elif dia_de_vencimento == PagamentoBoleto.DIA_HOJE:
            print(f'O valor é R${valor} pois não teve taxa de atraso ou de adianto')

#pc = PagamentoCartao()
#pc.calcular_desconto(1000)
            
pb = PagamentoBoleto(valor=100, dia_de_vencimento=10)
pb.calcular_desconto(10)
"""

##############################################################

"""
class Produto:
    def __init__(self, nome: str, preco: float, qtd_estoque: int):
        self.nome = nome
        self.preco = preco
        self.qtd_estoque = qtd_estoque
    

class Eletronico(Produto):
    def calcular_desconto(self) -> float:
        novo_preco = self.preco * 0.95
        print(f'O produto {self.nome}, que custava R${self.preco}, recebeu um desconto e agora custa {novo_preco}!')
        return novo_preco


class Alimento(Produto):
    def calcular_desconto(self) -> float :
        if self.qtd_estoque >= 10:
            print(f'O produto {self.nome} custa R${self.preco}!')
            return self.preco
        else:
            novo_preco = self.preco * 0.90
            print(f'O produto {self.nome}, que custava R${self.preco}, recebeu um desconto e agora custa {novo_preco}!')
            return novo_preco


xbox = Eletronico('Xbox', 2000, 20)
xbox.calcular_desconto()
xburguer = Alimento('X-Burguer', 20, 20)
xburguer.calcular_desconto()
xsalada = Alimento('X-Salada', 25, 8)
xsalada.calcular_desconto()
"""

##############################################################














    
        
    





    
    





    




    






 