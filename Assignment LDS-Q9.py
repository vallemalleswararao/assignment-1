class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def reverse(self):
        aux_stack = Stack()

        while not self.is_empty():
            item = self.pop()
            aux_stack.push(item)

        self.items = aux_stack.items


# Test the stack reversal
stack = Stack()

num_elements = int(input("Enter the number of elements for the stack: "))

for _ in range(num_elements):
    item = input("Enter an element: ")
    stack.push(item)

print("Original stack:", stack.items)

stack.reverse()

print("Reversed stack:", stack.items)