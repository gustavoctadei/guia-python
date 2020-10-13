# Laço for
#
# Sintaxe:
# for variavel in lista:
#   comandos
nomes = ["Pedro", "João", "Leticia"]
for nome in nomes:
    print(nome)

# for/else - A instrução else é executada ao final do for
nomes = ["Pedro", "João", "Leticia"]
for nome in nomes:
    print(nome)
else:
    print("Todos os nomes foram listados com sucesso")

# Outra maneira de utilizar o for
for i in range(0, 5):
    print(i)
