POSSIBLE_MISSIONARY_COMBINATIONS = {
    '03': '         |      |  M M M  ',
    '12': '  M      |      |  M M    ',
    '21': '  M M    |      |  M      ',
    '30': '  M M M  |      |         ',
}
POSSIBLE_CANNIBAL_COMBINATIONS = {
    '03': '         |      |   C C C ',
    '12': '   C     |      |   C C   ',
    '21': '   C C   |      |   C     ',
    '30': '   C C C |      |         ',
}

POSSIBLE_BOAT_COMBINATIONS = {
    False: '         |__    |         ',
    True:  '         |    __|         ',
}

MISSIONARY_LIMIT = 3
CANNIBAL_LIMIT = 3

def draw_solution(path):
    """Draw the found path on console"""
    for step in path:
        missionary_on_left = MISSIONARY_LIMIT - step.state.missionaries
        missionary_on_right = step.state.missionaries
        missionary_key_string = f'{missionary_on_left}{missionary_on_right}'

        cannibal_on_left = CANNIBAL_LIMIT - step.state.cannibals
        cannibal_on_right = step.state.cannibals
        cannibal_key_string = f'{cannibal_on_left}{cannibal_on_right}'

        boat_position = step.state.boat

        full_state_drawing = f"""
        {step.__str__()}

        {POSSIBLE_MISSIONARY_COMBINATIONS[missionary_key_string]}
        {POSSIBLE_BOAT_COMBINATIONS[boat_position]}
        {POSSIBLE_CANNIBAL_COMBINATIONS[cannibal_key_string]}"""

        print(full_state_drawing)
        print()
        print('Press ENTER for next step')
        input('')

    print('GOAL REACHED!')


def get_path(node): 
    """Backtrack parent to parent until connects start to finish"""
    print('Path:')
    path = []
    path.append(node)
    next = node.parent
    while next != None:
        path.append(next)
        next = next.parent

    path.reverse()
    for step in path:
        print(step.__str__())

    print()
    print("""Want to see a graphical representation for the found solution?
    
            1. Yes
            0. No
        """)
    
    choice = int(input('Choose an option: '))

    if choice == 1:
        draw_solution(path)
