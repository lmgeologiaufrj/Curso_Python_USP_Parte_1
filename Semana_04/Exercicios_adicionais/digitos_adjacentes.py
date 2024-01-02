numero = int(input("Digite um número inteiro: "))
adjacente = False
digito = numero % 10

while numero != 0:
    numero = numero // 10
    digito_anterior = numero % 10
    if digito_anterior == digito:
        adjacente = True
    digito = digito_anterior
if adjacente:
    print("sim")
else:
    print("não")
