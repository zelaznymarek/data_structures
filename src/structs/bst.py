class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class BST:

    def __init__(self):
        self.root = None
        self.elements = 0

    def insert(self, data):
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            self.elements += 1
        else:
            self.insert_node(new_node, self.root)

    def insert_node(self, new_node, node):
        if new_node.data < node.data:
            if node.left_child:
                self.insert_node(new_node, node.left_child)
            else:
                node.left_child = new_node
                self.elements += 1

        else:
            if node.right_child:
                self.insert_node(new_node, node.right_child)
            else:
                node.right_child = new_node
                self.elements += 1

    def min(self):
        if self.root:
            return self.min_value(self.root)

    def min_value(self, node):
        if node.left_child:
            return self.min_value(node.left_child)

        return node.data

    def max(self):
        if self.root:
            return self.max_value(self.root)

    def max_value(self, node):
        if node.right_child:
            return self.max_value(node.right_child)

        return node.data

    def traverse(self):
        if self.root:
            self.traverse_in_order(self.root)

    def traverse_in_order(self, node):
        if node.left_child:
            self.traverse_in_order(node.left_child)

        print(node.data)

        if node.right_child:
            self.traverse_in_order(node.right_child)

    def delete(self, data):
        if self.root:
            self.root = self.delete_node(data, self.root)

    def delete_node(self, data, node):
        if not node:
            return node

        if data < node.data:
            node.left_child = self.delete_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.delete_node(data, node.right_child)
        else:
            if all([not node.left_child, not node.right_child]):
                print('Removing leaf node')
                del node
                return None
            elif node.left_child:
                print('Removing node with left child only')
                temp_node = node.left_child
                del node
                return temp_node
            elif node.right_child:
                print('Removing node with right child only')
                temp_node = node.right_child
                del node
                return temp_node

            print('Removing node with two children')
            temp_node = self.get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.delete_node(temp_node.data, node.left_node)

        return node

    def get_predecessor(self, node):
        if node.right_child:
            return self.get_predecessor(node.right_child)

        return node


bst = BST()
bst.insert(7)
bst.insert(10)
bst.insert(-2)
bst.insert(1)
bst.insert(15)
bst.insert(12)

print(bst.elements == 6)
print(bst.min() == -2)
print(bst.max() == 15)

bst.traverse()

print(bst.root.right_child.right_child.left_child.data == 12)
print(bst.root.right_child.right_child.right_child is None)
print(bst.root.left_child.right_child.data == 1)

print(bst.max_value(bst.root.left_child) == 1)
print(bst.min_value(bst.root.right_child) == 10)

bst.traverse()

bst.delete(10)

bst.traverse()
