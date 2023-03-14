MISSIONARY_LIMIT = 3
CANNIBAL_LIMIT = 3

class State:
    """This class represents a single state of the M and C problem"""
    def __init__(self, missionaries, cannibals, boat):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.actions = self.get_state_possible_actions()

    def has_more_cannibals_on_wrong_side(self):
        """This method checks if C outnumber M at wrong side"""
        return ((self.missionaries == 2 and self.cannibals == 1) or
                (self.missionaries == 1 and self.cannibals == 0) or 
                (self.missionaries == 2 and self.cannibals == 0))

    def has_more_cannibals_on_correct_side(self):
        """This method checks if C outnumber M at correct side"""
        return ((self.missionaries == 1 and self.cannibals == 3) or
                (self.missionaries == 2 and self.cannibals == 3) or
                (self.missionaries == 1 and self.cannibals == 2))

    def is_valid(self):
        """This method checks if the current state is valid"""

        # checks if the number of M or C outnumber it's limit
        if self.missionaries > MISSIONARY_LIMIT or self.missionaries < 0:
            return False
        if self.cannibals > CANNIBAL_LIMIT or self.cannibals < 0:
            return False

        # check if there is more C than M at any side
        if self.has_more_cannibals_on_wrong_side():
            return False
        if self.has_more_cannibals_on_correct_side():
            return False

        return True

    @staticmethod
    def get_all_possible_actions():
        """Method that list all possible moves on the problem (every action changes side)"""
        return [
            [2, 0], # move: 2 missionary, 0 cannibals
            [1, 0], # move: 1 missionary, 0 cannibals
            [1, 1], # move: 1 missionary, 1 cannibals
            [0, 1], # move: 0 missionary, 1 cannibals
            [0, 2]  # move: 0 missionary, 2 cannibals
        ]


    def get_state_possible_actions(self):
        """This method gets all possible actions and filter depending the boat
            direction and number os missionaries and canniblas"""
        
        # fetching all possible actions
        all_actions = self.get_all_possible_actions()
        actions = []

        # check if the boat is where it should be (at the end)
        # if the number of M or C at the correct side (number represented by state)
        # is greater than the current action, the algo keep it
        # ex: we have 1 M and 1 C at correct side we should filter only those actions:
        # (1, 0), (1, 1), (0, 1)
        if self.is_boat_on_correct_side():
            for action in all_actions:
                if self.missionaries >= action[0] and self.cannibals >= action[1]:
                    action.append(not self.is_boat_on_correct_side())
                    actions.append(action)

        # the same logic applies when boat is at start position but
        # we have to subtract the number of M and C by the max number of M or C 
        # to get the number of M and C on the wrong side of the river
        else:
            for action in all_actions:
                if ((MISSIONARY_LIMIT - self.missionaries >= action[0]) and
                    (CANNIBAL_LIMIT - self.cannibals >= action[1])):
                    action.append(not self.is_boat_on_correct_side())
                    actions.append(action)

        return actions


    def is_boat_on_correct_side(self):
        """This method checks and returns if the boat is currently on the correct side"""
        return self.boat

    def is_equal_to(self, state):
        if self.missionaries != state.missionaries:
            return False

        if self.cannibals != state.cannibals:
            return False

        if self.boat != state.boat:
            return False

        return True

    def __str__(self) -> str:
        return f'({self.missionaries}, {self.cannibals}, {self.boat})'

