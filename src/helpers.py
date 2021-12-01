def read_lines_as_ints(filename):
    file = open(filename, 'r')
    lines = file.readlines()
    int_lines = [int(line) for line in lines]
    return int_lines
