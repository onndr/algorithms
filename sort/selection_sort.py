def selection_sort(array):
    size = len(array)
    for i in range(size):
        iMin = i
        for j in range(i + 1, size):
            if array[j] < array[iMin]:
                iMin = j
        ii = array[i]
        jj = array[iMin]
        array[i] = jj
        array[iMin] = ii
    return array
