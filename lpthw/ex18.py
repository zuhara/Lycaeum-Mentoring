def print_two(*args):
    arg1, arg2 = args
    print(f"arg1 is {arg1} and arg2 is {arg2}")

def print_two_again(arg1, arg2):
    print(f"arg1: {arg1},\narg2: {arg2}")

def print_one(arg1):
    print(f"arg1: {arg1}")


def print_none():
    print("I got nothing")

# Calling the functions........

print_two("Zuhara","Sharin")
print_two_again("Zuhara","Sharin")
print_one("First!")
print_none()
