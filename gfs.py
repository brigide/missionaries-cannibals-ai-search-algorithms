from structures.stack import Stack
from utils.node import Node
from structures.priority_queue import PriorityQueue
from utils.path import get_path


def GreedyBFS(initial_state, goal_state):
    queue = PriorityQueue()
    initial_node = Node(initial_state)
    explored_states = Stack()
    explored_states.push(initial_node)
    visited_states = 0

    initial_node.set_searched()
    initial_node.set_heuristics(heuristics(initial_node.state))
    queue.enqueue(initial_node)

    print('Searching for a path...')
    while len(queue.get_values()) > 0:
        print('queue: ', end='')
        [print(f'{e.__str__(True)} ', end='') for e in queue.get_values()]
        print()
        current_node = queue.dequeue()
        visited_states += 1
        print(f'current: {current_node.__str__(True)}')
        print()

        if current_node.is_equal_to(goal_state):
                print('Goal found!')
                get_path(current_node)
                break

        edges = current_node.edges
        for e in edges:
            if not e.searched and not queue.has_value(e) and not explored_states.has_value(e):
                e.set_searched()
                e.set_heuristics(heuristics(e.state))
                explored_states.push(e)
                e.parent = current_node
                queue.enqueue(e)


def heuristics(state):
    return 6 - ((state.missionaries + state.cannibals))