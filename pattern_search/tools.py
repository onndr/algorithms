from matplotlib import pyplot
import time
import gc


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


def draw_multiple(plot_name, xlabel, ylabel, data, file_name):
    pyplot.clf()
    pyplot.title(plot_name)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    for label, stats in data.items():
        pyplot.plot(stats.keys(), stats.values(), label=label)
    pyplot.legend()
    pyplot.savefig(f'{file_name}.png')


def draw_single(plot_name, xlabel, ylabel, data, file_name):
    pyplot.clf()
    pyplot.title(plot_name)
    pyplot.xlabel(xlabel)
    pyplot.ylabel(ylabel)
    pyplot.plot(data.keys(), data.values(), label=plot_name)
    pyplot.legend()
    pyplot.savefig(f'{file_name}.png')


def measure_time(function, repeats):
    gc_old = gc.isenabled()
    gc.disable()
    measures = []
    for i in range(repeats):
        start = time.process_time()
        function()
        stop = time.process_time()
        measures.append(stop - start)
    if gc_old:
        gc.enable()
    return sum(measures)/repeats
