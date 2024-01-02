import math

a = float(input("Insira o parâmetro a: "))
b = float(input("Insira o parâmetro b: "))
c = float(input("Insira o parâmetro c: "))

delta = b**2 - 4 * a * c

if delta < 0:
    print("esta equação não possui raízes reais")
else:
    if delta == 0:
        print("a raiz desta equação é", (-b + math.sqrt(delta)) / (2 * a))
    else:
        print(
            "as raízes da equação são",
            (-b - math.sqrt(delta)) / (2 * a),
            "e",
            (-b + math.sqrt(delta)) / (2 * a),
        )
