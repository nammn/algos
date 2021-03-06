from random import randint
from queues.Queue import Queue


class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # add a node in a binary way
    def add_node(self, node):
        if node.value > self.value:
            # push right
            if self.right is None:
                self.right = node
            else:
                self.right.add_node(node)
        else:
            # push left
            if self.left is None:
                self.left = node
            else:
                self.left.add_node(node)

    # searching the tree for a existing value
    def search(self, value):
        if self.value == value:
            return True
        else:
            if value > self.value:
                if self.right is None:
                    return False
                found = self.right.search(value)
            else:
                if self.left is None:
                    return False
                found = self.left.search(value)
        return found

    # depth first
    # root -> left -> right
    def traverse_pre_order(self):
        print(self.value)
        if self.left is not None:
            self.left.traverse_pre_order()
        if self.right is not None:
            self.right.traverse_pre_order()

    # left -> root -> right
    def traverse_in_order(self):
        if self.left is not None:
            self.left.traverse_in_order()
        print(self.value)
        if self.right is not None:
            self.right.traverse_in_order()

    #  left -> right -> root
    def traverse_post_order(self):
        if self.left is not None:
            self.left.traverse_in_order()
        if self.right is not None:
            self.right.traverse_in_order()
        print(self.value)

    # breadth first || level order
    def traverse_bfs(self):
        queue = Queue()
        queue.en_queue(self)
        while not queue.is_empty():
            node = queue.de_queue()
            print(node.value)
            if node.left is not None:
                queue.en_queue(node.left)
            if node.right is not None:
                queue.en_queue(node.right)

    # rebalance the tree, such that a search and insertion time of log*n to be the avg. case of skewed tree
    def balance_tree(self):
        print(1)

    def sum(self, node):
        if node is None:
            return 0
        else:
            left = self.sum(node.left)
            right = self.sum(node.right)
            mysum = node.value + left + right
            return mysum

    # fix, or is not right, neither is and!
    def max(self):
        current = self
        while current.right is not None:
            current = current.right
        return current

    def max_rec(self, node):
        if not node:
            return -99999999
        left_max = self.max_rec(node.left)
        right_max = self.max_rec(node.right)

        return max(left_max, right_max, node.value)

    def min(self):
        current = self
        while current.left is not None:
            current = current.left
        return current

    def min_rec(self, node):
        if not node:
            return 99999999
        left_min = self.min_rec(node.left)
        right_min = self.min_rec(node.right)

        return min(left_min, right_min, node.value)

    def left_sum(self, node):
        if not node:
            return 0
        left = node.left_sum(node.left)
        return left + node.value

    def right_sum(self, node):
        if not node:
            return 0
        right = node.right_sum(node.right)
        return right + node.value

    def max_depth(self, node):
        if not node:
            return 0
        ltree = node.max_depth(node.left)
        rtree = node.max_depth(node.right)

        if ltree > rtree:
            return ltree + 1
        else:
            return rtree + 1

    def width(self):
        
        print(2)


root = Node(42)
inserts = [29, 27, 57, 71, 30, 97, 41, 78, 102, 3, 60, 28, 100, 50]
sum = root.value
for i in inserts:
    n1 = Node(i)
    root.add_node(n1)
    sum += i
print('inserted: ', inserts)
print('sum: ', sum)

print('searching for 70: ', root.search(70))
print('searching for 50: ', root.search(50))
print('\n preOrder')
root.traverse_pre_order()
print('\n inOrder')
root.traverse_in_order()
print('\n postOrder')
root.traverse_post_order()
print('\n bfs')
root.traverse_bfs()
print('\n sum')
print(root.sum(root))

print('\n max')
print(root.max().value)

print('\n max-rec')
print(root.max_rec(root))

print('\n min')
print(root.min().value)

print('\n min-rec')
print(root.min_rec(root))

print('\n left-sum')
print(root.left_sum(root))

print('\n right-sum')
print(root.right_sum(root))

print('\n max-depth')
print(root.max_depth(root))
