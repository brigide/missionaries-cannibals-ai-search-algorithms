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
    
    def has_value(self, node):
        for value in self.values:
            if value.state.is_equal_to(node.state):
                return True
            
        return False
