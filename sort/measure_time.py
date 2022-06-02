import gc
import time


def measure_time(function, repeats):
    gc_old = gc.isenabled()
    gc.disable()
    measures = []
    for i in range(repeats):
        start = time.process_time()
        function()
        stop = time.process_time()
        measures.append(stop - start)
    if gc_old: gc.enable()
    return sum(measures)/repeats
