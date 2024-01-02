lista = []
lista.append(int(input("Digite um número: ")))
while lista[-1] != 0:
    lista.append(int(input("Digite um número: ")))

for i in lista[-2::-1]:
    print(i)
