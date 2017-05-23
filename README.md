# Artificial Intelligence Engineer Nanodegree
## Introductory Project
### Diagonal Sudoku Solver

In this project, I wrote code to implement two extensions of Udacity's sudoku solver. The first implementation is the technique called "[naked twins](http://www.sudokudragon.com/tutorialnakedtwins.htm)". The second one was modifing their existing code to solve a diagonal sudoku. I implemented the naked twins function, and wrote an AI agent that will solve the Diagonal Sudoku game.

#### Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: *We iterate through each position find its peers. We then check the peers of that position for Naked Twins. If twins are found we reiterate through the peer group and remove each of the individual twins from the  peers that contain them. Here we use the fact that naked twin means that those two spaces are the only spaces in a peer group that can contain those values.*

#### Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: *We use 4 methods of constraint propagation to solve the Diagonal Sudoku problem. First we use a technique called Elimination which looks at the solve positions and determine the possible answers for unsolved positions. Second we used Only Choice, which looks at a position peer group and determine if a possibility is unique to its position within a its peer group. If so then we know that the value for that position is that unique possibility. Third we used the naked twin approach which is describe above(see Q1; [DRY]). This could be abstracted to higher levels of siblings; we could implement Naked Triplets, Naked Quadruplets, Naked Quintets, etc. Lastly we wrap all these up in a DFS.*

### Code

* `solutions.py` - I filled in the methods in this file.
* `solution_test.py` - This file was provided by Udacity. You can test my solution by running `python solution_test.py`.
* `PySudoku.py` - This file was provided by Udacity. This is code for visualizing your solution.
* `visualize.py` - This file was provided by Udacity. This is code for visualizing your solution.



## Getting Started

To get this code on your machine you can fork the repo or open a terminal and run this command.
```sh
git clone https://github.com/JonathanKSullivan/Sudoku-With-AI.git
```

### Prerequisites

This project requires **Python 3**:

##### Notes:
1. It is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python and load the environment included below.
I used pygame to help me visualize mu programs so that I have beautiful visualizations of AI I can share with others in your portfolio. However, pygame is optional as it can be tricky to install.

### Installing
#### Mac OS X and Linux
1. Download the `aind-environment-unix.yml/aind-environment-unix.yml`/`aind-environment-osx.yml` file at the bottom of this section.
2. Run `conda env create -f aind-environment-unix.yml`(or `aind-environment-osx.yml`) to create the environment.
then source activate aind to enter the environment.

#### Windows
1. Download the `aind-environment-windows.yml` file at the bottom of this section.
2. `conda env create -f aind-environment-windows.yml` to create the environment.
then activate aind to enter the environment.
3. Install the development version of hmmlearn 0.2.1 in one of the following ways.
    ##### Source build
    1. Download the Visual C++ Build Tools [here](http://landinghub.visualstudio.com/visual-cpp-build-tools).
    `pip install git+https://github.com/hmmlearn/hmmlearn.git`
    ##### Precompiled binary wheel
    1. Download the appropriate `hmmlearn-0.2.1-yourpythonwindows.whl` file from here
    2. Install with `pip install hmmlearn-0.2.1-yourpythonwindows.whl`.

#### Optional: Install Pygame
I used pygame to help you visualize my programs so that I have beautiful visualizations of AI I can share with others in my portfolio.
##### Mac OS X
1. Install [homebrew](http://brew.sh/)
2. `brew install sdl sdl_image sdl_mixer sdl_ttf portmidi mercurial`
3. `source activate aind`
4. `pip install pygame`
Some users have reported that pygame is not properly initialized on OSX until you also run `python -m pygame.tests`.

Windows and Linux
1. `pip install pygame`
2. In Windows, an alternate method is to install a precompiled binary wheel:
    1. Download the appropriate `pygame-1.9.3-yourpythonwindows.whl` file from here
    2. Install with `pip install pygame-1.9.3-yourpythonwindows.whl`.


Download the one of the following yml files:
- [aind-environment-osx.yml](https://d17h27t6h515a5.cloudfront.net/topher/2017/April/58ee7e68_aind-environment-macos/aind-environment-macos.yml)
- [aind-environment-unix.yml](https://d17h27t6h515a5.cloudfront.net/topher/2017/April/58ee7eff_aind-environment-unix/aind-environment-unix.yml)
- [aind-environment-windows.yml](https://d17h27t6h515a5.cloudfront.net/topher/2017/April/58ee7f6c_aind-environment-windows/aind-environment-windows.yml)

## Running the tests

Test are included in notebook. To run test from terminal, navigate to project directory and run
```sh
    python solution_test.py
```

## Deployment
To run test from terminal, navigate to project directory and run
```sh
    python solution.py
```

## Built With
* [Anaconda](https://www.continuum.io/downloads) - The data science platform used

## Authors
* **Udacity** - *Initial work* - [AIND-Isolation](https://github.com/udacity/AIND-Isolation)
* **Jonathan Sulivan**

## Acknowledgments
* Hackbright Academy
* Udacity
