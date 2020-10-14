from calculadora import Calculadora

calculadora = Calculadora()

largura: float = float(input("Qual a largura do cômodo? "))
altura: float = float(input("Qual a profundidade do cômodo? "))
profundidade: float = 2.9

# calculadora.area_paredes: float = 2 * (largura + profundidade) * altura

print("A área das paredes é:", calculadora.calcular_area_paredes(largura, profundidade, altura))

# calculadora.area_teto: float = largura * profundidade

print("A Área do teto é:", calculadora.calcular_area_teto(largura, profundidade))

print("A litragem de tinta necessária é:", calculadora.calcular_litragem_necessaria())
