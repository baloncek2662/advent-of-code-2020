#!/usr/bin/env python
import time

PREAMBLE = 25

def main():
    input_list = get_input_list()
    first_invalid = solve_a(input_list)
    print()
    solve_b(input_list, first_invalid)


def solve_a(number_list):
    for i in range(PREAMBLE, len(number_list)):
        if not is_sum_of_preamble(number_list, i):
            print(f'First invalid number is: {number_list[i]}')
            return number_list[i]

def solve_b(number_list, expected_sum):
    contiguous_range = []
    for i in range(0, len(number_list)):
        j = i + 1
        range_sum = number_list[i]
        while j < len(number_list) and range_sum < expected_sum: 
            range_sum += number_list[j]
            if range_sum == expected_sum:
                contiguous_range = number_list[i:j+1] # we need to INCLUDE j
                break
            j += 1
            
    print(f'Sum of min and max value in contigous range: {min(contiguous_range) + max(contiguous_range)}')

def is_sum_of_preamble(list, i):
    expected_sum = list[i]
    sublist = list[i - PREAMBLE:i]

    for a in sublist:
        b = expected_sum - a
        if b in sublist:
            return True
            
    return False

def get_input_list():
    file = open("../inputs/day_09.txt", "r")
    numbers = []
    for line in file.readlines():
        numbers.append(int(line))
        
    file.close()
    return numbers


if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')