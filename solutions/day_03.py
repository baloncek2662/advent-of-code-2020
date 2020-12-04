#!/usr/bin/env python
import time
from collections import Counter


def main():
    input_table = get_input_table()
    solve_a(input_table)
    print()
    solve_b(input_table)

def solve_a(input_table):
    trees_hit = get_trees_hit_count(input_table, 3, 1)
    print (f'Number of trees hit: {trees_hit}')

def solve_b(input_table):
    move_params = [
        {'right' : 1, 'down' : 1},
        {'right' : 3, 'down' : 1},
        {'right' : 5, 'down' : 1},
        {'right' : 7, 'down' : 1},
        {'right' : 1, 'down' : 2},
    ]
    result = 1
    for move in move_params:
        result *= get_trees_hit_count(input_table, move['right'], move['down'])
    
    print (f'Number of trees hit multiplied: {result}')



def get_trees_hit_count(input_table, RIGHT, DOWN):
    trees_hit = 0
    step = 0
    for i in range(0, len(input_table), DOWN):
        x = step * RIGHT
        x %= len(input_table[i]) 
        y = i

        if input_table[y][x] == '#':
            trees_hit += 1
        
        step += 1

    return trees_hit

def get_input_table():
    file = open("../inputs/day_03.txt", "r")
    table = []
    for line in file.readlines():
        row = []
        for symbol in line:
            if symbol == '\n':
                continue
            row.append(symbol)
        table.append(row)
            
    file.close()
    return table

    

if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')