# coding: utf-8

nome = "Gustavo"

# Pegando a primeira letra
primeiraLetra = nome[0]
print(primeiraLetra)

# Fatiando uma string
fatia = nome[0:3]
print(fatia)

# Também podemos usar a forma inversa utilizando índices negativos
fatia = nome[-2]
print(fatia)

# Imutabilidade das Strings
print( id(nome) )
nome = "Eduardo"
# Um novo id, ou seja, apesar de ser a mesma variável, a original foi destruída e a nova string foi criada e não
# alterada pois são imutáveis
print( id(nome) )

# Também não é possível alterar o valor de um posição da string
# nome[6] = 'a'

# Tamanho da string
tamanho = len(nome)
print("Tamanho da string: ", str(tamanho))

# Concatenando strings
nome = "Daniel"
sobrenome = "Silva"
nome_completo = nome + ' ' + sobrenome
print(nome_completo)

# Comparação de strings
nome_1 = "Eduardo"
nome_2 = "Eduardo"

# Usando o operador ==
if nome_1 == nome_2:
    print("Iguais")
else:
    print("Diferentes")

# Usando o operador is
if nome_1 is nome_2:
    print("Iguais")
else:
    print("Diferentes")

# Método find()
mensagem = "String no Python"
print(mensagem.find("Python"))
print(mensagem.find("Java"))

# Método replace() - substituir ocorrências dentro de uma string
mensagem = "Quero aprender Java! Na DevMedia tem salas de Java para aprender essa linguagem"
nova_mensagem = mensagem.replace("Java", "Python")
print(nova_mensagem)

# Método split() - desmembrar strings
mensagem = "Estou aprendendo Python na DevMedia"
lista_mensagem = mensagem.split(" ")

print( type(lista_mensagem) )
print(lista_mensagem)
print(lista_mensagem[2])

# Método upper()
mensagem = "Eu gosto de Python"
nova_mensagem = mensagem.upper()
print(nova_mensagem)

# Método lower()
mensagem = "EU gOstO de pYthOn"
nova_mensagem = mensagem.lower()
print(nova_mensagem)

# Acentuação - devemos definir a codificação UTF-8 - não necessário no Python versão 3
nome = "João da Silva"
print(nome)