#!/usr/bin/env python
import time

SHINY_GOLD = 'shiny gold'
def main():
    input_list = get_input_list()
    solve_a(input_list)
    print()
    solve_b(input_list)


def solve_a(bag_list):
    result = 0
    for b in bag_list:
        if contains_gold_bag(bag_list, b) and b.color != SHINY_GOLD:
            result += 1

    print(f'Number of bags which can contain a shiny gold bag: {result}')
    
def contains_gold_bag(bag_list, master_bag):
    if master_bag.color == SHINY_GOLD:
        return True

    for contained_bag in master_bag.contained_bags:
        if contains_gold_bag(bag_list, get_bag(bag_list, contained_bag.color)):
            return True
    return False

def solve_b(bag_list):
    shiny_gold_bag = get_bag(bag_list, SHINY_GOLD)
    result = contained_count(bag_list, shiny_gold_bag) - 1 # minus 1 because the bag does not contain itself
    print(f'Number of bags a shiny gold bag can hold: {result}')

def contained_count(bag_list, master_bag):
    if len(master_bag.contained_bags) == 0:
        return 1
    
    contained_bag_sum = 0
    for i in range(0, len(master_bag.contained_bags)):
        contained_bag = master_bag.contained_bags[i]
        contained_bag_count = master_bag.contained_bag_count[i]
        temp = contained_bag_count * contained_count(bag_list, contained_bag)
        
        contained_bag_sum += temp 

    return contained_bag_sum + 1
    

def get_input_list():
    file = open("../inputs/day_07.txt", "r")
    bag_list = []
    for line in file.readlines():
        master_bag_color = line.split(' bags contain ')[0]

        master_bag = get_bag(bag_list, master_bag_color)
        if master_bag is None:
            master_bag = Bag(master_bag_color)
            bag_list.append(master_bag)

        contained_bags = line.split(' bags contain ')[1].split('.')[0].split(', ')
        if 'no other bags' in contained_bags:
            continue

        for b in contained_bags:
            b = b.split(' bag')[0] # get rid of singular/plural
            count = int(b[0]) # first char is number of bags
            color = b[2:]

            contained_bag = get_bag(bag_list, color)
            if contained_bag is None:
                contained_bag = Bag(color)
                bag_list.append(contained_bag)
            
            master_bag.add_contained(contained_bag, count)

        
    file.close()
    return bag_list

def get_bag(bag_list, bag_color):
    for b in bag_list:
        if b.color == bag_color:
            return b
    return None

def print_bag(bag_list):
    for b in bag_list:
        print(b.color)
        for cb in b.contained_bags:
            print(cb['count'])
        print('==============')



class Bag():
    def __init__(self, color):
        self.color = color
        self.contained_bags = []
        self.contained_bag_count = []

    def add_contained(self, contained_bag, count):
        self.contained_bags.append(contained_bag)
        self.contained_bag_count.append(count)

if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')