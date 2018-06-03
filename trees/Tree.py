from random import randint


class Node:
    left = None
    right = None
    value = None

    def __init__(self, value):
        self.value = value

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

    # print every value, while traversing
    def traverse_inorder(self):
        print('ok')

    def traverse_preorder(self):
        print('ok')

    def traverse_postOrder(self):
        print('ok')

    # rebalance the tree, such that a search and insertion time of log*n to be the avg. case
    def balanceTree(self):
        print(1)


root = Node(7)
inserts = []
for i in range(0, 10):
    x = randint(0, 100)
    n1 = Node(x)
    root.add_node(n1)
    inserts.append(x)
print('inserted: ', inserts)
n1 = Node(70)
root.add_node(n1)

print(root.search(70))
