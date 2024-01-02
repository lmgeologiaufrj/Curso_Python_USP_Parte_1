numero = int(input("Digite um número inteiro: "))
n = 2
ehPrimo = True
while n < numero:
    if numero % n == 0:
        ehPrimo = False
    n += 1
if ehPrimo:
    print("primo")
else:
    print("não primo")
