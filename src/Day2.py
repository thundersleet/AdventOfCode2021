from helpers import *

if __name__ == '__main__':
    horizontal_position = 0
    depth = 0
    aim = 0
    line_object = read_lines('input/Day2.txt')
    for line in line_object:
        command = line.split()
        if command[0] == 'forward':
            horizontal_position += int(command[1])
            depth += (int(command[1]) * aim)
        elif command[0] == 'up':
            aim -= int(command[1])
        elif command[0] == 'down':
            aim += int(command[1])
    print(f'The course is {horizontal_position * depth}')
