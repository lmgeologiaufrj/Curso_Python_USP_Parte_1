def é_hipotenusa(n):
    lado1 = 1
    hipotenusa = False
    while lado1 <= n:
        lado2 = 1
        while lado2 <= n:
            if n**2 == (lado1**2 + lado2**2):
                hipotenusa = True
            lado2 += 1
        lado1 += 1
    return hipotenusa


def soma_hipotenusas(n):
    soma = 0
    hipotenusa = 1
    while hipotenusa <= n:
        if é_hipotenusa(hipotenusa):
            soma = soma + hipotenusa
        hipotenusa += 1
    return soma
