def maximo(a, b, c):
    if a <= b:
        maior = b
    else:
        maior = a
    if maior <= c:
        maior = c
    return maior
