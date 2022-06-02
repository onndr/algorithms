def get_words_list(n, file_name):
    text = get_file_content(file_name)
    lines = [line.strip() for line in text.split('\n') if line]
    words = []
    for line in lines:
        words.extend(line.split(' '))
        if len(words) >= n:
            return words[:n]
    return words


def get_file_content(file_name):
    with open(file_name, 'r', encoding='utf8') as fh:
        return fh.read()
