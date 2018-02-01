import random
import time


def make_grid(rows, cols, pempty=0.9):
    """ Make a grid which represents the paths and the blocked cells"""
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            random_val = random.random()
            if random_val < pempty:
                grid[i].append(0)
            else:
                grid[i].append(blocked_cell)
    grid[0][0] = 0
    grid[rows-1][cols-1] = 0
    return grid


def print_grid(grid):
    """ Prints the grid which is easily readable by humans """
    print
    for i in grid:
        print i


def get_mem_grid(value):
    """ Make a memory grid which helps us in memoization """
    grid = []
    for i in range(rows):
        grid.append([])
        for j in range(cols):
            grid[i].append(value)
    return grid
    

def get_num_paths(grid, row, col):
    """ Get the number of paths with pure recursion """
    if row == (rows - 1) and col == (cols - 1):
        return 1
    elif grid[row][col] == blocked_cell:
        return 0
    else:
        r = c = 0
        if row < (rows - 1):
            r = get_num_paths(grid, row + 1, col)
        if col < (cols - 1):
            c = get_num_paths(grid, row, col + 1)
        return r + c


def get_num_paths_dp_memoize(grid, row, col):
    """ Get the num paths using recursion and memoization """
    mem_grid = get_mem_grid(-1)
    def get_num_paths_dp_helper(grid, row, col, mem_grid):
        if mem_grid[row][col] > -1:
            return mem_grid[row][col]
        if row == (rows - 1) and col == (cols - 1):
            mem_grid[row][col] = 1
            return mem_grid[row][col]
        elif grid[row][col] == blocked_cell:
            mem_grid[row][col] = 0
            return mem_grid[row][col]
        else:
            r = c = 0
            if row < (rows - 1):
                r = get_num_paths_dp_helper(grid, row + 1, col, mem_grid)
            if col < (cols - 1):
                c = get_num_paths_dp_helper(grid, row, col + 1, mem_grid)
            mem_grid[row][col] = r + c
            return mem_grid[row][col]
    return get_num_paths_dp_helper(grid, row, col, mem_grid)


def get_num_paths_dp_tabulation(grid, rows, cols):
    """ Get the num paths by using tabulation method """
    mem_grid = get_mem_grid(0)
    def set_cell_value(row, col, mem_grid):
        if row == rows - 1:
            row_value = 0
        else:
            row_value = mem_grid[row+1][col]
        if col == cols - 1:
            col_value = 0
        else:
            col_value = mem_grid[row][col+1]
            
        if grid[row][col] != -2:
            value = row_value + col_value
        else:
            value = 0
        mem_grid[row][col] = value
        # print row, col, value
        return value

    mem_grid[rows-1][cols-1] = 1
    # print_grid(mem_grid)
    num_row = rows - 1
    num_col = cols - 1

    while num_row >= 0 and num_col >= 0:
        for row in range(num_row, -1, -1):
            if not mem_grid[row][num_col]:
                set_cell_value(row, num_col, mem_grid)

        for col in range(num_col, -1, -1):
            if not mem_grid[num_row][col]:
                set_cell_value(num_row, col, mem_grid)
        num_row -= 1
        num_col -= 1
    # cprint_grid( mem_grid)
    return mem_grid[0][0]


def time_it(func, *args):
    """ Time each functions which computes the same output but in different methods """
    begin = time.time()
    ret = func(*args)
    end = time.time()
    print ret, end - begin

for i in range(2, 100):
    rows = i
    cols = i
    print rows, cols
    blocked_cell = -2


    grid = make_grid(rows, cols, 0.9)
    print_grid(grid)
    # time_it(get_num_paths, grid, 0, 0)
    time_it(get_num_paths_dp_memoize, grid, 0, 0)
    time_it(get_num_paths_dp_tabulation, grid, rows, cols)
