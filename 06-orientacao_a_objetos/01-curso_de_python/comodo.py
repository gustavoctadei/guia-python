class Comodo:
    largura: float
    profundidade: float
    altura: float

    # Construtor da Classe
    # Não é necessário declarar os atributos previamente
    def __init__(self, largura, profundidade):
        self.largura = float(largura)
        self.profundidade = float(profundidade)
        self.altura = 2.9
