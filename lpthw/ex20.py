from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())


def rewind(f):
    print(f.seek(0))
    print()


def print_a_line(line_count, f):
    print(line_count, f.readline())
    


# Calling the Functions

current_file = open(input_file)


print("First let's print the whole file:\n")
print_all(current_file) # First Function


print("Now let's rewind, kind of like a tape.")
rewind(current_file) # Second


print("Next, Let's print three lines:")
current_line = 1
print_a_line(current_line, current_file) # Third

current_line = current_line + 1
print_a_line(current_line, current_file) # Third

current_line = current_line + 1
print_a_line(2, current_file) # Third

print_a_line(2, current_file)
