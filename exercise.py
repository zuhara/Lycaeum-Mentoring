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
# Q4
def biggest(a,b,c):
    if (a > b) and (a > c):
        return a
    elif (b > a) and (b > c):
        return b
    else:
        return c
            

# def biggest1(a,b,c):
#     if a > b:
#         temp = a
#     if temp > c:
#         temp = c


# Q5
def tables2(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            print("{:3}".format(i*j),end=' ')
        print("\n")
        
# Q6
def tables3(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(j,end=' ')
        print("\n")

# Q7
def tables4(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
           # print("____",end=' ')
            print("{:3}".format(i*j),end=' ')
           # print("____",end=' ')
        print("\n")
        print("__________")

# Q8
def tables5(x):
    for i in  range(1,x+1):
        for j in range(1,x+1):
            print("{:3}".format(1),end=' ')
        print("\n")

