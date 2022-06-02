from matplotlib import pyplot


def draw(stats, algorithm_name):
    pyplot.title('Sorting algorithms')
    pyplot.xlabel('Sorted words')
    pyplot.ylabel('Time in seconds')
    pyplot.plot(stats.keys(), stats.values(), label=algorithm_name)
    pyplot.legend()
    pyplot.savefig('plot.png')
