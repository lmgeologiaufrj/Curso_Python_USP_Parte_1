def ehPrimo(numero):
    n = 2
    ehPrimo = True
    while n < numero:
        if numero % n == 0:
            ehPrimo = False
        n += 1
    return ehPrimo


def maior_primo(numero):
    n = 2
    while n <= numero:
        if ehPrimo(n):
            valor = n
        n += 1
    return valor


print(maior_primo(7))
