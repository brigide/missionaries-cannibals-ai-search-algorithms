class Stack:
    """Stack data structure"""
    def __init__(self):
        self.values = []

    def push(self, value):
        self.values.append(value)

    def pop(self):
        return self.values.pop()

    def get_values(self):
        return self.values