from structures.stack import Stack
from utils.node import Node
from structures.queue import Queue
from utils.path import get_path
from utils.state import State

def BFS(initial_state, goal_state):
    queue = Queue() # defining a queue
    initial_node = Node(initial_state) # instance the starting node
    explored_states = Stack() # instance a explored state as stack
    explored_states.push(initial_node) # includes starting node
    visited_states = 0 # to counting purposes only

    initial_node.set_searched() # this trigger the function to define this node's edges
    queue.enqueue(initial_node) # add node to the queue

    print('Searching for optimal path...')
    # if queue gets empty, no solution was found
    while len(queue.get_values()) > 0:
        print('queue: ', end='')
        [print(f'{e.__str__()} ', end='') for e in queue.get_values()]
        print()
        current_node = queue.dequeue() # get the fisrt element on queue
        visited_states += 1 # to counting purposes only
        print(f'current: {current_node.__str__()}')

        # check if goal was found
        if current_node.is_equal_to(goal_state):
            print('Goal found!')
            print(f'Explored {len(explored_states.get_values())} nodes')
            print(f'Visited {visited_states} nodes')
            get_path(current_node)
            break

        # loop through current node possible actions
        edges = current_node.edges
        for e in edges:
            # check if the edge has been searched, is not on queue (will be explored soon) and if any similar state has been explored
            if not e.searched and not queue.has_value(e) and not explored_states.has_value(e):
                e.set_searched()
                explored_states.push(e)
                e.parent = current_node # set the parent
                queue.enqueue(e)
