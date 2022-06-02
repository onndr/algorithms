import math
from io import StringIO


class HeapIsFull(Exception):
    pass


class EmptyHeap(Exception):
    pass


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Ary_2_Heap:
    def __init__(self, capacity=100):
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def is_full(self):
        return self.size == self.capacity

    def swap(self, index1, index2):
        temp = self.storage[index1]
        self.storage[index1] = self.storage[index2]
        self.storage[index2] = temp

    def get_parent(self, index):
        return self.storage[self.get_parent_index(index)]

    def get_left_child(self, index):
        return self.storage[self.get_left_child_index(index)]

    def get_right_child(self, index):
        return self.storage[self.get_right_child_index(index)]

    def get_parent_index(self, index):
        return (index - 1) // 2

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def insert(self, element):
        if (self.is_full()):
            raise HeapIsFull()
        self.storage[self.size] = element
        self.size += 1
        self.heapify_up()

    def remove_min(self):
        if (self.size == 0):
            raise EmptyHeap()
        element = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        size -= 1
        self.heapify_down()
        return element

    def heapify_up(self):
        index = 0
        while (self.has_left_child(index)):  # check for only left because it is a complete tree
            smaller_child_index = self.get_left_child_index(index)
            if (self.has_right_child(index) and self.get_right_child(index) < self.get_left_child(index)):
                smaller_child_index = self.get_right_child_index(index)
            if (self.storage[index] < self.storage[smaller_child_index]):
                break
            else:
                self.swap(index, smaller_child_index)
            index = smaller_child_index

    def heapify_down(self):
        index = self.size - 1
        while (self.has_parent(index) and self.get_parent(index) > self.storage[index]):
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

    def display(self):
        for i in range(1, (self.size//2)+1):
            print(" PARENT : " + str(self.storage[i])+"   LEFT CHILD : " +
                  str(self.storage[2 * i])+"  RIGHT CHILD : " +
                  str(self.storage[2 * i + 1]))


heap = Ary_2_Heap()
elements = [4, 43, 12, 64, 11, 1, 33, 53, 99, 38, 111]
for element in elements:
    heap.insert(element)

heap.display()
