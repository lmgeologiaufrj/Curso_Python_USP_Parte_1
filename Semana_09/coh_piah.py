import re


def le_assinatura():
    """A funcao le os valores dos tracos linguisticos do modelo e
    devolve uma assinatura a ser comparada com os textos fornecidos"""
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]


def le_textos():
    """A funcao le todos os textos a serem comparados e devolve
    uma lista contendo cada texto como um elemento"""
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + " (aperte enter para sair):")

    return textos


def separa_sentencas(texto):
    """A funcao recebe um texto e devolve uma lista das sentencas dentro do texto"""
    sentencas = re.split(r"[.!?]+", texto)
    if sentencas[-1] == "":
        del sentencas[-1]
    return sentencas


def separa_frases(sentenca):
    """A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca"""
    return re.split(r"[,:;]+", sentenca)


def separa_palavras(frase):
    """A funcao recebe uma frase e devolve uma lista das palavras dentro da frase"""
    return frase.split()


def n_palavras_unicas(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras que
    aparecem uma unica vez"""
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas


def n_palavras_diferentes(lista_palavras):
    """Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas"""
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)


def compara_assinatura(as_a, as_b):
    """IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver
    o grau de similaridade nas assinaturas."""
    int = 0
    soma = 0
    while int <= 5:
        soma += abs(as_a[int] - as_b[int])
        int += 1
    S_ab = soma / 6
    return S_ab


def calcula_assinatura(texto):
    """IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a
    assinatura do texto."""
    sentencas = separa_sentencas(texto)

    frases = []
    int = 0
    while int < len(sentencas):
        frases += separa_frases(sentencas[int])
        int += 1

    palavras = []
    int = 0
    while int < len(frases):
        palavras += separa_palavras(frases[int])
        int += 1

    int = 0
    tamanho_palavras = 0
    while int < len(palavras):
        tamanho_palavras += len(palavras[int])
        if int == 135:
            print()
        int += 1

    wal = tamanho_palavras / len(palavras)

    ttr = n_palavras_diferentes(palavras) / len(palavras)

    hlr = n_palavras_unicas(palavras) / len(palavras)

    int = 0
    tamanho_sentencas = 0
    while int < len(sentencas):
        tamanho_sentencas += len(sentencas[int])
        int += 1

    sal = tamanho_sentencas / len(sentencas)

    sac = len(frases) / len(sentencas)

    int = 0
    tamanho_frases = 0
    while int < len(frases):
        tamanho_frases += len(frases[int])
        int += 1

    pal = tamanho_frases / len(frases)

    return [wal, ttr, hlr, sal, sac, pal]


def avalia_textos(textos, ass_cp):
    """IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp
    e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido
    infectado por COH-PIAH."""
    int = 1
    numero_texto = 1
    S_ab = compara_assinatura(calcula_assinatura(textos[0]), ass_cp)
    while int < len(textos):
        ass = calcula_assinatura(textos[int])
        S_ab_novo = compara_assinatura(ass, ass_cp)
        if S_ab_novo < S_ab:
            S_ab = S_ab_novo
            numero_texto = int + 1
        int += 1
    print("O autor do texto ", numero_texto, "está infectado com COH-PIAH")
    return numero_texto
