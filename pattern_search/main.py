from funcs import naive, kmp, kr
import tools
import sys


def collect_stats(func, words, text, steps=10, values_step=100, repeats=1):
    measures = {}
    for i in range(steps+1):
        nvalues = i*values_step
        selected_words = words[:nvalues]
        measures[nvalues] = tools.measure_time(
            lambda: func(selected_words, text), repeats)
    return measures


def find_words(find_func, words, text):
    i = 1
    for word in words:
        if len(word) == 1:
            i += 1
            continue
        find_func(word, text)
    # print(i)


def main():
    sys.setrecursionlimit(10000)
    text = tools.get_file_content('pan-tadeusz.txt')
    words = tools.get_words_list(1000, 'pan-tadeusz.txt')
    print("naive start")
    stats_naive = collect_stats(lambda words, text: find_words(
        naive, words, text), words, text, repeats=1)
    print("naive end")
    print("kmp started")
    stats_kmp = collect_stats(lambda words, text: find_words(
        kmp, words, text), words, text, repeats=1)
    print("kmp ended")
    print("kr started")
    stats_kr = collect_stats(lambda words, text: find_words(
        kr, words, text), words, text, repeats=1)
    print("kr ended")
    data = {
        'naive': stats_naive,
        'kmpfind': stats_kmp,
        'kr': stats_kr
    }
    tools.draw_multiple('Find pattern', 'Words, n',
                        'Time, s', data, 'find_pattern_All')


if __name__ == "__main__":
    main()
