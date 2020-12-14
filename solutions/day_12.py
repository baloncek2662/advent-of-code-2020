#!/usr/bin/env python
import time

NORTH,EAST,SOUTH,WEST,LEFT,RIGHT,FORWARD = range(7)

def main():
    input_list = get_input_list()
    solve_a(input_list)
    print()
    solve_b(input_list)


def solve_a(instruction_list):
    ship = Ship()
    for instruction in instruction_list:
        ship.execute_instruction(instruction)
        
    print(f'Manhattan distance of ship coordinates: {ship.x+ship.y}')
        
def solve_b(instruction_list):
    ship2 = Ship2()
    for instruction in instruction_list:
        ship2.execute_instruction(instruction)
        print(f'x: {ship2.x}, y: {ship2.y}\nwx: {ship2.wx}, wy: {ship2.wy}\n=========================')
        
    print(f'Manhattan distance of ship2 coordinates: {ship2.x+ship2.y}')

def get_input_list():
    file = open("../inputs/day_12.txt", "r")
    instructions = []
    for line in file.readlines():
        order = line[0]
        value = int(line[1:])
        instructions.append(Instruction(order, value))
        
    file.close()
    return instructions

class Instruction:
    def __init__(self, order, value):
        self.order = self.get_order_enum(order)
        self.value = value

    def get_order_enum(self, order):
        if order == 'N':
            return NORTH
        elif order == 'E':
            return EAST
        elif order == 'S':
            return SOUTH
        elif order == 'W':
            return WEST
        elif order == 'L':
            return LEFT
        elif order == 'R':
            return RIGHT
        elif order == 'F':
            return FORWARD
    
    def __repr__(self):
        return f"order: {self.order}, value: {self.value}\n"

class Ship:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.direction = EAST
    
    def execute_instruction(self, instruction):
        if instruction.order == LEFT or instruction.order == RIGHT:
            self.handle_direction_change(instruction)
        else:
            self.handle_position_change(instruction)
    
    def handle_position_change(self, instruction):
        direction = instruction.order
        if instruction.order == FORWARD:
            direction = self.direction
        if direction == EAST:
            self.x += instruction.value
        elif direction == WEST:
            self.x -= instruction.value
        elif direction == NORTH:
            self.y -= instruction.value
        elif direction == SOUTH:
            self.y += instruction.value

    def handle_direction_change(self, instruction):
        normalized_value = (instruction.value % 360) / 90
        if instruction.order == LEFT:
            self.direction = (self.direction + 4 - normalized_value) % 4 # +4 so we never get negative value
        else:
            self.direction = (self.direction + normalized_value) % 4

class Ship2:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.wx = 10
        self.wy = -1
        self.direction = EAST
    
    def execute_instruction(self, instruction):
        if instruction.order == LEFT or instruction.order == RIGHT:
            self.handle_waypoint_rotation(instruction)
        elif instruction.order == FORWARD:
            self.handle_ship_move(instruction)
        else:
            self.handle_waypoint_change(instruction)
    
    def handle_waypoint_change(self, instruction):
        direction = instruction.order
        if direction == EAST:
            self.wx += instruction.value
        elif direction == WEST:
            self.wx -= instruction.value
        elif direction == NORTH:
            self.wy -= instruction.value
        elif direction == SOUTH:
            self.wy += instruction.value

    def handle_waypoint_rotation(self, instruction):
        dist_x = self.wx
        dist_y = self.wy
        quadrant_shifts_clockwise = (instruction.value % 360) / 90
        if instruction.order == LEFT:
            quadrant_shifts_clockwise = 4 - quadrant_shifts_clockwise 

        # if quadrant_shifts_clockwise == 1:
        #     if dist_x > 0 and dist_y > 0 or dist_x < 0 and dist_y < 0:
        #         self.wy = -self.wy
        #     else:
        #         self.wx = -self.wx
        # elif quadrant_shifts_clockwise == 2:
        #     self.wx = -self.wx
        #     self.wy = -self.wy

        # elif quadrant_shifts_clockwise == 3:
        #     if dist_x > 0 and dist_y > 0 or dist_x < 0 and dist_y < 0:
        #         self.wx = -self.wx
        #     else:
        #         self.wy = -self.wy
        if quadrant_shifts_clockwise == 1:
            if dist_x > 0 and dist_y > 0 or dist_x < 0 and dist_y < 0:
                self.wx = dist_y
                self.wy = - dist_x
            else:
                self.wx = - dist_y
                self.wy = dist_x
        elif quadrant_shifts_clockwise == 2:
            self.wx = - dist_y
            self.wy = - dist_x

        elif quadrant_shifts_clockwise == 3:
            if dist_x > 0 and dist_y > 0 or dist_x < 0 and dist_y < 0:
                self.wx = - dist_y
                self.wy = dist_x
            else:
                self.wx = dist_y
                self.wy = - dist_x


    def handle_ship_move(self, instruction):
        self.x += self.wx * instruction.value
        self.y += self.wy * instruction.value
        # if self.x > self.wx:
        #     self.x -= self.wx * instruction.value
        # else:
        #     self.x += self.wx * instruction.value
        
        # if self.y > self.wy:
        #     self.y -= self.wy * instruction.value
        # else:
        #     self.y += self.wy * instruction.value




if __name__ == "__main__":
    start_time = time.time()

    main()

    end_time = time.time()
    print(f'\nExecution time: {end_time - start_time} s')