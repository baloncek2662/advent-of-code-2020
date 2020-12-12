#!/usr/bin/env python
import time
import string

def main():
    solve_a(get_input_list_a())
    print()
    solve_b(get_input_list_b())


def solve_a(answers_list):
    result = 0
    for el in answers_list:
        result += len(el)
    print(f'Answers count A: {result}')
    return answers_list

def solve_b(answers_list):
    result = 0
    for el in answers_list:
        result += len(el)
    print(f'Answers count B: {result}')    

def get_input_list_a():
    file = open("../inputs/day_06.txt", "r")
    all_group_answers = []
    group_answers = set()
    for line in file.readlines():
        if line == '\n':
            group_answers.remove('\n')
            all_group_answers.append(group_answers)
            group_answers = set()
            continue
        
        group_answers = group_answers.union(set(line))
        
    if '\n' in group_answers:
        group_answers.remove('\n')
    all_group_answers.append(group_answers) # to add the last group answers
    file.close()
    return all_group_answers

def get_input_list_b():
    file = open("../inputs/day_06.txt", "r")
    all_group_answers = []
    group_answers = set(string.ascii_letters)
    for line in file.readlines():
        if line == '\n':
            all_group_answers.append(group_answers)
            group_answers = set(string.ascii_letters)
            continue
        
        group_answers = group_answers.intersection(set(line))
        
    all_group_answers.append(group_answers) # to add the last group answers
    file.close()
    return all_group_answers

    
if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')