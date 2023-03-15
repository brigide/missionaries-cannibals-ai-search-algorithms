from .state import State

class Node:
    def __init__(self, state):
        self.state = state
        self.edges = []
        self.searched = False
        self.parent = None
        self.heuristic_value = None

    def set_searched(self):
        self.searched = True
        if self.state.is_valid():
            self.calculate_edges()

    def set_heuristics(self, value):
        self.heuristic_value = value

    def is_equal_to(self, goal):
        return self.state.is_equal_to(goal)


    def calculate_edges(self):
        for action in self.state.actions:
            # if boat is going to goal (True)
            if action[2]:
                self.edges.append(Node(
                    State(
                        missionaries=self.state.missionaries + action[0],
                        cannibals=self.state.cannibals + action[1],
                        boat=action[2]
                    )
                ))

            else:
                self.edges.append(Node(
                    State(
                        missionaries=self.state.missionaries - action[0],
                        cannibals=self.state.cannibals - action[1],
                        boat=action[2]
                    )
                ))

    def __str__(self, show_heuristic = False) -> str:
        if show_heuristic:
            return f'{self.state.__str__(self.heuristic_value)}'
        
        return f'{self.state.__str__(None)}'
