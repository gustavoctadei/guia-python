# Laço while
i = 0
while i < 5:
    print(i)
    i += 1

# while/else - a Instrução else é executada após o fim do laço while
i = 0
while i < 5:
    print(i)
    i += 1
else:
    print("O loop while foi encerrado com sucesso")

# Se dentro do while existir um comando break, sairá do laço e não executará o else
i = 0
while i < 10:
    print(i)
    i += 1

    if i == 6:
        print("i é igual a 6")
        break
else:
    print("fim while")
