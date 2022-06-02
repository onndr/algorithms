def merge_sort(list):
    if len(list) > 1:
        middle = round(len(list)/2)
        right = merge_sort(list[middle:])
        left = merge_sort(list[:middle])
        merged = []
        i = j = 0
        while len(merged) < len(left) + len(right):
            if i >= len(left):
                merged.append(right[j])
                j += 1
            elif j >= len(right):
                merged.append(left[i])
                i += 1
            elif right[j] <= left[i]:
                merged.append(right[j])
                j += 1
            elif left[i] < right[j]:
                merged.append(left[i])
                i += 1
        return merged
    else:
        return list
