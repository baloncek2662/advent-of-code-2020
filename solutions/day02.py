#!/usr/bin/env python
import time
from collections import Counter

def main():
    input_list = get_input_list()
    solve_a(input_list)
    print()
    solve_b(input_list)

def solve_a(input_list):
    valid_password_count = 0
    for input in input_list:
        letter_count = Counter(input['password'])
        key_letter_count = letter_count[input['letter']]
        if key_letter_count >= input['min'] and key_letter_count <= input['max']:
            valid_password_count += 1

    print (f'Number of valid passwords A: {valid_password_count}')

def solve_b(input_list):
    valid_password_count = 0
    for input in input_list:
        valid_positions = 0
        if input['password'][input['min']-1] == input['letter']:
            valid_positions += 1
        if input['password'][input['max'] - 1] == input['letter']:
            valid_positions += 1

        if valid_positions == 1:
            valid_password_count += 1

    print (f'Number of valid passwords B: {valid_password_count}')

def get_input_list():
    file = open("../inputs/day_02.txt", "r")
    input_list = []
    for line in file.readlines():
        # line example:
        # 11-13 c: cfcfccbcctgnccccvcc
        elements = line.split(' ')
        [min, max] = elements[0].split('-')
        letter = elements[1][0]
        password = elements[2][:len(elements[2])-1]
        input_list.append({
            'min' : int(min),
            'max': int(max),
            'letter' : letter,
            'password' : password,
        })

    file.close()
    return input_list

    

if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')