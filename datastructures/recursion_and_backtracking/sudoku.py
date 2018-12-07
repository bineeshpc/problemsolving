filename = 'sudoku.txt'

def read_input(filename):
    lines = [line.strip() for line in open(filename)]
    length = len(lines)
    n = length // 10
    i = 0
    problems = []
    for _ in range(n):
        i += 1 # pass the game number
        problem = []
        for k in range(9):
            one_row = [int(j) for j in lines[i]]
            problem.append(one_row)
            i += 1
        problems.append(problem)
    return problems

        
def get_problems():
    problems = read_input(filename)
    return problems

def get_problem():
    return get_problems()[0]

def get_row_map(problem):
    row_maps = []
    for i in range(9):
        row_map = [0 for _ in range(9)]
        for j in range(9):
            if problem[i][j] != 0:
                row_map[problem[i][j] - 1] += 1
        row_maps.append(row_map)
    return row_maps



def get_column_map(problem):
    column_maps = []
    for i in range(9):
        column_map = [0 for _ in range(9)]
        for j in range(9):
            if problem[j][i] != 0:
                column_map[problem[j][i] - 1] += 1
        column_maps.append(column_map)
    return column_maps

def get_sector_map(problem):
    sector_maps = []
    for i in range(9):
        sector_map = [0 for _ in range(9)]
        x, y = i // 3, i % 3
        for j in range(3):
            for k in range(3):
                p = x*3+j
                q = y*3+k
                if problem[p][q] != 0:
                    sector_map[problem[p][q]-1] += 1
        sector_maps.append(sector_map)
    return sector_maps
                
        

def get_next_tofill(problem, x, y):
    for i in range(0, 9):
        for j in range(0, 9):
            if problem[i][j] == 0:
                return i, j
    return -1, -1




def get_sector_number(i, j):
    x = i // 3
    y = j // 3
    return x * 3 + y


def is_valid(problem, i, j, e):
    """
    If I place e at position[i][j] is it still a valid position
    Returns true if valid
    Returns false if not valid
    """
    row_map = row_maps[i]
    column_map = column_maps[j]
    sector_map = sector_maps[get_sector_number(i, j)]
    not_in_row = row_map[e-1] == 0
    not_in_column = column_map[e-1] == 0
    not_in_sector = sector_map[e-1] == 0

    return not_in_row and not_in_column and not_in_sector


def print_problem(problem):
    print()
    for row in problem:
        print(row)

def sudoku_helper(problem, i, j):
    #print(problem)
    #print(i, j)
    i, j = get_next_tofill(problem, i, j)
    
    if i == -1:
        print_problem(problem)
        return True
            
    else:
        for e in range(1, 10):
            if problem[i][j] == 0 and is_valid(problem, i, j, e):
                # do
                problem[i][j] = e
                row_maps[i][e-1] += 1
                column_maps[j][e-1] += 1
                sector_maps[get_sector_number(i, j)][e-1] += 1

                # this would have worked even without the return true option
                # but this makes the function return earlier
                # so that we can count the backtracks if required
                if sudoku_helper(problem, i, j):
                    return True

                # if we reach here that means that we are backtracking because of the return statement
                # undo
                problem[i][j] = 0
                row_maps[i][e-1] -= 1
                column_maps[j][e-1] -= 1
                sector_maps[get_sector_number(i, j)][e-1] -= 1
                


def sudoku_helper1(problem, i, j):
    #print(problem)
    #print(i, j)
    i, j = get_next_tofill(problem, i, j)
    
    if i == -1:
        print_problem(problem)
            
    else:
        for e in range(1, 10):
            if problem[i][j] == 0 and is_valid(problem, i, j, e):
                # do
                problem[i][j] = e
                row_maps[i][e-1] += 1
                column_maps[j][e-1] += 1
                sector_maps[get_sector_number(i, j)][e-1] += 1

                sudoku_helper(problem, i, j)

                # undo
                problem[i][j] = 0
                row_maps[i][e-1] -= 1
                column_maps[j][e-1] -= 1
                sector_maps[get_sector_number(i, j)][e-1] -= 1
                

def sudoku(problem):
    return sudoku_helper1(problem, 0, 0)


for i, problem in enumerate(get_problems()):
    #problem = get_problem()
    row_maps = get_row_map(problem)
    column_maps = get_column_map(problem)
    sector_maps = get_sector_map(problem)
    print(i)
    print_problem(problem)
    sudoku(problem)
    
