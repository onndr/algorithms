def naive(pattern, text):
    list_of_occurs = []
    i = 0
    t = 0  # position of current character in text
    p = 0  # position of current character in pattern
    text_end = len(text) - len(pattern)
    while i <= text_end:
        pattern_end = i + len(pattern) - 1
        while t <= pattern_end:
            if not pattern[p] == text[t]:
                break
            if t == pattern_end:
                list_of_occurs.append(i)
            p += 1
            t += 1
        p = 0
        i += 1
        t = i
    return list_of_occurs


def kmp(pattern, text):
    list_of_occurs = []

    def calculate_prefix(pattern):
        pattern_length = len(pattern)
        arr = [0] * pattern_length
        prefix_len = 0
        j = 1
        while j < pattern_length:
            if pattern[prefix_len] == pattern[j]:
                prefix_len += 1
                arr[j] = prefix_len
                j += 1
            elif prefix_len != 0:
                prefix_len = arr[prefix_len - 1]
            else:
                j += 1
        return arr

    if pattern and text:
        prefix = calculate_prefix(pattern)
        t = 0  # position of current character in text
        p = 0  # position of current character in pattern
        while t < len(text):
            if text[t] == pattern[p]:
                t += 1
                p += 1
            elif p != 0:
                p = prefix[p - 1]
            else:
                t += 1
            if p == len(pattern):
                list_of_occurs.append(t - p)
                p = prefix[p - 1]
    return list_of_occurs


def get_hash(pattern, Q):
    m = len(pattern)
    result = 0
    for i in range(m):
        result = (10 * result + ord(pattern[i])) % Q
    return result


def kr(pattern, text):
    Q = 256
    list_of_occurs = []

    pattern_len = len(pattern)
    text_len = len(text)

    multiplier = 1
    for i in range(1, pattern_len):
        multiplier = (multiplier * 10) % Q

    pattern_hash = get_hash(pattern, Q)
    text_hash = get_hash(text[:pattern_len], Q)

    for index_symbol in range(text_len - pattern_len + 1):
        if pattern_hash == text_hash:
            if text[index_symbol: index_symbol + pattern_len] == pattern:
                list_of_occurs.append(index_symbol)

        if index_symbol < text_len - pattern_len:
            text_hash = ((text_hash - ord(text[index_symbol]) * multiplier) * 10 + ord(
                text[index_symbol + pattern_len])) % Q

            if text_hash < 0:
                text_hash += Q

    return list_of_occurs


# text = 'aiaisdi, what is aiaiaisdi? aisdaisdii'
# pat = 'aiai'
# print(naive(pat, text))
# print(kmp(pat, text))
# print(kr(pat, text))
# print("------------")
# text = 'absbab'
# pat = 'b'
# print(naive(pat, text))
# print(kmp(pat, text))
# print(kr(pat, text))
# print("------------")
# text = 'absbab'
# pat = ''
# print(naive(pat, text))
# print(kmp(pat, text))
# print(kr(pat, text))
# print("------------")
# text = 'absbab'
# pat = 'absbab'
# print(naive(pat, text))
# print(kmp(pat, text))
# print(kr(pat, text))
