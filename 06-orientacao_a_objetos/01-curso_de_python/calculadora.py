class Calculadora:
    # Para os atributos serem privados, devemos declará-los com __ no início do nome
    __area_paredes: float
    __area_teto: float

    def calcular_area_paredes(self, comodo):
        self.__area_paredes = 2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return self.__area_paredes

    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return self.__area_teto

    def calcular_litragem_necessaria(self):
        return (self.__area_paredes + self.__area_teto) / 10
