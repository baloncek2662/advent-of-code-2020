#!/usr/bin/env python
import time

def main():
    solve_a(get_input_list())
    print()
    solve_b(get_input_list())


def solve_a(instruction_list):
    acc = run_program(instruction_list)
    print(f'Final value of accumulator: {acc}')

def solve_b(instruction_list):
    for changed_instr in instruction_list:
        if changed_instr['instr'] == 'acc':
            continue
        changed_instr = change_instr(changed_instr) # change
        
        run_program(instruction_list)

        changed_instr = change_instr(changed_instr) # change back
        reset_visited(instruction_list)

def change_instr(instr):
    if instr['instr'] == 'jmp':
        instr['instr'] = 'nop'    
    elif instr['instr'] == 'nop':
        instr['instr'] = 'jmp'
    return instr

def reset_visited(instruction_list):
    for i in instruction_list:
        i['visited'] = False

def run_program(instruction_list):
    acc = 0
    i = 0
    while True:
        if i >= len(instruction_list):
            print(f'Value of accumulator after finishing: {acc}')
            break
        if instruction_list[i]['visited']:
            break 
        instruction_list[i]['visited'] = True
        instr = instruction_list[i]['instr']
        val = instruction_list[i]['val']
        if instr == 'jmp':
            i += val
            continue
        elif instr == 'acc':
            acc += val    

        i += 1
    return acc

def get_input_list():
    file = open("../inputs/day_08.txt", "r")
    instruction_list = []
    for line in file.readlines():
        instr = line.split(' ')[0]
        val = int(line.split(' ')[1])

        instruction_full = {
            'instr' : instr,
            'val' : val,
            'visited' : False
        }

        instruction_list.append(instruction_full)
        
    file.close()
    return instruction_list


if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')