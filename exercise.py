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

# Q9
def fizzbizz(x):
    for i in range (1,x+1):
        if i % 15 == 0 :
            print("fizzbizz")
        elif i % 5 == 0:
            print("bizz")
        elif i % 3 == 0:
            print("fizz")
        else:
            print(i)

# Q10
def biggest_in_list(x):
    # x.sort(reverse=True)
    # print(x[0])
    temp = x[0]
    for i in x:
        if i > temp:
            temp = i 
    return temp

# Q11
# def biggest2_in_list(x):
#     l=[]
#     temp = x[0]
#     for i in x:
#         if i > temp:
#             temp = i
#             if temp not in l:
#                 l.append(temp)
#     print(l)
#     return l[-1],l[-2]

# exercise.biggest2_in_list([1,-1,45,-4,8,-2])---->not working for this{list index out of range}

def biggest2_in_list(x):
    for i in range(0,len(x)):
        temp = i
        for j in range(i+1,len(x)):
            if x[i] > x[j]:
                temp = j
        x[i],x[temp] = x[temp],x[j]
        return x[-1],x[-2]
        
                

def biggest_n(x,n):
    return 0
        

# Q12
def panagram(s):
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in s:
            return False
    return True

# Q13
def freq(s):
    d = {}
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i in s:
            if i not in d.keys():
                d[i] += 1
    return d

    
            
