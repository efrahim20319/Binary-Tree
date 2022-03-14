def removerRepetidos(array):
    for i in range(len(array)):
        j = i+1
        while (j < len(array)):
            if array[i] == array[j]:
                del array[j]
            j += 1
    return array