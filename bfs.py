from utils.node import Node
from structures.queue import Queue
from utils.path_representation import draw_solution
from utils.state import State

def BFS(initial_state, goal_state):
    queue = Queue()
    explored_states = []
    initial_node = Node(initial_state)

    initial_node.set_searched()
    queue.enqueue(initial_node)

    print('Searching for optimal path...')
    while len(queue.get_values()) > 0:
        current_node = queue.dequeue()

        if current_node.is_goal(goal_state):
            print('Goal found!')
            get_path(current_node)
            break

        edges = current_node.edges
        for e in edges:
            if not e.searched and e not in queue.get_values() and e not in explored_states:
                e.set_searched()
                explored_states.append(e)
                e.parent = current_node
                queue.enqueue(e)


def get_path(node): 
    print('Path:')
    path = []
    path.append(node)
    next = node.parent
    while next != None:
        path.append(next)
        next = next.parent

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

    else: 
        pass

