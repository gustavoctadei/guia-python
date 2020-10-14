largura: float = float(input("Qual a largura do cômodo? "))
altura: float = float(input("Qual a profundidade do cômodo? "))
profundidade: float = 2.9

area_paredes: float = 2 * (largura + profundidade) * altura

print("A área das paredes é:", area_paredes)

area_teto: float = largura * profundidade

print("A Área do teto é:", area_teto)

print("A litragem de tinta necessária é:", (area_paredes + area_teto) / 10)
