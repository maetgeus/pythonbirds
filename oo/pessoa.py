class Pessoa:
    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    renzo = Pessoa(nome='renzo',idade=44)
    cawan = Pessoa(nome='Cawan', idade=22)
    matheus = Pessoa(nome='matheus', idade=22)
    luciano = Pessoa(renzo, cawan, matheus, idade=70, nome='Luciano')
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(f'Nome: {filho.nome}, Idade: {filho.idade}')
    luciano.sobrenome = 'Ramalho'
    print(luciano.sobrenome)
    del luciano.filhos
    print(luciano.__dict__)
    print(renzo.__dict__)
