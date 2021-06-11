class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    Pessoa.olhos = 3
    luciano.olhos = 1
    del luciano.olhos
    print(luciano.__dict__)
    print(renzo.__dict__)
    print(cawan.olhos)
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), luciano.nome_e_atributos_de_classe())