import tools
from BST import BST
from AVL import AVL
import sys


def create_BST(elements):
    bs_tree = BST()
    for el in elements:
        bs_tree.add_element(el)


def create_AVL(elements):
    AVL(elements)


def find_n_first_elements(tree, elements, n):
    for el in elements[:n]:
        tree.find_element(el)


def remove_n_first_elements(tree, elements, n):
    for el in elements[:n]:
        tree.remove_element(el)


def add_n_first_elements(tree, elements, n):
    for el in elements[:n]:
        tree.add_element(el)


def main():
    sys.setrecursionlimit(100000)
    "-----Binary search tree-----"
    elements = tools.generate_collection(30000, 30000)

    # create_BST_stats = tools.collect_stats_create(
    #     create_BST, elements, 10, 1000, 10)
    # print('created BST')
    # tools.draw_single('BST create', "elements", "time in s", create_BST_stats, "BST_create")

    bs_tree = BST()
    for element in elements:
        bs_tree.add_element(element)

    # find_BST_stats = tools.collect_stats_find(
    #     find_n_first_elements, bs_tree, elements, 30, 1000, 10)
    # print('found BST')
    # tools.draw_single('BST find', "elements", "time in s", find_BST_stats, "BST_find")

    remove_BST_stats = tools.collect_stats_remove(
        remove_n_first_elements, add_n_first_elements, bs_tree, elements, 10, 1000, 5)
    print('removed BST')
    tools.draw_single('BST remove', "elements", "time in s", remove_BST_stats, "BST_remove")

    "-----AVL tree-----"

    # create_AVL_stats = tools.collect_stats_create(
    #     create_AVL, elements, 10, 1000, 10)
    # print('created AVL')
    # tools.draw_single('AVL create', "elements", "time in s", create_AVL_stats, "AVL_create")

    avl_tree = AVL(elements)

    # find_AVL_stats = tools.collect_stats_find(
    #     find_n_first_elements, avl_tree, elements, 30, 1000, 10)
    # print('found AVL')
    # tools.draw_single('AVL find', "elements", "time in s", find_AVL_stats, "AVL_find")

    remove_AVL_stats = tools.collect_stats_remove(
        remove_n_first_elements, add_n_first_elements, avl_tree, elements, 10, 1000, 5)
    print('removed AVL')
    tools.draw_single('AVL remove', "elements", "time in s", remove_AVL_stats, "AVL_remove")

    # tools.draw_multiple('Create tree', 'elements', 'time in s', {'BST': create_BST_stats, 'AVL': create_AVL_stats}, 'create_tree')
    # tools.draw_multiple('Find in tree', 'elements', 'time in s', {'BST': find_BST_stats, 'AVL': find_AVL_stats}, 'find_in_tree')
    tools.draw_multiple('Remove from tree', 'elements', 'time in s', {'BST': remove_BST_stats, 'AVL': remove_AVL_stats}, 'remove_from_tree')


if __name__ == "__main__":
    main()
