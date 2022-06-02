def quick_sort(array, left=0, right=-1):
    if (right == -1):
        right = len(array) - 1
    if (left >= right):
        return array
    p = partition(array, left, right)
    quick_sort(array, left, p-1)
    quick_sort(array, p+1, right)
    return array


def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if (array[j] < pivot):
            i += 1
            ii = array[i]
            jj = array[j]
            array[i] = jj
            array[j] = ii
    ii = array[i + 1]
    rr = array[right]
    array[i + 1] = rr
    array[right] = ii
    return i + 1
