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

        print('ok')

    # rebalance the tree, such that a search and insertion time of log*n to be the avg. case
    def balanceTree(self):
        print(1)


root = Node(42)
inserts = [29, 27, 57, 71, 30, 97, 41, 78, 3, 60, 28, 100, 50]
for i in inserts:
    n1 = Node(i)
    root.add_node(n1)
print('inserted: ', inserts)

# print(root.search(70))
print('\n preOrder')
root.traverse_pre_order()
print('\n inOrder')
root.traverse_in_order()
print('\n postOrder')
root.traverse_post_order()
