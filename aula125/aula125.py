# Atributos de classe


class Pessoa:
    ano_atual = 2024

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade

igor = Pessoa('Igor', 17)
victor = Pessoa('Victor', 19)

print(Pessoa.ano_atual)
#Pessoa.ano_atual = 1

print(igor.get_ano_nascimento())
print(victor.get_ano_nascimento())