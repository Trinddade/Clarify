class Carro:
    def __init__(self, cor, modelo):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f'O {self.modelo} acelerou para {self.velocidade}')

    def desacelerar(self):
        for _ in range(self.velocidade // 10):
            self.velocidade -= 10
        print(f'O {self.modelo} desacelerou para {self.velocidade}')

carro_do_Lucas = Carro('Preto', 'C3')
carro_do_Elias = Carro('Vermelho', 'Sandero')
carro_do_Yuri = Carro('Preto', 'New Fiesta')

carro_do_Lucas.acelerar(10)
carro_do_Lucas.acelerar(20)
carro_do_Lucas.desacelerar(20)