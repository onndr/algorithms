import random
from numpy import delete
from pyparsing import remove_quotes


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self, root=None):
        self.root = root

    def find_minimum_child(self, current):
        temp = current
        while(temp.left != None):
            temp = temp.left
        return temp

    def add_element(self, value, current=None):
        if self.root == None:
            self.root = Node(value)
        else:
            if current == None:
                current = self.root
            if value < current.value:
                if current.left == None:
                    current.left = Node(value)
                else:
                    self.add_element(value, current.left)
            else:
                if current.right == None:
                    current.right = Node(value)
                else:
                    self.add_element(value, current.right)

    def remove_element(self, value, current=None):
        if self.root == None:
            return None
        if current == None:
            current = self.root
        if value < current.value:
            current.left = self.remove_element(value, current.left)
        elif value > current.value:
            current.right = self.remove_element(value, current.right)
        else:

            if current.left == None:
                temp = current.right
                current = None
                return temp

            elif current.right == None:
                temp = current.left
                current = None
                return temp
            temp = self.find_minimum_child(current.right)
            current.value = temp.value
            current.right = self.remove_element(temp.value, current.right)

        return current

    def find_element(self, value, current=None):
        if self.root == None:
            return None
        if current == None:
            current = self.root
        if value == current.value:
            return current
        if value < current.value:
            if current.left == None:
                return False
            return self.find_element(value, current.left)
        else:
            if current.right == None:
                return False
            return self.find_element(value, current.right)

    def show(self):
        lines, n, p, x = self.get_line(self.root)
        for line in lines:
            print(line)

    def get_line(self, current):
        if current.right == None and current.left == None:
            line = '%s' % current.value
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # left child
        if current.right == None:
            lines, n, p, x = self.get_line(current.left)
            s = '%s' % current.value
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # right child
        if current.left == None:
            lines, n, p, x = self.get_line(current.right)
            s = '%s' % current.value
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children
        left, n, p, x = self.get_line(current.left)
        right, m, q, y = self.get_line(current.right)
        s = '%s' % current.value
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


# bs_tree = BST()
# elements = [4, 43, 12, 64, 11, 1, 33, 53, 99, 38]
# for element in elements:
#     bs_tree.add_element(element)

# bs_tree.show()
# bs_tree.remove_element(11)
# bs_tree.remove_element(64)
# bs_tree.show()
# el = bs_tree.find_element(64)
# print(el)