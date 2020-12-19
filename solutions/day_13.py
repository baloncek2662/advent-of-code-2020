#!/usr/bin/env python
import time
import copy
from math import gcd

def main():
    input_dict = get_input_dict()
    solve_a(input_dict)
    print()
    solve_b(input_dict)


def solve_a(input_dict):
    only_numbers = []
    for el in input_dict['bus_ids']:
        if el != 'x':
            only_numbers.append(el)
            
    numbers_time_diff = list(map(lambda x : (int(input_dict['time'] / x) + 1) * x - input_dict['time'], only_numbers))
    min_ix = numbers_time_diff.index(min(numbers_time_diff))
    print(f'Solution to A: {only_numbers[min_ix] * numbers_time_diff[min_ix]}')
        
        
def solve_b(input_dict):
    bus_ids = input_dict['bus_ids']
    first_bus_id = bus_ids[0]

    initial_timestamps = copy.deepcopy(bus_ids)
    intervals = copy.deepcopy(bus_ids)
    for i in range(1, len(bus_ids)):
        curr_bus_id = bus_ids[i]
        if curr_bus_id == 'x':
            continue
        j = 1
        second_run = False
        while True:
            first_bus_time = first_bus_id * j
            kolicnik = (first_bus_time / curr_bus_id) + 1
            if first_bus_time % curr_bus_id == 0:
                kolicnik -= 1
            closest_curr_bus_time = int(kolicnik) * curr_bus_id 
            if second_run and closest_curr_bus_time == first_bus_time + i:
                intervals[i] = closest_curr_bus_time - initial_timestamps[i]
                break
            if closest_curr_bus_time == first_bus_time + i:
                second_run = True
                initial_timestamps[i] = closest_curr_bus_time
            j += 1
            
    # only works if last list element is a number
    last_ix = len(initial_timestamps) - 1
    possible_solution = initial_timestamps[last_ix] 
    while True:
        all_good = True
        for i in range(1,len(intervals)-1):
            if intervals[i] == 'x':
                continue
                
            if (possible_solution - initial_timestamps[i] - last_ix + i) % intervals[i] != 0:
                all_good = False
                break
        if all_good:
            break
        possible_solution += intervals[last_ix]
    print(f'Solution to B.1: {possible_solution - last_ix}')



    # However, with so many bus IDs in your list, surely the actual earliest timestamp will be larger than 100000000000000!
    # i = int(100000000000000 / first_bus_id) 
    # default solution
    i = 1
    while True:
        first_bus_time = first_bus_id * i
        all_good = True
        for j in range(1, len(bus_ids)):
            curr_bus_id = bus_ids[j]
            if curr_bus_id == 'x':
                continue
            closest_curr_bus_time = int((first_bus_time / curr_bus_id) + 1) * curr_bus_id 
                        
            if closest_curr_bus_time != first_bus_time + j:
                all_good = False
                break
        if all_good:
            print(f'Solution to B.2: {first_bus_time}')
            break

        i += 1
    

def get_input_dict():
    file = open("../inputs/day_13.txt", "r")
    
    depart_time = int(file.readline())
    bus_ids = file.readline().split(',')
    for i in range(len(bus_ids)):
        if bus_ids[i] != 'x':
            bus_ids[i] = int(bus_ids[i])


    file.close()
    return {
        'time' : depart_time,
        'bus_ids' : bus_ids,
    }


if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')