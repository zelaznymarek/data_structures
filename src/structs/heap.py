class MaxHeap:
    def __init__(self):
        self.heap = []
        self.heap_size = 0

    def insert(self, data):
        self.heap[self.heap_size] = data
        self.heap_size += 1

        self.fix_up(self.heap_size - 1)

    def get_max(self):
        return self.heap[0]

    def poll(self):
        max_value = self.get_max()

        self.swap(0, self.heap_size - 1)
        self.heap_size -= 1

        self.fix_down(0)

        return max_value

    def heap_sort(self):
        for i in range(self.heap_size):
            print(self.poll())

    def fix_up(self, index):
        parent_index = (index - 1) // 2

        if index > 0 and self.heap[index] > self.heap[parent_index]:
            self.swap(index, parent_index)
            self.fix_up(parent_index)

    def fix_down(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        max_index = index

        if left_index < self.heap_size and self.heap[left_index] > self.heap[max_index]:
            max_index = left_index

        if right_index < self.heap_size and self.heap[right_index] > self.heap[max_index]:
            max_index = right_index

        if max_index != index:
            self.swap(index, max_index)
            self.fix_down(max_index)

    def swap(self, index_1, index_2):
        self.heap[index_1], self.heap[index_2] = self.heap[index_2], self.heap[index_1]


heap = MaxHeap()

heap.insert(10)
heap.insert(12)
heap.insert(8)
heap.insert(-2)
heap.insert(23)
heap.insert(14)

heap.heap_sort()
