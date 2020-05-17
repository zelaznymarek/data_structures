class Node:
    def __init__(self, character):
        self.character = character
        self.left_child = None
        self.middle_child = None
        self.right_child = None
        self.value = None


class TST:
    def __init__(self):
        self.root = None

    def insert(self, key, value):
        self.root = self.insert_item(self.root, key, value, 0)

    def insert_item(self, node, key, value, index):
        c = key[index]

        if not node:
            node = Node(c)

        if c < node.character:
            node.left_child = self.insert_item(node.left_child, key, value, index)
        elif c > node.character:
            node.right_child = self.insert_item(node.right_child, key, value, index)
        elif index < len(key) - 1:
            node.middle_child = self.insert_item(node.middle_child, key, value, index + 1)
        else:
            node.value = value

        return node

    def get(self, key):
        node = self.get_item(self.root, key, 0)

        if not node:
            return

        return node.value

    def get_item(self, node, key, index):
        if not node:
            return

        c = key[index]

        if c < node.character:
            return self.get_item(node.left_child, key, index)
        if c > node.character:
            return self.get_item(node.right_child, key, index)
        if index < len(key) - 1:
            return self.get_item(node.middle_child, key, index + 1)

        return node


tst = TST()

tst.insert('one', 1)
tst.insert('two', 2)
tst.insert('three', 3)

print(tst.get('two') == 2)
print(tst.get('three') == 3)
print(tst.get('threee') is None)

