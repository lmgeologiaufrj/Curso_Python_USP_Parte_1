import math

x1 = float(input("Insira a primeira coordenada x: "))
y1 = float(input("Insira a primeira coordenada y: "))
x2 = float(input("Insira a segunda coordenada x: "))
y2 = float(input("Insira a segunda coordenada y: "))

distancia = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if distancia >= 10:
    print("longe")
else:
    print("perto")
