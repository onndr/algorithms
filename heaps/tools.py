from matplotlib import pyplot
from heap import Heap
import random
import time
import gc


def generate_collection(n=50, rng=1000):
    return [random.randint(1, rng) for i in range(n)]


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


def collect_stats_create(n, elements, steps=10, values_step=100, repeats=1):
    measures = {}
    def creat_heap_func(n, elements):
        Heap(n, elements)
    for i in range(steps+1):
        nvalues = i*values_step
        measures[nvalues] = measure_time(
            lambda: creat_heap_func(n, elements[:nvalues]), repeats)
    return measures


def collect_stats_remove(n, numbers, steps=10, values_step=100, repeats=1):
    measures = {}
    def remove_heap_root_func(heap, n):
        for i in range(n):
            heap.pop()
    for i in range(steps+1):
        heap = Heap(n, numbers)
        ntimes = i*values_step
        measures[ntimes] = measure_time(
            lambda: remove_heap_root_func(heap, ntimes), repeats)
    return measures
