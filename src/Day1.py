from helpers import *

if __name__ == '__main__':
    increase_count = 0
    line_object = read_lines_as_ints('input/Day1.txt')
    for i in range(len(line_object)-3):
        if line_object[i + 3] > line_object[i]:
            increase_count += 1
    print(increase_count)
