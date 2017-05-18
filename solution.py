import copy
import string

assignments = []

### Setup
board_rows = string.ascii_uppercase[0:9]
board_cols = string.digits[1:10]
subboard_rows = [board_rows[0:3], board_rows[3:6],board_rows[6:9]]
subboard_cols = [board_cols[0:3], board_cols[3:6],board_cols[6:9]]
subboards = [[r+c for r in sub_row for c in sub_col] for sub_row in subboard_rows \
              for sub_col in subboard_cols]
diagonals = [[board_rows[i] + board_cols[i] for i in range(9)], [board_rows[i] + \
              board_cols[8-i] for i in range(9)]]
peer_groups = {}

#Creates a list of list of rows
rows = [ [board_row+board_col for board_col in board_cols] for board_row in board_rows]

#Creates a list of list of column
cols = [[board_row+board_col for board_row in board_rows] for board_col in board_cols]

def strIntersection(s1, s2):
  out = ""
  for c in s1:
    if c in s2 and not c in out:
      out += c
  print (''.join([c for c in s1 if (c in s2 and not c in out)]), out)
  return ''.join([c for c in s1 if c in s2 and not c in out])
  return out

def get_all_peer_grp(values):
    """
    Generate a dictionary of peer groups.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        a dictionary of the form {'A1': ['A2','A3',..], ...}
    """
    #One time function to generate fast look up for peer groups later
    pd = {}
    for value in values:
        pd[value] = get_peer_grp(value)
    return pd

def get_peer_grp(value):
    """
    Given a position this function returns a list of position in its peer group.
    Args:
        value(str): a string of the form 'A1'

    Returns:
        the positions list with the peers.
    """

    peer_grp = []

    # add member of target box row to peer group list
    for row in rows:
        if value in row:
            peer_grp += row

    # add member of target box column to peer group list
    for col in cols:
        if value in col:
            peer_grp += col

    # add member of target box subboard to peer group list
    for subboard in subboards:
        if value in subboard:
            peer_grp += subboard

    # add member of target box diagonal if applicable to peer group list
    for diagonal in diagonals:
        if value in diagonal:
            peer_grp += diagonal

    return peer_grp

### Main Logic
def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """
    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    global peer_groups
    if peer_groups == {}:
        peer_groups = get_all_peer_grp(values)
    for value in values:
        if (len(values[value]) == 2):
            peer_group = peer_groups[value]
            for peer in peer_group:
                if ( peer != value ) and ( values[peer] == values[value] ):
                    for cell_to_replace in list(set(peer_groups[value]).intersection(set(peer_groups[peer]))):
                        if ( cell_to_replace != peer and cell_to_replace != value ) and \
                        (values[peer][0] in  values[cell_to_replace] or values[peer][1] in values[cell_to_replace]) and \
                        len(values[cell_to_replace]) > 2:
                            assign_value(values, cell_to_replace, values[cell_to_replace].replace(values[peer][0],''))
                            assign_value(values, cell_to_replace, values[cell_to_replace].replace(values[peer][1],''))
    return values

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [b+a for b in B for a in A]

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    grid_dict = {}
    for n, box in enumerate(cross(board_cols, board_rows)):
        entry = '123456789' if grid[n] == '.' else grid[n]
        grid_dict[box] = entry

    global peer_groups
    peer_groups = get_all_peer_grp(grid_dict)
    return grid_dict

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1+max(len(values[s]) for s in cross(board_cols, board_rows))
    line = '+'.join(['-'*(width*3)]*3)
    for r in board_rows:
        print(''.join(values[r+c].center(width)+('|' if c in '36' else '')
                      for c in board_cols))
        if r in 'CF': print(line)
    return


def eliminate(values):
    """
    Eliminate values that are not possibile.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the eliminated values from peers.
    """
    for value in values:
        # Removes potential answers from a target box that are valid solutions for peers
        seen_buffer = ''
        value_buffer = ''
        if len(values[value]) > 1:
            # add to targets seen buffer validated solutions for peers
            for cell in peer_groups[value]:
                if len(values[cell]) == 1 and cell != value:
                    seen_buffer += values[cell]
            # add to targets value buffer potential solution that are not validated solutions for peers
            for i in board_cols:
                if i not in seen_buffer:
                    value_buffer += i
            #Assign value buffer box if the value buffer is not empty if it is empty there is no change
            assign_value(values, value, strIntersection(value_buffer, values[value]))

        # Removes single-valued box values from peers
        if len(values[value]) == 1:
            for peer in peer_groups[value]:
                if peer != value:
                    entry = values[peer].replace(values[value], '')
                    assign_value(values, peer, entry)
    return values

def only_choice(values):
    """
    Chooses values using the only choice strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the only choice chosen from among peers.
    """
    for value in values:
        seen_buffer = ''
        peer_grp = peer_groups[value]

        #Creates a set of seen values from target box peer group
        for i in peer_grp:
            if i != value:
                seen_buffer += values[i]
        seen_buffer = ''.join(list(set(list(seen_buffer))))

        #If there is a number not in seen buffer we make it the new value of the target box
        new_value = ''
        for i in values[value]:
            if i not in seen_buffer:
                new_value += i

        #Assign new value to  box if the value if there is new value is non-empty
        new_value = values[value] if new_value == '' else new_value
        if new_value != values[value]:
            values = assign_value(values, value, new_value)
    return values

def reduce_puzzle(values):
    """
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}
    Reduces puzzle and determine if puzzle is stalled.
    """
    solved_values = [box for box in values.keys() if len(values[box]) == 1]
    stalled = False
    while not stalled:
        solved_values_before = len([box for box in values.keys() if len(values[box]) == 1])
        values = eliminate(values)
        values = only_choice(values)
        values = naked_twins(values)
        solved_values_after = len([box for box in values.keys() if len(values[box]) == 1])
        stalled = solved_values_before == solved_values_after
        if len([box for box in values.keys() if len(values[box]) == 0]):
            return False
    return values

def search(values):
    """
    Use DFS to check different possibilities for the puzzles.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """
    values = reduce_puzzle(values)
    if values is False:
        return values ## Failed earlier
    if all(len(values[s]) == 1 for s in cross(board_cols, board_rows)):
        return values ## Solved!
    # Chose one of the unfilled square s with the fewest possibilities
    n,s = min((len(values[s]), s) for s in cross(board_cols, board_rows) if len(values[s]) > 1)
    # Now use recurrence to solve each one of the resulting sudokus, and
    for value in values[s]:
        new_sudoku = values.copy()
        new_sudoku[s] = value
        attempt = search(new_sudoku)
        if attempt:
            return attempt

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """
    sudoku_board = grid_values(grid)
    sudoku_board = search(sudoku_board)
    return sudoku_board

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))
    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
