class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_at_start(self, data):
        new_node = Node(data)
        self.size += 1

        if not self.head:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        self.size += 1
        actual_node = self.head

        while actual_node.next_node is not None:
            actual_node = actual_node.next_node

        actual_node.next_node = new_node

    def traverse(self):
        actual_node = self.head

        while actual_node is not None:
            print(actual_node.data, end=' ')
            actual_node = actual_node.next_node

    def remove(self, data):
        if self.head is None:
            return

        actual_node = self.head
        previous_node = None

        while actual_node.data != data:
            if not actual_node.next_node:
                print(f'Value {data} not found.')
                return

            previous_node = actual_node
            actual_node = actual_node.next_node

        self.size -= 1

        if previous_node:
            previous_node.next_node = actual_node.next_node
        else:
            self.head = actual_node.next_node

    def size_of(self):
        return self.size


linked_list = LinkedList()
print(linked_list.size_of() == 0)

linked_list.insert_at_start(10)
linked_list.insert_at_start(13)
linked_list.insert_at_end(15)
linked_list.insert_at_end(27)
print(linked_list.head.data == 13)
print(linked_list.size_of() == 4)

linked_list.remove(100)
print(linked_list.size_of() == 4)

linked_list.remove(10)
print(linked_list.head.data == 13)
print(linked_list.size_of() == 3)

linked_list.remove(13)
print(linked_list.head.data == 15)
print(linked_list.size_of() == 2)

linked_list.remove(27)
print(linked_list.head.data == 15)
print(linked_list.size_of() == 1)

linked_list.remove(15)
print(linked_list.head is None)
print(linked_list.size_of() == 0)
