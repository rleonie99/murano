def main():
    listaParaOrdenar = leituraDados('murano/exercicio5/exercicio5.txt')

    mergeSortOrd(listaParaOrdenar)
    bubbleSortOrd(listaParaOrdenar)

# Leitura dos Dados
def leituraDados(caminho):
    arquivo = open(caminho, 'r')
    lista = arquivo.readlines()
    arquivo.close()
    
    for i in range(0,len(lista)):
        lista[i] = int(lista[i])

    print('Entrada: ',end='')
    print(lista)

    return lista

# Metodos de Ordenacao
def mergeSort(lista):
    if len(lista) > 1:
        meio = len(lista)/2
        splitEsq = lista[:int(meio)]
        splitDir = lista[int(meio):]
        mergeSort(splitEsq)
        mergeSort(splitDir)

        i=0
        j=0
        k=0
        
        while i < len(splitEsq) and j < len(splitDir):
            if splitEsq[i] < splitDir[j]:
                lista[k] = splitEsq[i]
                i = i + 1
            else:
                lista[k]= splitDir[j]
                j = j + 1
            k = k + 1

        while i < len(splitEsq):
            lista[k] = splitEsq[i]
            i = i + 1
            k = k + 1

        while j < len(splitDir):
            lista[k]= splitDir[j]
            j = j + 1
            k = k + 1

    return lista
def mergeSortOrd(lista):
    mergeSort(lista)
    print('Ordenacao MergeSort: ',end='')
    print(lista)

    return lista

def bubbleSortOrd(lista):
    tamanho = len(lista)-1
    ordenada = False
    while not ordenada:
        ordenada = True
        for i in range(tamanho):
            if lista[i] > lista[i+1] :
                lista[i], lista[i+1] = lista[i+1], lista[i]
                ordenada = False

    print('Ordenacao BubbleSort: ',end='')
    print(lista)

    return lista
