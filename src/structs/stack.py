class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.size():
            return self.stack.pop(-1)

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# tests

stack = Stack()

print(stack.is_empty())

stack.push(1)
stack.push(2)
stack.push(3)

print(not stack.is_empty())

print(stack.stack == [1, 2, 3])

item = stack.pop()

print(item == 3)
print(stack.stack == [1, 2])

item = stack.peek()

print(item == 2)
print(stack.stack == [1, 2])

stack.pop()
stack.pop()

print(stack.is_empty())

none = stack.pop()

print(none is None)
