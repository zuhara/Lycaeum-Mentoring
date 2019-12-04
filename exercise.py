# Example warm up programs
 
# Q1
def digits(n):
    "Returns number of digits in number n"
    return len(str(n))

# The len() function can be used to get the length of any iterable


# Q2
def words(s):
    "Returns number of words in sentence s"
    return len(s.split(" "))

# Q3
def bigger(a,b):
    if (a > b):
        return a
    else:
        return b

def biggest(a,b,c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c
            

