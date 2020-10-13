# Estruturas de condição com IF
# Permite avaliar uma expressão e, de acordo com o seu resultado, executar uma determinada ação
idade = 18
if idade < 20:
    print("Você é jovem!")

# Estrutura IF-ELIF-ELSE
idade = int(input("Digite a sua idade: "))
if idade >= 10 and idade < 20:
    print("Você é adolescente")
elif idade >= 20 and idade < 30:
    print("Você é Jovem")
elif idade >=30 and idade <= 100:
    print("Você é adulto")
else:
    print("Valor não encontrado")
