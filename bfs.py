from structures.stack import Stack
from utils.node import Node
from structures.queue import Queue
from utils.path import get_path
from utils.state import State

def BFS(initial_state, goal_state):
    queue = Queue()
    initial_node = Node(initial_state)
    explored_states = Stack()
    explored_states.push(initial_node)
    visited_states = 0

    initial_node.set_searched()
    queue.enqueue(initial_node)

    print('Searching for optimal path...')
    while len(queue.get_values()) > 0:
        print('queue: ', end='')
        [print(f'{e.__str__()} ', end='') for e in queue.get_values()]
        print()
        current_node = queue.dequeue()
        visited_states += 1
        print(f'current: {current_node.__str__()}')

        if current_node.is_equal_to(goal_state):
            print('Goal found!')
            print(f'Explored {len(explored_states.get_values())} nodes')
            print(f'Visited {visited_states} nodes')
            get_path(current_node)
            break

        edges = current_node.edges
        for e in edges:
            if not e.searched and not queue.has_value(e) and not explored_states.has_value(e):
                e.set_searched()
                explored_states.push(e)
                e.parent = current_node
                queue.enqueue(e)
