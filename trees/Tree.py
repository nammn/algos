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

    def max(self):
        print(1)

    def min(self):
        print(2)

    def left(self):
        print(2)

    def right(self):
        print(2)

    def size(self):
        print(2)


root = Node(42)
inserts = [29, 27, 57, 71, 30, 97, 41, 78, 3, 60, 28, 100, 50]
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
