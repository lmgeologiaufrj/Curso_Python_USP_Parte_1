def n_primos(n):
    numero = 2
    total = 0
    while numero <= n:
        fator = 2
        nao_e_primo = False
        while fator <= numero / 2:
            if numero % fator == 0:
                nao_e_primo = True
            fator += 1
        if nao_e_primo is False:
            total += 1
        numero += 1

    return total


print(n_primos(2))

print(n_primos(4))

print(n_primos(121))
