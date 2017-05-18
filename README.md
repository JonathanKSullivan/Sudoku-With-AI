# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *We iterate through each position find its peers. We then check the peers of that position for Naked Twins. If twins are found we reiterate through the peer group and remove each of the individual twins from the  peers that contain them. Here we use the fact that naked twin means that those two spaces are the only spaces in a peer group that can contain those values.*

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *We use 4 methods of constraint propagation to solve the Diagonal Sudoku problem. First we use a technique called Elimination which looks at the solve positions and determine the possible answers for unsolved positions. Second we used Only Choice, which looks at a position peer group and determine if a possibility is unique to its position within a its peer group. If so then we know that the value for that position is that unique possibility. Third we used the naked twin approach which is describe above(see Q1; [DRY]). This could be abstracted to higher levels of siblings; we could implement Naked Triplets, Naked Quadruplets, Naked Quintets, etc. Lastly we wrap all these up in a DFS.*

### Install

This project requires **Python 3**.

Installing [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project.

##### Optional: Pygame
Optionally, you can also install [pygame](http://www.pygame.org/download.shtml). if you want to see the visualization.

### Code

* `solutions.py` - I filled in the methods in this file.
* `solution_test.py` - This file was provided by Udacity. You can test my solution by running `python solution_test.py`.
* `PySudoku.py` - This file was provided by Udacity. This is code for visualizing your solution.
* `visualize.py` - This file was provided by Udacity. This is code for visualizing your solution.
