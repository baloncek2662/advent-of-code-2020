#!/usr/bin/env python
import time
import copy
from collections import Counter

def main():
    solve_a(get_input_list())
    print()
    solve_b(get_input_list())


def solve_a(grid):
    while True:
        new_grid = make_changes(grid)
        if grid == new_grid:
            filled_seats = get_filled_seats_count(new_grid)
            print(f'Final number of filled seats: {filled_seats}')
            break
        grid = new_grid

def make_changes(grid):
    new_grid = []
    for i in range(0, len(grid)):
        row_chars = ''
        for j in range(0, len(grid[i])):
            adj_occupied = get_adj_occupied(grid, i, j)
            if grid[i][j] == 'L' and adj_occupied == 0:
                new_char = '#'
            elif grid[i][j] == '#' and adj_occupied >= 4:
                new_char = 'L'
            else:
                new_char = grid[i][j]

            row_chars += new_char
        new_grid.append(row_chars)
            

    return new_grid

def get_adj_occupied(grid, i, j):
    result = 0
    if i > 0:
        if j > 0 and grid[i-1][j-1] == '#':
            result += 1
        if grid[i-1][j] == '#':
            result += 1
        if j < len(grid[i]) - 1 and grid[i-1][j+1] == '#':
            result += 1
        
    if j > 0 and  grid[i][j-1] == '#':
        result += 1
    if j < len(grid[i]) - 1 and grid[i][j+1] == '#':
        result += 1

    if i < len(grid) - 1:
        if j > 0 and grid[i+1][j-1] == '#':
            result += 1
        if grid[i+1][j] == '#':
            result += 1
        if j < len(grid[i]) - 1 and grid[i+1][j+1] == '#':
            result += 1

    return result


def get_filled_seats_count(grid):
    result = 0
    for line in grid:
        result += Counter(line)['#']
    return result


def solve_b(grid):
    while True:
        new_grid = make_changes_2(grid)
        if grid == new_grid:
            filled_seats = get_filled_seats_count(new_grid)
            print(f'Final number of filled seats 2: {filled_seats}')
            break
        grid = new_grid

def make_changes_2(grid):
    new_grid = []
    for i in range(0, len(grid)):
        row_chars = ''
        for j in range(0, len(grid[i])):
            adj_occupied = get_adj_occupied_2(grid, i, j)
            if grid[i][j] == 'L' and adj_occupied == 0:
                new_char = '#'
            elif grid[i][j] == '#' and adj_occupied >= 5:
                new_char = 'L'
            else:
                new_char = grid[i][j]

            row_chars += new_char
        new_grid.append(row_chars)
            
    return new_grid

def get_adj_occupied_2(grid, i, j):
    result = 0
    
    # left
    x = j - 1
    while x >= 0:
        if grid[i][x] == '#':
            result += 1
            break
        elif grid[i][x] == 'L':
            break
        x -= 1
    # right
    x = j + 1
    while x < len(grid[i]):
        if grid[i][x] == '#':
            result += 1
            break
        elif grid[i][x] == 'L':
            break
        x += 1
    # up 
    y = i - 1
    while y >= 0:
        if grid[y][j] == '#':
            result += 1
            break
        elif grid[y][j] == 'L':
            break
        y -= 1
    # down
    y = i + 1
    while y < len(grid):
        if grid[y][j] == '#':
            result += 1
            break
        elif grid[y][j] == 'L':
            break
        y += 1
    # left-up
    x = j-1
    y = i-1
    while x >= 0 and y >= 0:
        if grid[y][x] == '#':
            result += 1
            break
        elif grid[y][x] == 'L':
            break
        x -= 1
        y -= 1
    # left-down
    x = j-1
    y = i+1
    while x >= 0 and y < len(grid):
        if grid[y][x] == '#':
            result += 1
            break
        elif grid[y][x] == 'L':
            break
        x -= 1
        y += 1
    # right-up
    x = j+1
    y = i-1
    while x < len(grid[i]) and y >= 0:
        if grid[y][x] == '#':
            result += 1
            break
        elif grid[y][x] == 'L':
            break
        x += 1
        y -= 1
    # right-down
    x = j+1
    y = i+1
    while x < len(grid[i]) and y < len(grid):
        if grid[y][x] == '#':
            result += 1
            break
        elif grid[y][x] == 'L':
            break
        x += 1
        y += 1

    return result

# NOTE: make sure the input txt file ends with new line, else program crashes
def get_input_list():
    file = open("../inputs/day_11.txt", "r")
    grid = []
    for line in file.readlines():
        line = line.split('\n')[0] # get rid of \n
        grid.append(line)
        
    file.close()
    return grid


if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')