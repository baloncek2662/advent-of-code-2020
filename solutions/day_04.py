#!/usr/bin/env python
import time
import string
from collections import Counter


def main():
    input_list = get_input_list()
    valid_passports = solve_a(input_list)
    print()
    solve_b(valid_passports)

def solve_a(passport_list):
    valid_passports = []
    for passport in passport_list:
        # if all fields are present || all fields except for north pole credentials are present
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
            valid_passports.append(passport)
            
    print(f'Valid passports A: {len(valid_passports)}')
    return valid_passports

def solve_b(valid_passports):
    valid_passport_fields = []
    for passport in valid_passports:
        all_valid = True
        for field in passport:
            if not field_is_valid(field, passport[field]):
               all_valid = False
               break 

        if all_valid:
            valid_passport_fields.append(passport)
            
    
    print(f'Valid passports B: {len(valid_passport_fields)}')

def field_is_valid(field, value):
    if field == 'byr':
        if int(value) >= 1920 and int(value) <= 2002:
            return True
    elif field == 'iyr':
        if int(value) >= 2010 and int(value) <= 2020:
            return True
    elif field == 'eyr':
        if int(value) >= 2020 and int(value) <= 2030:
            return True        
    elif field == 'hgt':
        if is_hgt_correct(value):
            return True
    elif field == 'hcl':
        if is_hcl_correct(value):
            return True
    elif field == 'ecl':
        if value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
            return True
    elif field == 'pid':
        if len(value) == 9:
            return True
    elif field == 'cid':
        return True
        
    return False
'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
    If cm, the number must be at least 150 and at most 193.
    If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not.
'''

def is_hcl_correct(value):
    if value[0] != '#' or len(value) != 7:
        return False
    for letter in value[1:]:
        if not (letter in string.ascii_lowercase[:6] or letter in '0123456789'):
            return False
    return True
    


def is_hgt_correct(value):
    if len(value.split('c')) == 2:
        number = int(value.split('cm')[0])
        return number >= 150 and number <= 193
    if len(value.split('i')) == 2:
        number = int(value.split('in')[0])
        return number >= 59 and number <= 76        

    return False


def get_input_list():
    file = open("../inputs/day_04.txt", "r")
    list = []
    passport = {}
    for line in file.readlines():
        if line == '\n':
            list.append(passport)
            passport = {}
            continue

        fields = line.split(' ')
        for field in fields:
            [key, value] = field.split(':')
            passport[key] = value.split('\n')[0] # to remove the EOL char where needed
            
    list.append(passport) # to add the last passport
    file.close()
    return list

    

if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')