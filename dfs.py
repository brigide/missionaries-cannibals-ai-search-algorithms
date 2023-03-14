from structures.stack import Stack
from utils.node import Node
from utils.path import get_path


def DFS(initial_state, goal_state):
    stack = Stack()
    initial_node = Node(initial_state)
    explored_states = Stack()
    explored_states.push(initial_node)

    initial_node.set_searched()
    stack.push(initial_node)

    print('Searching for a path...')
    while len(stack.get_values()) > 0:
        print('stack: ', end='')
        [print(f'{e.__str__()} ', end='') for e in stack.get_values()]
        print()
        current_node = stack.pop()
        print(f'current: {current_node.__str__()}')

        if current_node.is_equal_to(goal_state):
            print('Goal found!')
            get_path(current_node)
            break

        edges = current_node.edges
        for e in edges:
            if not e.searched and not stack.has_value(e) and not explored_states.has_value(e):
                e.set_searched()
                explored_states.push(e)
                e.parent = current_node
                stack.push(e)
