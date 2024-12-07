# Search-Algorithm-Project
# This search algorithm is based on a previous project from CSCI 111 (Introduction to AI)

# This project primarily consists with the application of search algorithms such as Uninformed Search, Informed Search, A-Star Search, and  Uniform-Cost Search (UCS) for short. These algorithms are deployed through the visualization of a 8 puzzles. The 8 puzzle search is commonly used for search algorithms that will sort the puzzle according to the goal state that is declared. 

# The 8-puzzle is a sliding puzzle that elements within the 3x3 grid (numbers from 1-8 with an unlisted number) would be swapped. The goal of the puzzle is to rearrange the tiles into the correct order (goal state). 

#### Visualization of a 8-puzzle (current visualization will show the goal state)

#   | 1 | 2
# 3 | 4 | 5
# 6 | 7 | 8


# The initial state of the 8-puzzle refers to the starting arrangement of the tiles on the 3x3 grid. This state can vary depending on the specific puzzle configuration, but it typically consists of the numbers 1 through 8 arranged in a randomized order, with one blank space (representing the missing tile). Moreover, the program offers the set of moves that will be displayed to the user until the goal state has been reached. 

# Instructions

# Once loaded, please select the list of pre-determined combinations in the drop-down
# NOTE: We designed the program in a way that only takes in pre-determined combinations is to ensure that the program will not run for a long time. 

# Please select an option for the search tree. Once the search tree is selected, please choose an algorithm and a heuristics for the desired search tree (if you have chosen the option that is: Do Both UCS and A*. This would mean that the algorithm and heuristics has already been chosen)

# Once you click the Go For It Button below, the steps will be displayed below and alongside the heuristics and number of steps. Scroll down to view the steps that shows the swapping sequence and the last step will display the goal state.  


# Docker-and-Kubernetes-Deployment


Tech stack
If you don't like some of these choices that's no problem, you can swap them out for something else on your own.

Back-end
PostgreSQL
Redis
Celery
Front-end
esbuild
TailwindCSS
Heroicons




docker build -t gcr.io/group7-444005/group7-image:1.0.0 .

docker push gcr.io/group7-444005/group7-image:1.0.0

