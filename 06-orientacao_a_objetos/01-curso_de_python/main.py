from calculadora import Calculadora
from comodo import Comodo

calculadora = Calculadora()

comodo = Comodo(
    input("Qual a largura do cômodo? "),
    input("Qual a profundidade do cômodo? ")
)

# calculadora.area_paredes: float = 2 * (largura + profundidade) * altura

print("A área das paredes é:", calculadora.calcular_area_paredes(comodo.largura, comodo.profundidade, comodo.altura))

# calculadora.area_teto: float = largura * profundidade

print("A Área do teto é:", calculadora.calcular_area_teto(comodo.largura, comodo.profundidade))

print("A litragem de tinta necessária é:", calculadora.calcular_litragem_necessaria())
