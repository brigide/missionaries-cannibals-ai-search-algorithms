from bfs import BFS
from utils.state import State

def main():
    print("""      
            Welcome to the Missionaries and Cannibals problem!
    
            The objective is to cross every missionary and every cannibal 
            to the other side of the river without letting missionaries outnumbered
            by cannibals otherwise the missionaries will be eaten and the game ends!

            This program was built to solve this problem using 4 diffrent
            AI algorithms.

            Please choose one to start!

            1. Breadth-First Search
            2. Depth-First Search
            3. Greedy Search
            4. A*

            0. Exit

            """)

    choice = int(input('Please, choose an option: '))

    INITIAL_STATE_TUPLE = State(0, 0, False)
    GOAL_STATE_TUPLE = State(3, 3, True)

    if choice == 1:
        BFS(INITIAL_STATE_TUPLE, GOAL_STATE_TUPLE)

    elif choice == 2:
        pass
    elif choice == 3:
        pass
    elif choice == 4:
        pass
    else:
        pass

if __name__ == '__main__':
    main()