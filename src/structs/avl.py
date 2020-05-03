class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None
        self.height = 0


class AVL:
    def __init__(self):
        self.root = None

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print(node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def insert(self, data):
        self.root = self.insert_node(data, self.root)

    def insert_node(self, data, node):
        if not node:
            return Node(data)

        if data < node.data:
            node.left_child = self.insert_node(data, node.left_child)
        else:
            node.right_child = self.insert_node(data, node.right_child)

        node.height = max(self.calculate_height(node.left_child), self.calculate_height(node.right_child)) + 1

        return self.settle_violation(data, node)

    def settle_violation(self, data, node):
        balance = self.calculate_balance(node)

        if balance > 1 and data < node.left_child.data:
            print('Left left heavy situation')
            return self.rotate_right(node)
        if balance < -1 and data > node.right_child.data:
            print('Right right heavy situation')
            return self.rotate_left(node)
        if balance > 1 and data > node.left_child.data:
            print('Left right heavy situation')
            node.left_child = self.rotate_left(node.left_child)
            return self.rotate_right(node)
        if balance < -1 and data < node.right_child.data:
            print('Right left heavy situation')
            node.right_child = self.rotate_right(node.right_child)
            return self.rotate_left(node)

        return node

    def calculate_height(self, node):
        if node is None:
            return -1

        return node.height

    def calculate_balance(self, node):
        if not node:
            return 0

        return self.calculate_height(node.left_child) - self.calculate_height(node.right_child)

    def rotate_right(self, node):
        print(f'Rotating right on node {node.data}')
        temp_left = node.left_child
        t = temp_left.right_child
        node.left_child = t
        temp_left.right_child = node

        node.height = max(self.calculate_height(node.left_child), self.calculate_height(node.right_child)) + 1
        temp_left.height = max(self.calculate_height(temp_left.left_child), self.calculate_height(temp_left.right_child)) + 1

        return temp_left

    def rotate_left(self, node):
        print(f'Rotating left on node {node.data}')
        temp_right = node.right_child
        t = temp_right.left_child
        node.right_child = t
        temp_right.left_child = node

        node.height = max(self.calculate_height(node.left_child), self.calculate_height(node.right_child)) + 1
        temp_right.height = max(self.calculate_height(temp_right.left_child), self.calculate_height(temp_right.right_child)) + 1

        return temp_right


# Right right heavy situation
avl_rr = AVL()

print('Expected output:')
print('Right right heavy situation')
print('Rotating left on node 1')
print('Output:')

avl_rr.insert(1)
avl_rr.insert(2)
avl_rr.insert(3)

print(avl_rr.root.data == 2)
print(avl_rr.root.left_child.data == 1)
print(avl_rr.root.right_child.data == 3)

print('Expected traverse: 1, 2, 3')
avl_rr.traverse()

# Left left heavy situation
avl_ll = AVL()

print()
print('Expected output:')
print('Left left heavy situation')
print('Rotating right on node 3')
print('Output:')

avl_ll.insert(3)
avl_ll.insert(2)
avl_ll.insert(1)

print(avl_ll.root.data == 2)
print(avl_ll.root.left_child.data == 1)
print(avl_ll.root.right_child.data == 3)

print('Expected traverse: 1, 2, 3')
avl_ll.traverse()

# Left right heavy situation
avl_lr = AVL()

print()
print('Expected output:')
print('Left right heavy situation')
print('Rotating left on node 3')
print('Rotating right on node 5')
print('Output:')

avl_lr.insert(5)
avl_lr.insert(3)
avl_lr.insert(4)

print(avl_lr.root.data == 4)
print(avl_lr.root.left_child.data == 3)
print(avl_lr.root.right_child.data == 5)

print('Expected traverse: 3, 4, 5')
avl_lr.traverse()

# Right left heavy situation
avl_rl = AVL()

print()
print('Expected output:')
print('Right left heavy situation')
print('Rotating right on node 5')
print('Rotating left on node 1')
print('Output:')

avl_rl.insert(1)
avl_rl.insert(5)
avl_rl.insert(2)

print(avl_rl.root.data == 2)
print(avl_rl.root.left_child.data == 1)
print(avl_rl.root.right_child.data == 5)

print('Expected traverse: 1, 2, 5')
avl_rl.traverse()
