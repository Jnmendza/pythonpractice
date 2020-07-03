class Stack():
    def __init__(self):
        self.data = []
        
    def push(self, item):
        self.data.append(item)

    def pop(self):
        return self.data.pop()

    def is_empty(self):
        return self.data == []

    def peek(self):
        if not self.is_empty():
            return self.data[-1]

    def get_stack(self):
        return self.data

