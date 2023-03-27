# About

The current repository contains the code for solving the missionaries and cannibals problem using Breadth First Search, Depth First Search, Greedy Best-First Search and A*.

The objective is to cross every missionary and every cannibal to the other side of the river without letting missionaries outnumbered by cannibals otherwise the missionaries will be eaten and the game ends!

# Instructions

The problem was solved using python 3, you must have it installed!

First, clone this repository

`git clone https://github.com/brigide/missionaries-cannibals-ai-search-algorithms`

Then, simply run 

`python main.py`


# State Representation

Examples of states:

- (0, 0, False) - Initial State
- (3, 3, True)  - Goal State

Where:
 - First param shows the quantity of missionaries on the correct side of the river;
 - Second param shows the quantity of cannibals on the correct side of the river;
 - Last param shows if the boat is at the correct side of the river.


# Implementation

All the data structures used where developed for this problem:

 - Queue (methods for enqueue and dequeue);
 - Stack (methods for push and pop);
 - Priority Queue (methods for enqueue and dequeue the most prior data - defined by heuristic/cost)


Some other classes where also created:

 - Node - Stores a state, it's parent and edges
 - State - Defines the state, calculate it's edges and validate if no violations occurred on a edge creation (such as outnumbered missionaries close to cannibals)
 - Path - Backtracks the solution and find the path from start to the solution


# Heuristic

`h(state) = 6 - (state.missionaries + state.cannibals)`