"""
Você deve criar uma classe carro, que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade
Ele oferece os seguintes atibutos:
1) Atributo de dado velocidade
2) Método acelerar que deverá incrementar a velocidade de  uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) valor de direção com valores possíveis: Norte, Sul, Leste, Oeste

              N
           O     L
              S

2) Método girar_a_esquerda
3) Método girar_a_direita

    Exemplo:
    >>> # Testando Motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor.acelerar()
    >>> motor.velocidade
    2
    >>> motor.acelerar()
    >>> motor.velocidade
    3
    >>> motor.frear()
    >>> motor.velocidade
    1
    >>> motor.frear()
    >>> motor.velocidade
    0
    >>> #Testando Direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.girar_a_esquerda()
    >>> direcao.valor
    'Norte'

    >>> #Teste completo
    >>> carro = Carro(direcao, motor)
    >>> carro.velocidade()
    0
    >>> carro.acelerar()
    >>> carro.velocidade()
    1
    >>> carro.acelerar()
    >>> carro.velocidade()
    2
    >>> carro.frear()
    >>> carro.velocidade()
    0
    >>> carro.direcao()
    'Norte'
    >>> carro.girar_a_direita()
    >>> carro.direcao()
    'Leste'
    >>> carro.girar_a_esquerda()
    >>> carro.direcao()
    'Norte'
    >>> carro.girar_a_esquerda()
    >>> carro.direcao()
    'Oeste'

"""

NORTE = 'Norte'
SUL = 'Sul'
LESTE = 'Leste'
OESTE = 'Oeste'

class Direcao:
    rotacao_a_direita = {NORTE:LESTE,LESTE:SUL,SUL:OESTE,OESTE:NORTE}
    rotacao_a_esquerda = {NORTE:OESTE,LESTE:NORTE,SUL:LESTE,OESTE:SUL}

    def __init__(self):
        self.valor = NORTE

    def girar_a_direita(self):
        self.valor = self.rotacao_a_direita[self.valor]

    def girar_a_esquerda(self):
        self.valor = self.rotacao_a_esquerda[self.valor]

class Motor:
    def __init__(self):
        self.velocidade = 0

    def acelerar(self):
        self.velocidade += 1

    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0,self.velocidade)

if __name__ == '__main__':
    motor = Motor()
