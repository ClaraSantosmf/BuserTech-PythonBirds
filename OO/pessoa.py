#Classe é a base da orientação objeto, pois ela cria objetos. Utilizando CamelCase.
# método é uma função da classe e está atrelada ao objeto. Sua escrit aé com underline. Sempre terá o parâmetro do self.
# self é o próprio objeto que será criado passado implicitamente no método
class Pessoa:
    def cumprimentar(self):
        return 'Olá'

if __name__ == '__main__':
    p = Pessoa()
    print(Pessoa.cumprimentar(p))