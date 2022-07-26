#Classe é a base da orientação objeto, pois ela cria objetos. Utilizando CamelCase.
# método é uma função da classe e está atrelada ao objeto. Sua escrit aé com underline. Sempre terá o parâmetro do self.
# self é o próprio objeto que será criado passado implicitamente no método
# Atributos são criados após o método especial de inicialização __initi(self): logo abaixo com self.atributo o parâmetro é depois do =, nesse caso, 'nome'
class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.idade = idade
        self.nome = nome

    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))
    print(p.nome)
# Para alterar o atributo de um objeto criado, é possível retribuir chamando objeto . atributo e =
    p.nome = 'Clara'
    print(p.nome, p.idade)
    p = Pessoa('Maria', 24)
    print(p.nome)
    print(p.idade)
