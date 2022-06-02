def bubble_sort(list):
    i = 0
    while i < len(list):
        j = 0
        while j + 1 < len(list) - i:
            if list[j] > list[j+1]:
                tmp = list[j+1]
                list[j+1] = list[j]
                list[j] = tmp
            j += 1
        i += 1
    return list
