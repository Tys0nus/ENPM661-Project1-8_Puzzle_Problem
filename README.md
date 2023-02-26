Project 1 - 8 Puzzle Problem
============================

This project is a Python implementation of the 8 puzzle problem using Breadth First Search algorithm.
- Sim Output:
![](https://github.com/Tys0nus/ENPM661-Project1-8_Puzzle_Problem/blob/main/sim/8%20Puzzzle%20Problem.gif)

Requirements
------------

-   Python 3.x

Dependencies
------------

-   numpy
-   collections
-   pygame

Usage
-----

-   Run the script main.py and press Enter.
-   The output files Nodes.txt, nodeInfo.txt and nodePath.txt will be generated in the same directory.

Files
-----

-   main.py: Execute this script. This script calls all the other scripts and displays visualization
-   BFSalgorithm.py: Source script that contains the code for the 8 puzzle problem using Breadth First Search algorithm.
-   visual.py: Script used for visualization of the implemented algorithm for the project
-   Nodes.txt: Output file that contains information about each node explored during the search. The file contains three(3) columns - C (node index), P (parent node index) and Node
-   nodePath.txt: Output file that contains the sequence of nodes in the path from the initial state to the goal state.
-   nodeInfo: Output file that contans sequence of explored nodes.

Notes
-----

-   The initial state and goal state are specified in the code. They can be changed by modifying the 'p' and 'goal' variables, respectively.
-   The code uses the numpy and collections libraries, which are imported at the beginning of the script.
-   The parse_goal and parse_p variables are used to flatten the matrices into arrays for easier manipulation. They are reshaped back into matrices when necessary.
-   The tracking function is used to generate the path for traversing from initial node to goal node.

Tested Environment

------------------

The code has been tested using Python 3.10.

Author
------

Aditya Chaugule\
Graduate Student\
Master of Engineering in Robotics\
University of Maryland, College park

