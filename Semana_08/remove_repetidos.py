def remove_repetidos(lista):
    lista_ordenada = []
    for i in lista:
        if i not in lista_ordenada:
            lista_ordenada.append(i)
    lista_ordenada.sort()
    return lista_ordenada
