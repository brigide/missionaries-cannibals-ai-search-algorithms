from structures.stack import Stack
from utils.node import Node
from utils.path import get_path


def DFS(initial_state, goal_state):
    stack = Stack()
    initial_node = Node(initial_state)
    visited_states = Stack()
    explored_count = 1

    stack.push(initial_node)

    print('Searching for a path...')
    while len(stack.get_values()) > 0:
        print('stack: ', end='')
        [print(f'{e.__str__()} ', end='') for e in stack.get_values()]
        print()
        current_node = stack.pop()
        print(f'current: {current_node.__str__()}')
        print()

        current_node.set_searched() # this trigger the function to define this node's edges
        visited_states.push(current_node)

        if current_node.is_equal_to(goal_state):
            print('Goal found!')
            get_path(current_node)
            break

        edges = current_node.edges
        for e in edges:
            if not e.searched and not stack.has_value(e) and not visited_states.has_value(e):
                explored_count += 1
                e.parent = current_node
                stack.push(e)
