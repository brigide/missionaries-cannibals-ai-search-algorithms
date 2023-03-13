from utils.node import Node
from structures.queue import Queue
from utils.state import State

def BFS(initial_state, goal_state):
    queue = Queue()
    explored_states = []
    initial_node = Node(initial_state)

    initial_node.set_searched()
    queue.enqueue(initial_node)

    while len(queue.get_values()) > 0:
        current_node = queue.dequeue()

        if current_node.is_goal(goal_state):
            print('Goal found!')
            get_path(current_node)
            break

        edges = current_node.edges
        for e in edges:
            print(e.__str__())
            if not e.searched and e not in queue.get_values() and e not in explored_states:
                e.set_searched()
                explored_states.append(e)
                e.parent = current_node
                queue.enqueue(e)
                

def get_path(node): 
    path = []
    path.append(node)
    next = node.parent
    while next != None:
        path.append(next)
        next = next.parent

    for i in path:
        print(i.__str__())