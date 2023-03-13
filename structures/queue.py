class Queue:
    """Queue data structure"""
    def __init__(self):
        self.values = []

    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        return self.values.pop(0)

    def get_values(self):
        return self.values