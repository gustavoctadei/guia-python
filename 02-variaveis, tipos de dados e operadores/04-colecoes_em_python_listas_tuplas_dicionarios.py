programadores = ["Victor", "Juliana", "Samuel", "Caio", "Luana"]
print(type(programadores))
print(len(programadores))
print(programadores[4])

# As listas no Python são mutáveis
print(programadores)
programadores[1] = "Carolina"
print(programadores)

# Também podemos adicionar elementos na lista
programadores.append("Renato")
print(programadores)

# Através do método insert(), podemos indicar em qual posição o elemento será incluído
programadores.insert(1, "Rafael")
print(programadores)

# Para removermos um elemento da lista, podemos utilizar o remove() passando o valor
programadores.remove("Samuel")
print(programadores)

# Ou podemos remover um elemento da lista passando o seu índice através do método pop()
programadores.pop(0)
print(programadores)

# Uma lista pode possuir diferentes tipos de elementos em sua composição
aluno = ["Murilo", 19, 1.79]
print(type(aluno))
print(aluno)

# Tuplas
# É uma estrutura de dados semelhante à lista, porém ela é imutável
times_rj = ("Botafogo", "Flamengo", "Fluminense", "Vasco")
print(type(times_rj))
print(times_rj)

# Podemos acessar um elemento de uma tupla pelo seu índice
print(times_rj[2])

# Para dclarar uma tupla de um único ítem, é necessário colocar uma vírgula depois dele
objeto_string = ("tesoura")
objeto_tupla = ("tesoura",)

print(type(objeto_string))
print(type(objeto_tupla))

# Por ser imutável, os seus elementos não podem ser alterados
vogais = ('a', 'e', 'i', 'o', 'u')
# vogais[1] = 'E' #esta linha gera erro

# Dicionários
# Os Dicionários representam coleções de dados que contém na sua estrutura um conjunto de pares chave/valor, nos quais
# cada chave individual tem um valor associado
dados_cliente = {
    "Nome": "Renan",
    "Endereco": "Rua Cruzeiro do Sul",
    "Telefone": "982503645"
}
print(type(dados_cliente))
print(dados_cliente)

# Para adicionarmos elementos num dicionário, basta associar uma nova chave ao objeto e atribuir um valor associado
# a ela
dados_cliente["Idade"] = 40

print(dados_cliente)

# Para removermos um item do dicionario, podemos usar o método pop()
dados_cliente.pop("Telefone", None)

print(dados_cliente)

# Também podemos usar a palavra-chave del, que remove uma chave e o valor associado a ela
del dados_cliente["Idade"]

print(dados_cliente)

# Funções para Coleções

# min() e max()

numeros = [15, 5, 0, 20, 10]
nomes = ["Caio", "Alex", "Renata", "Patrícia", "Bruno"]

# Como esta lista é de inteiros, ele retorna o maior e menor valor
print(min(numeros))
print(max(numeros))

# Como esta lista é de strings, ele faz comparações alfabéticas
print(min(nomes))
print(max(nomes))

# sum()
numeros = [1, 3, 6]
print(sum(numeros))

# len()
paises = ["Argentina", "Brasil", "Colômbia", "Uruguai"]
print(len(paises))

# type()
professores = ['Carla', 'Daniel', 'Ingrid', 'Roberto']
estacoes = ('Primavera', 'Verão', 'Outono', 'Inverno')
cliente = {
    'Nome': 'Fábio Garcia',
    'email' : 'fabio_garcia_9@outlook.com'
}

print(type(professores))
print(type(estacoes))
print(type(cliente))
