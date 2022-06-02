class Heap:
    def __init__(self, n, list=[], max=True):
        self.n = n
        self.max = max
        self.nodes = []
        self.size = 0
        for el in list:
            self.add(el)

    def heapify_down(self, i):
        priv = None
        while not i == priv:
            priv = i
            i = self.heapify(i)

    def heapify_up(self, i):
        while not (i-1)//self.n < 0:
            parent = (i-1)//self.n
            res = self.heapify(parent)
            i = parent
            if res == parent:
                break

    def heapify(self, i):
        parent = self.nodes[i]
        if self.n*i+1 < self.size:
            if self.max:
                max_child, i_max_child = self.get_max_child(i)
                if max_child > parent:
                    self.nodes[i] = max_child
                    self.nodes[i_max_child] = parent
                    return i_max_child
            else:
                min_child, i_min_child = self.get_min_child(i)
                if min_child < parent:
                    self.nodes[i] = min_child
                    self.nodes[i_min_child] = parent
                    return i_min_child
        return i

    def get_max_child(self, i):
        i = self.n*i+1
        to = self.n*(i+1)
        max = self.nodes[i]
        i_max = i
        while i <= to and i < self.size:
            if self.nodes[i] > max:
                max = self.nodes[i]
                i_max = i
            i += 1
        return max, i_max

    def get_min_child(self, i):
        i = self.n*i+1
        to = self.n*(i+1)
        min = self.nodes[i]
        i_min = i
        while i <= to and i < self.size:
            if self.nodes[i] < min:
                min = self.nodes[i]
                i_min = i
            i += 1
        return min, i_min

    def get_children(self, i):
        fr = self.n*i+1
        to = self.n*(i+1)
        return self.nodes[fr: to + 1]

    def add(self, value):
        self.nodes.append(value)
        self.size += 1
        self.heapify_up(self.size - 1)

    def pop(self):
        if not self.size:
            return
        if self.size == 1:
            self.size -= 1
            return self.nodes.pop()
        root = self.nodes[0]
        self.nodes[0] = self.nodes.pop()
        self.size -= 1
        self.heapify_down(0)
        return root

    def display(self):
        for i in range(self.size):
            string = f'{i}, {self.nodes[i]}'
            children = self.get_children(i)
            if children:
                string += ': ' + str(children) + ';'
            print(string)

import random
def generate_collection(n=100, rng=10000):
    return [random.randint(1, rng) for i in range(n)]
list = generate_collection(20, 1000)
# # list = [34, 32, 66, 222, 45, 324545, 23, 12, 0, 3, 5, 766]
heap = Heap(3, list, True)
heap.display()
# [heap.pop() for i in range(5)]
heap.pop()
heap.display()
