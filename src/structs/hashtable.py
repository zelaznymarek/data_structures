# Hashtable with linear probing collision solver
class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash(self, key):
        if isinstance(key, int):
            return key % self.size

        sum = 0

        for char in key:
            sum += ord(char)

        return sum % self.size

    def probe_next_index(self, index):
        if index == self.size - 1:
            return 0

        return index + 1

    def put(self, key, value):
        index = self.hash(key)

        while self.keys[index] is not None:
            if self.keys[index] == key:
                self.values[index] = value
                return

            index = self.probe_next_index(index)

        self.values[index] = value
        self.keys[index] = key

    def get(self, key):
        index = self.hash(key)

        for i in range(self.size):
            if self.keys[index] and self.keys[index] == key:
                return self.values[index]

            index = self.probe_next_index(index)

        return


ht = HashTable(11)

ht.put('zero', 0)
ht.put('one', 1)
ht.put('two', 2)
ht.put('three', 3)
ht.put('four', 4)
ht.put('five', 5)
ht.put('six', 6)
ht.put('seven', 7)
ht.put('eight', 8)
ht.put('nine', 9)
ht.put(10, 10)

print(ht.get('eleven') is None)
print(ht.get('four') == 4)
print(ht.get('zero') == 0)

ht.put('four', 44)
print(ht.get('four') == 44)

print(ht.get(10) == 10)

print(ht.keys)
