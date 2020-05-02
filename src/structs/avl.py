class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0


class AVL:
    def __init__(self):
        self.root = None

    def calculate_height(self, node):
        if node is None:
            return -1

        return node.height

    def calculate_balance(self, node):
        if not node:
            return 0

        return self.calculate_height(node.left_child) - self.calculate_height(node.right_child)

    def rotate_right(self, node):
        temp_left = node.left_child
        t = temp_left.right_child
        node.left_child = t
        temp_left.right_child = node

        node.height = max(self.calculate_height(node.left_child), self.calculate_height(node.right_child)) + 1
        temp_left.height = max(self.calculate_height(temp_left.left_child), self.calculate_height(temp_left.right_child)) + 1

        return temp_left

    def rotate_left(self, node):
        temp_right = node.right_child
        t = temp_right.left_child
        node.right_child = t
        temp_right.left_child = node

        node.height = max(self.calculate_height(node.left_child), self.calculate_height(node.right_child)) + 1
        temp_right.height = max(self.calculate_height(temp_right.left_child), self.calculate_height(temp_right.right_child)) + 1

        return temp_right
