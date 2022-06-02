import bubble_sort
import merge_sort
import quick_sort
import selection_sort

import measure_time
import collection_generator
import grapher
import sys

STEPS = 10
NUMBER_OF_VALUES_STEP = 300
REPEATS = 3


def collect_stats(sorting_function, steps=10, values_step=500, repeats=3):
    measures = {}
    for i in range(steps+1):
        values = collection_generator.get_words_list(
            i*values_step, 'pan-tadeusz.txt')
        measures[len(values)] = measure_time.measure_time(
            lambda: sorting_function(values), repeats)
        if len(values) < i*values_step:
            break
    return measures


def main():
    sys.setrecursionlimit(30000)
    # bubble_stats = collect_stats(
    #     bubble_sort.bubble_sort, STEPS, NUMBER_OF_VALUES_STEP, REPEATS)
    # merge_stats = collect_stats(
    #     merge_sort.merge_sort, STEPS, NUMBER_OF_VALUES_STEP, REPEATS)
    quick_stats = collect_stats(
        quick_sort.quick_sort, 1, 20000, 1)
    # selection_stats = collect_stats(
    #     selection_sort.selection_sort, STEPS, NUMBER_OF_VALUES_STEP, REPEATS)
    # built_in_func_stats = collect_stats(
    #     sorted, STEPS, NUMBER_OF_VALUES_STEP, REPEATS)
    # grapher.draw(bubble_stats, 'bubble')
    # grapher.draw(merge_stats, 'merge')
    grapher.draw(quick_stats, 'quick')
    # grapher.draw(built_in_func_stats, 'built in function')
    # grapher.draw(selection_stats, 'selection')
    # print(bubble_stats)
    # print('_____________________')
    # print(merge_stats)
    # print('_____________________')
    print(quick_stats)
    print('_____________________')
    # print(selection_stats)
    # print('_____________________')
    # print(built_in_func_stats)


if __name__ == '__main__':
    main()
