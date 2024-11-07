from django.db import models

# importing "heapq" to implement heap queue
import heapq

# ============ GOAL STATE & PUZZLE SIZE ============

Goal_State = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# Goal_State = [1, 2, 3, 4, 5, 6, 7, 8, 0]
Puzzle_Size = 3

ROW = COL = Puzzle_Size # Sets row and col to puzzle size

# Converts a dictionary of values into list format
def dictionary_to_list_converter(start):
    return [l['value'] for l in start]

# Enables us to check if the x and y positions of the values in any given node are within x == 0–2 and y == 0–2
def valid_position(row, col):
    return (row >= 0) and (row < ROW) and (col >= 0) and (col < COL)

# Converts a list of values into dictionary format
def list_to_dictionary_converter(chosen_config, Puzzle_Size):
  index = 0
  list_of_value_positions = [] # Contains a list of the positions of each value
  puzzle_dict = {}
  for x in range(Puzzle_Size):
    for y in range(Puzzle_Size):
      value = chosen_config[index] # Retrieves number from chosen configuration
      """
      puzzle_dict essentially allows us to more easily display the 8-puzzle on
      our Django app
      """
      puzzle_dict = {'style': 'cell', 'position': f"{x}-{y}", 'x': x, 'y': y, 'value': value}
      if value == 0 :
        puzzle_dict = {'style': 'cell-hidden', 'position': f"{x}-{y}", 'x': x, 'y': y, 'value': value}
      
      list_of_value_positions.append(puzzle_dict)
      index += 1
  return {'cells': list_of_value_positions} # 'cells' will be called upon by front-end


# Searches for mistmatches
def mismatch_keys(start_dict, goal_dict):
    # print(goal_dict)    
    start_list = [i['value'] for i in start_dict]
    goal_list = [l['value'] for l in goal_dict['cells']]
    mismatch_list = [i for i in range(len(goal_list)) if goal_list[i] != start_list[i]]
    return len(mismatch_list)


"""
Enables the start, middle, and goal states to be visually displayed

Note that 'data_puzzle' refers to the starting configuration chosen
by the user
"""
def emoji_puzzle(data_puzzle):
    emoji_list = [] # Stores list of emojis

    """
    This for loop translates the starting configuration from list
    format into their corresponding emojis
    """
    for key in data_puzzle.keys():
        inside = data_puzzle[key]

        """
        Appends the following emojis into emoji_list in the order the values
        are listed in starting configuration
        """
        for l in inside:
            v = l['value']
            if v == 0: val = '⬜'
            elif v == 1: val = '[1]'
            elif v == 2: val = '[2]'
            elif v == 3: val = '[3]'
            elif v == 4: val = '[4]'
            elif v == 5: val = '[5]'
            elif v == 6: val = '[6]'
            elif v == 7: val = '[7]'
            elif v == 8: val = '[8]'
            emoji_list.append(val)

        # Splits the list of emojis into three different lists
        emoji = []
        for key, value in grouped_into_three(emoji_list).items():
            emoji.append(value)

        # Prints the visualization of the 8-puzzle in its given state
        for string in emoji:
            print(string)

"""
• Splits the starting configuration in list format into three different lists
• Only called by the emoji_puzzle function
"""
def grouped_into_three(new_list):
    """
    Splits list into three different list

    Example:
    INPUT: [1, 2, 3, 4, 5, 6, 7, 8, 0]
    OUTPUT: [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    """
    grouped_list = [new_list[i:i + 3] for i in range(0, len(new_list), 3)]

    """
    Assigns each list in grouped_list its own dictionary key (the dictionary
    being new_values)
    """
    new_values = {}
    for index, chunk in enumerate(grouped_list, start=1):
        chunk = [str(item) for item in chunk]
        new_values[index] = ''.join(chunk)
    return new_values

def tracing_path(parents, start_values, current_values, f_score, heuristic):
    expanded_nodes_list = []
    while current_values != start_values:
        expanded_nodes_list.append(current_values)
        current_values = parents[tuple(current_values)]
    expanded_nodes_list.append(start_values)
    expanded_nodes_list.reverse()
    x = 0

    """
    Enables us to display a visualization of the 8-puzzle in a given state by...
    """
    for step in expanded_nodes_list:

        # 1) Showing the user the step number and the corresponding state reached by the algorithm in list format
        print(f"\nStep {x}: {step}")

        # 2) Triggers the emoji_puzzle function to create a visualization of the state reached by the algorithm
        emoji_puzzle(list_to_dictionary_converter(step, Puzzle_Size))

        # 3) Increases step number
        x += 1

    move = x
    print(f"Total Number of moves: {move}")
    print(f"F-score ({heuristic}): {f_score}")

    return f_score, move, expanded_nodes_list
# ============ SOLVING FOR HUERISTC and the Priority Function ============

def ManhattanDist(g_values, start_state, goal_state, puzzle_size):
  # Convert start_state and goal_state from lists to dictionaries
  start_dict = list_to_dictionary_converter(start_state, puzzle_size)['cells']
  goal_dict = list_to_dictionary_converter(goal_state, puzzle_size)['cells']
  total_sum = 0
  movements = []

  for tile in range(puzzle_size * puzzle_size):
      start_pos = None
      goal_pos = None

      # Find positions of the tile in both start and goal states
      for cell in start_dict:
          if cell['value'] == tile:
              start_pos = (cell['x'], cell['y'])
              break

      for cell in goal_dict:
          if cell['value'] == tile:
              goal_pos = (cell['x'], cell['y'])
              break

      # Calculate Manhattan distance for the tile
      if start_pos is not None and goal_pos is not None:
          manhattan_dist = abs(start_pos[0] - goal_pos[0]) + abs(start_pos[1] - goal_pos[1])
          total_sum += manhattan_dist
          movements.append(manhattan_dist)
      else:
          movements.append(0)

  """
  Start: 1 4 0 3 5 2 6 7 8
  Goal: 0 1 2 3 4 5 6 7 8
  Number movement for each tile: 2 1 1 0 1 1 0 0 0
  Total Sum of movements for each tile: 6
  """
  new_g = g_values
  new_h = total_sum
  new_f = new_g + new_h  # Total f-score (g + h)
  return new_g, new_h, new_f

  '''
  Source: https://www.geeksforgeeks.org/maximum-manhattan-distance-between-a-distinct-pair-from-n-coordinates/
  manhattan distance is equated as: |X1 - X2| + |Y1 - Y2|

  Source: https://stackoverflow.com/questions/39759721/calculating-the-manhattan-distance-in-the-eight-puzzle
  Understanding how to calculate the Manhattan
  '''

def HammingDist(g_values, current_cells, algorithm_goal):
  '''
  Calculate the Hamming distance heuristic for the A* algorithm.

  Parameters:
  - g_values: The current number of movements towards the goal.
  - new_cells: List of dictionaries representing the new puzzle configuration.
  '''
  new_g = g_values  # Number of movements towards the goal
  new_h = mismatch_keys(current_cells, algorithm_goal)  # MismatZch keys from the goal position
  new_f = new_g + new_h  # Total f-score (g + h)

  return new_g, new_h, new_f
  """

  Source: https://blog.goodaudience.com/solving-8-puzzle-using-a-algorithm-7b509c331288
  Followed the logic on how it is taken for the values of new_g, new_h, and new_f
  also use the basis of the figure made in the link as a visual reference for the mtf

  """


# ============ ALGORITHMS ============

def UCS(starting_configuration, algorithm_goal):

    heuristic = 'UCS'

    # Keeps track of all possible nodes
    frontier = []

    # Keeps track of all the explored nodes
    explored_nodes = []

    # Enables us to keep track of the path from starting configuration to goal state
    parents = {}

    # Keeps track of number of movements towards goal
    g_values = 0

    # Retrieves the starting configuration in dictionary form
    start_values = dictionary_to_list_converter(starting_configuration['cells'])

    """
    heapq.heappussh is a propoerty function that pushes an element onto the heap
    - It also sorts the nodes in the frontier by cost
    - frontier is being selected as the list for the heap
    - start_values presents the current configuration of the puzzle
    """
    heapq.heappush(frontier, (0.0, start_values, starting_configuration['cells']))

    while frontier: # Another way of saying "while True"/"while frontier not empty"
        """
        Removes and returns the smallest node from the frontier
        • current_f – refers to current f-score
        • current_values – refers to the current configuration of the puzzle
        in list format, e.g. [0, 1, 2, 3, 4, 5, 6, 7, 8]
        • current_puzzle – refers to the current configuration of the puzzle
        in dictionary format, e.g. {'position': '0-0', 'x': 0, 'y': 0, 'value': 0}
        """
        current_f, current_values, current_puzzle = heapq.heappop(frontier)

        # Marks the smallest node as having been explored and adds them to the dictionary for current_values
        explored_nodes.append(current_values)

        """
        Finds the empty cell in the node
        • empty cell is used assign where the current puzzle value is 0
        • the x and y values will be selected as the empty cells (for x as the row, and y as a column)
        """
        empty_cell = next(puzzle for puzzle in current_puzzle if puzzle['value'] == 0)
        x, y = empty_cell['x'], empty_cell['y']

        # current_values eventually leads to the goal state values stored in heapq
        if current_values == Goal_State:
            current_f, move, final_list = tracing_path(parents, start_values, current_values, new_f, heuristic)
            return current_f, move, final_list

        """
        POSSIBLE Directions: goes up, down, left, and right
        • up (x-coordinate decreases by 1)
        • down (x-coordinated increases by 1)
        • left (y-coordinate decrases by 1)
        • right (y-coordinate increases by 1)
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        g_values += 1 # Keeps track of number of movements towards goal (essentially our cost)

         # For each direction, check the successors
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            # Checks if successor is a valid move, e.g. does not push any of the cells out of the bounds of the 3x3 puzzle
            if valid_position(new_x, new_y):

                # Creates a new dictionary found in current_puzzle which is stored in heapq
                new_cells = [dict(cell) for cell in current_puzzle]

                # Identifies position of empty cell
                empty_index = next(i for i, cell in enumerate(new_cells) if cell['value'] == 0)

                """
                Identifies position of cell to be swapped
                - next() allows us to access the object associated to the enumerated variable
                - Source: https://www.geeksforgeeks.org/enumerate-in-python/
                """
                swap_index = next(i for i, cell in enumerate(new_cells) if cell['x'] == new_x and cell['y'] == new_y)

                """
                Switches positions of empty cell and the cell being swapped
                - Comma assignment is used to swap the two elements
                - Source: https://www.geeksforgeeks.org/python-program-to-swap-two-elements-in-a-list/
                """
                new_cells[empty_index]['value'], new_cells[swap_index]['value'] = new_cells[swap_index]['value'], new_cells[empty_index]['value']

                # Checks if successor has been explored yet
                new_values = dictionary_to_list_converter(new_cells)
                if new_values not in explored_nodes:
                    new_g = g_values
                    new_f = new_g
                    parents[tuple(new_values)] = current_values
                    heapq.heappush(frontier, (new_f, new_values, new_cells))

                    # print(f"f: {new_f}")
                    # print(f"g: {new_g}\n")
                    # print("h: 0")
                    # print(f"Open: {frontier}")

def A_Star(starting_configuration, algorithm_goal, heuristic):
    # Keeps track of all possible nodes
    frontier = []

    # Keeps track of all the explored nodes
    explored_nodes = []

    # Enables us to keep track of the path from starting configuration to goal state
    parents = {}

    # Keeps track of number of movements towards goal (essentially our cost)
    g_values = 0

    # Retrieves the starting configuration in dictionary form
    start_values = dictionary_to_list_converter(starting_configuration['cells'])

    # Sorts the nodes in the frontier by cost
    heapq.heappush(frontier, (0.0, start_values, starting_configuration['cells']))

    while frontier: # Another way of saying "while True"/"while frontier not empty"
        current_f, current_values, current_puzzle = heapq.heappop(frontier)

        # Marks the smallest node as having been explored
        explored_nodes.append(current_values)

        empty_cell = next(puzzle for puzzle in current_puzzle if puzzle['value'] == 0)
        x, y = empty_cell['x'], empty_cell['y']

        if current_values == Goal_State:
            current_f, move, final_list = tracing_path(parents, start_values, current_values, current_f, heuristic)
            return  current_f, move, final_list

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        g_values += 1

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy

            if valid_position(new_x, new_y):
                new_cells = [dict(cell) for cell in current_puzzle]

                empty_index = next(i for i, cell in enumerate(new_cells) if cell['value'] == 0)
                swap_index = next(i for i, cell in enumerate(new_cells) if cell['x'] == new_x and cell['y'] == new_y)

                new_cells[empty_index]['value'], new_cells[swap_index]['value'] = new_cells[swap_index]['value'], new_cells[empty_index]['value']

                new_values = dictionary_to_list_converter(new_cells)
                if new_values not in explored_nodes:
                    if heuristic == "Manhattan":
                        new_g, new_h, new_f = ManhattanDist(g_values, new_values, Goal_State, Puzzle_Size)
                    elif heuristic == "Hamming":
                        new_g, new_h, new_f = HammingDist(g_values, new_cells, algorithm_goal)
                    else:
                        # Default case to handle unexpected heuristic values
                        new_g = g_values
                        new_h = mismatch_keys(starting_configuration,  algorithm_goal)
                        new_f = new_g + new_h

                    parents[tuple(new_values)] = current_values
                    heapq.heappush(frontier, (new_f, new_values, new_cells))