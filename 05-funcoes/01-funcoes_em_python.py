# Funções em Python
#
# A palvra reservada def explicita a definição da função naquele ponto
def hello(meu_nome):
    print("Olá,", meu_nome)


hello("Gustavo")


def hello_idade(meu_nome, idade):
    print("Olá,", meu_nome, "\nIdade:", idade)


hello_idade("Gustavo", 24)


def print_hello():
    print("Olá mundo!")


print_hello()


# As funções também podem ter um retorno
def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)

    if horas <= 40:
        salario = horas * taxa
    else:
        horas_excedentes = horas - 40
        salario = 40 * taxa + (horas_excedentes * (1.5 * taxa))

    return salario


string_horas = input("Digite a quantidade de horas: ")
string_taxa = input("Digite a taxa: ")

total_salario = calcular_pagamento(string_horas, string_taxa)

print("O valor de seus rendimentos é R$", total_salario)


# Parâmetros nomeados
def calcula_imc(peso, altura):
    print(peso / altura**2)


calcula_imc(75, 1.68)
calcula_imc(peso=75, altura=1.68)
calcula_imc(altura=1.68, peso=75)

# Funções built in - Não precisam dar import, estão sempre disponíveis para serem utilizadas:
# Exemplos: max(), min(), input(), float(), int()
maior_numero = max(1, 2, 3)
maior_letra = max('a', 'b', 'c')
print(maior_numero)
print(maior_letra)

# Funções disponíveis em módulos
# Exemplo função exp() que está no módulo math
import math
exponencial = math.exp(3)
print(exponencial)
