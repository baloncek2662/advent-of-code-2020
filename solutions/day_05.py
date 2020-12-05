#!/usr/bin/env python
import time

def main():
    input_list = get_input_list()
    ids_list = solve_a(input_list)
    print()
    solve_b(ids_list)

def solve_a(boarding_passes):
    max_id = 0
    ids_list = []
    for boarding_pass in boarding_passes:
        row = int(boarding_pass[:7], 2)
        column = int(boarding_pass[7:], 2)
        id = row * 8 + column
        ids_list.append(id)
        if id > max_id:
            max_id = id
    print(f'Maximum boarding pass id: {max_id}')
    return ids_list

def solve_b(ids_list):
    for row in range(1, 126):
        for column in range(0, 7):
            id = row * 8 + column
            # the only missing id in rows [1,126], which has both neighbours
            if id not in ids_list and id + 1 in ids_list and id - 1 in ids_list:
                print(f'My boarding pass id: {id}')


def get_input_list():
    file = open("../inputs/day_05.txt", "r")
    input_list = []
    for val in file.read().split():
        bin_val = get_binary_representation(val)
        input_list.append(bin_val)
    file.close()
    return input_list

def get_binary_representation(val):
    result = ''
    for letter in val[:7]:
        if letter == 'F':
            result += '0'
        else:
            result += '1'

    
    for letter in val[7:]:
        if letter == 'L':
            result += '0'
        else:
            result += '1'

    return result

    
if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')