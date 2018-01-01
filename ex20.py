from sys import argv

script, input_file = argv

def print_all(f):
    #print(">>> print_all: f=", f)
    print(f.read())
    #print("<<< print_all: f=", f)

def rewind(f):
    #print(">>> rewind: f=", f)
    f.seek(0)
    #print("<<< rewind: f=", f)

def print_a_line(line_count, f):
    #print(">>> print_a_line: f=", f, line_count)
    print(line_count, f.readline())
    #print("<<< print_a_line: f=", f, line_count)

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)
