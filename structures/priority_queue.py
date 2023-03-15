class PriorityQueue:
    def __init__(self):
        self.values = []

    def get_values(self):
        return self.values
    
    def enqueue(self, value):
        self.values.append(value)

    def dequeue(self):
        min_value = 999
        index = -1
        for value in self.values:
            if value.heuristic_value < min_value:
                min_value = value.heuristic_value
                index = self.values.index(value)

        return self.values.pop(index)
    
    def has_value(self, node):
        for value in self.values:
            if value.state.is_equal_to(node.state):
                return True
            
        return False
