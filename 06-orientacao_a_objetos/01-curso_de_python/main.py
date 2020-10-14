from calculadora import Calculadora

calculadora = Calculadora()

largura: float = float(input("Qual a largura do cômodo? "))
altura: float = float(input("Qual a profundidade do cômodo? "))
profundidade: float = 2.9

calculadora.area_paredes: float = 2 * (largura + profundidade) * altura

print("A área das paredes é:", calculadora.area_paredes)

calculadora.area_teto: float = largura * profundidade

print("A Área do teto é:", calculadora.area_teto)

print("A litragem de tinta necessária é:", (calculadora.area_paredes + calculadora.area_teto) / 10)
