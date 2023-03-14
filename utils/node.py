from .state import State

class Node:
    def __init__(self, state):
        self.state = state
        self.edges = []
        self.searched = False
        self.parent = None

    def set_searched(self):
        self.searched = True
        if self.state.is_valid():
            self.calculate_edges()

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

    def __str__(self) -> str:
        return f'state: {self.state.__str__()}'
