class Comodo:
    __largura: float
    __profundidade: float
    __altura: float

    # Construtor da Classe
    # Não é necessário declarar os atributos previamente
    def __init__(self, largura, profundidade):
        self.largura = largura
        self.profundidade = profundidade
        self.__altura = 2.9

    @property
    def largura(self):
        return self.__largura

    @property
    def profundidade(self):
        return self.__profundidade

    @property
    def altura(self):
        return self.__altura

    @largura.setter
    def largura(self, largura):
        try:
            self.__largura = float(largura)

        except Exception:
            print("O valor da largura informado é inválido")
            exit()

    @profundidade.setter
    def profundidade(self, profundidade):
        try:
            self.__profundidade = float(profundidade)

        except Exception:
            print("O valor da profundidade informado é inválido")
            exit()
