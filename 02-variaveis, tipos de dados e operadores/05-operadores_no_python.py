# Operadores Aritméticos - São utilizados na execução de operações matemáticas
#
# + (Adição, ou sinal positivo) | Realiza a soma entre operandos, Adiciona o sinal de positivo ao número | 10 + 7, +4
# - (Subtração, ou sinal negativo) | Realiza a subtração entre operandos, Adicional o sinal negativo ao número | 10 - 7, -4
# * (Multiplicação) | Realiza a multiplicação entre operandos | 3 * 4
# / (Divisão) | Realiza a divisão entre operandos | 10 / 5
# % (Módulo) | Retorna o resto da divisão entre operandos | 4 % 2
# ** (Exponenciação) | Retorna um número elevado à potência de outro | 4**2

numero_1 = 4
numero_2 = 2

soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
modulo = numero_1 % numero_2
exponenciacao = numero_1 ** numero_2

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)
print(modulo)
print(exponenciacao)

# Precedência

# 1 - As expressões contidas entre parênteses têm precedência
print((2 + 5) * 3)

# 2 - Após os parênteses, o próximo operador com maior precedência é o de exponenciação
print(1 + 5**2)

# 3 - Multiplicação e divisão têm precedência sobre a adição e subtração, como na matemática
print(5 * 3 + 8)

# 4 - A ordem de precedência é avaliada da esquerda para a direita
print(8 + 5 - 10)

# Operadores de Atribuição
#
# = | x = 1 | x = 1
# += | x += 1 | x = x + 1
# -= | x -= 1 | x = x - 1
# *= | x *= 1 | x = x * 1
# /= | x /= 1 | x = x / 1
# %= | x %= 1 | x = x % 1

numero = 5
numero += 5
print(numero)

# Operadores de Comparação
#
# > (Maior que) | Verifica se um valor é maior que outro | x > 5
# < (Menor que) | Verifica se um valor é menor que outro | x < 5
# == (é igual a) | Verifica se um valor é igual ao outro | x == 5
# != (é diferente de) | Verifica se um valor é diferente do outro | x != 5
# >= (Maior ou igual a) | Verifica se um valor é maior ou igual ao outro | x >= 5
# <= (Menor ou igual a) | Verifica se um valor é menor ou igual ao outro | x <= 5

numero_1 = 2
numero_2 = 4

soma = numero_1 + numero_2

if soma < 10:
    print("Soma não é maior que 10")
else:
    print("Soma é maior ou igual a 10")

# Operadores Lógicos
#
# and | retorna True se todas as condições forem verdadeiras, caso contrário, retorna false | x > 1 and x < 5
# or | Retorna True se uma das condições for verdadeira, caso contrário, retorna False | x > 1 or x < 5
# not | Inverte o resultado: se o resultado da expressão for True, o operador retorna false | not(x > 1 and x < 5)

idade_lucas = 21
idade_carolina = 19

# Operador or
if idade_lucas >= 18 or idade_carolina >= 18:
    print("Pelo menos um dos dois é maior de idade")
else:
    print("Lucas e Carolina não são maiores de idade")

# Operador and
if idade_lucas >= 18 and idade_carolina >= 18:
    print("Lucas e Carolina são maiores de idade")
else:
    print("Pelo menos um dos dois não é maior de idade")

# Operadores de Identidade
#
# Servem para a comparação de objetos. Nessa comparação, é verificado se eles ocupam a mesma posição na memória.
#
# is | Retorna True se as variáveis comparadas forem o mesmo objeto | nome is "Marcos"
# is not | Retorna True se as variáveis comparadas não forem o mesmo objeto | x is not "Python"
time_carlos = 'Botafogo'
time_luciano = 'Flamengo'
time_fabricia = 'Botafogo'

if time_carlos is time_luciano:
    print("time_carlos - time_luciano = mesmo objeto")
else:
    print("time_carlos - time_luciano = objetos diferentes")

if time_carlos is time_fabricia:
    print("time_carlos - time_fabricia = mesmo objeto")
else:
    print("time_carlos - time_fabricia = objetos diferentes")

# Operadores de Associação - São utilizados para verificar se uma sequência contém um objeto
#
# in | Retorna True caso o valor seja encontrado na sequência | 2 in x
# not in | Retorna True caso o valor não seja encontrado na sequência | 2 not in x
frutas = ["banana", "laranja", "uva", "ameixa"]

fruta_1 = "ameixa"
fruta_2 = "melancia"

print(fruta_1 in frutas)
print(fruta_2 in frutas)
