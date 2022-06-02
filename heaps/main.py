import tools
import sys
from heap import Heap


def main():
    sys.setrecursionlimit(100000)
    numbers = tools.generate_collection(300001, 300000)
    create_2_heap_stats = tools.collect_stats_create(2, numbers, 30, 10000, 10)
    print('created2')
    create_3_heap_stats = tools.collect_stats_create(3, numbers, 30, 10000, 10)
    print('created3')
    create_4_heap_stats = tools.collect_stats_create(4, numbers, 30, 10000, 10)
    print('created4')

    data_create = {
        '2-ary': create_2_heap_stats,
        '3-ary': create_3_heap_stats,
        '4-ary': create_4_heap_stats
        }

    tools.draw_multiple('Heap create', 'elements', 'time in s', data_create, 'create300k')

    remove_root_2_heap_stats = tools.collect_stats_remove(2, numbers, 30, 10000, 10)
    print('removed2')
    remove_root_3_heap_stats = tools.collect_stats_remove(3, numbers, 30, 10000, 10)
    print('removed3')
    remove_root_4_heap_stats = tools.collect_stats_remove(4, numbers, 30, 10000, 10)
    print('removed4')

    data_remove = {
        '2-ary': remove_root_2_heap_stats,
        '3-ary': remove_root_3_heap_stats,
        '4-ary': remove_root_4_heap_stats
        }

    tools.draw_multiple('Heap remove root', 'elements', 'time in s', data_remove, 'remove300k')

if __name__ == "__main__":
    main()
