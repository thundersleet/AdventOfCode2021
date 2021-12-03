from helpers import *


def part_one(filename):
    answer = 0
    lines = read_lines(filename)
    ones = [0] * len(lines[0])
    zeros = [0] * len(lines[0])
    for line in lines:
        for i in range(len(line)):
            if line[i] == '0':
                zeros[i] += 1
            elif line[i] == '1':
                ones[i] += 1

    gamma = ''
    epsilon = ''
    for i in range(len(zeros)):
        if zeros[i] > ones[i]:
            gamma += '0'
            epsilon += '1'
        elif zeros[i] < ones[i]:
            gamma += '1'
            epsilon += '0'

    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    answer = gamma_int * epsilon_int

    print(f'Power Consumption: {answer}')


def part_two(filename):
    answer = 0
    lines = read_lines(filename)
    ones = [0] * len(lines[0])
    zeros = [0] * len(lines[0])
    for line in lines:
        for i in range(len(line)):
            if line[i] == '0':
                zeros[i] += 1
            elif line[i] == '1':
                ones[i] += 1

    gamma = ''
    epsilon = ''
    for i in range(len(zeros)):
        if zeros[i] > ones[i]:
            gamma += '0'
            epsilon += '1'
        elif zeros[i] < ones[i]:
            gamma += '1'
            epsilon += '0'

    gamma_int = int(gamma, 2)
    epsilon_int = int(epsilon, 2)
    answer = gamma_int * epsilon_int

    print(f'Power Consumption: {answer}')


if __name__ == '__main__':
    file = 'input/Day3.txt'
    part_one(file)
