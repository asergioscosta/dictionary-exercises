def mergeSort(v):
    mergeSort_ordena(v, 0, len(v) - 1)

def mergeSort_ordena(v, esq, dir):
    if esq == dir:
        return

    meio = (esq + dir) // 2
    mergeSort_ordena(v, esq, meio)
    mergeSort_ordena(v, meio + 1, dir)
    mergeSort_intercala(v, esq, meio, dir)

def mergeSort_intercala(v, esq, meio, dir):
    a_tam = meio - esq + 1
    b_tam = dir - meio
    a = v[esq:esq + a_tam]
    b = v[meio + 1:meio + 1 + b_tam]

    i = j = 0
    k = esq
    while k <= dir:
        if i == a_tam:
            v[k] = b[j]
            j += 1
        elif j == b_tam:
            v[k] = a[i]
            i += 1
        elif a[i] < b[j]:
            v[k] = a[i]
            i += 1
        else:
            v[k] = b[j]
            j += 1
        k += 1
