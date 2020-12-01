#!/usr/bin/env python
import time

def main():
    input_list = get_input_list()
    solve_a(input_list)
    solve_b(input_list)

def solve_a(expense_report):
    solved = False
    for i in range(len(expense_report)):
        if solved:
            break
        for j in range(len(expense_report)):
            if (expense_report[i] + expense_report[j]) == 2020:
                print(f'Entries: {expense_report[i]}, {expense_report[j]}')
                print(f'Solution A: {expense_report[i] * expense_report[j]}')
                solved = True
                break

def solve_b(expense_report):
    solved = False
    for i in range(len(expense_report)):
        if solved:
            break
        for j in range(len(expense_report)):
            if solved:
                break
            if expense_report[i] + expense_report[j] > 2020:
                continue
            for k in range(len(expense_report)):
                if (expense_report[i] + expense_report[j] + expense_report[k]) == 2020:
                    print(f'Entries: {expense_report[i]}, {expense_report[j]}, {expense_report[k]}')
                    print(f'Solution B: {expense_report[i] * expense_report[j] * expense_report[k]}')
                    solved = True
                    break

def get_input_list():
    file = open("../inputs/day_01.txt", "r")
    input_list = []
    for val in file.read().split():
        input_list.append(int(val))
    file.close()
    return input_list

    

if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')