#!/usr/bin/env python
import time

def main():
    input_list = get_input_list()
    solve_a(input_list)
    print()
    solve_b(input_list)


def solve_a(number_list):
    prev_joltage = 0
    one_jolt_diff = 0
    three_jolt_diff = 1 # to account for the final diff between device and adapter
    for num in number_list:
        diff = num - prev_joltage
        if diff == 1:
            one_jolt_diff += 1
        elif diff == 3:
            three_jolt_diff += 1
        elif diff > 3:
            print('Whoops, can\'t adapt')
            break
        prev_joltage = num
        
    print(f'One jolt diffs multiplied by three jolt diffs: {one_jolt_diff * three_jolt_diff}')
        
        
cache = [] # memoisation ftw!!
def solve_b(number_list):
    number_list.insert(0, 0) # start with 0
    number_list.append(number_list[len(number_list)-1] + 3) # end with our device joltage

    for _ in range(0, len(number_list)):
        cache.append(0)
    result = get_arrangements(number_list, 0, len(number_list))
    
    print(f'All arrangements: {result}')


def get_arrangements(number_list, index, list_length):
    if index == list_length - 1:
        return 1
    if cache[index] != 0:
        return cache[index]

    current_number = number_list[index]
    sum = 0
    # look one ahead
    if index < list_length - 1 and number_list[index+1] - current_number <= 3:
        sum += sum + get_arrangements(number_list, index+1, list_length)
    # look two ahead
    if index < list_length - 2 and number_list[index+2] - current_number <= 3:
        sum += get_arrangements(number_list, index+2, list_length)
    # look three ahead
    if index < list_length - 3 and number_list[index+3] - current_number <= 3:
        sum += get_arrangements(number_list, index+3, list_length)

    if cache[index] == 0:
        cache[index] = sum
        
    return sum

def get_input_list():
    file = open("../inputs/day_10.txt", "r")
    numbers = []
    for line in file.readlines():
        numbers.append(int(line))
        
    file.close()
    return sorted(numbers)


if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')