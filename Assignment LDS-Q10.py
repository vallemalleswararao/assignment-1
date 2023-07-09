class Stack:
    def __init__(self):
        self.items = []
        self.min_element = None

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        if self.is_empty() or item < self.min_element:
            self.min_element = item
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            item = self.items.pop()
            if item == self.min_element:
                self.update_min_element()
            return item

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def update_min_element(self):
        if self.is_empty():
            self.min_element = None
        else:
            self.min_element = min(self.items)

    def get_smallest_element(self):
        return self.min_element


# Test the stack for smallest number
stack = Stack()

num_elements = int(input("Enter the number of elements for the stack: "))

for _ in range(num_elements):
    item = int(input("Enter an element: "))
    stack.push(item)

print("Smallest element:", stack.get_smallest_element())