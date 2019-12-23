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

#Q3
def Mtable(n):
    l = []
    for i in range(1,11):
        #print("{} * {} = {}".format(i,n,i*n))
        l.append(i*n)
    return l
    
def Mtable2(n,a):
    l = []
    for i in range(1,a+1):
        l.append(i*n)
        #print("{} * {} = {}".format(i,n,i*n))
    return l

# Q4
def bigger(a,b):
    if (a > b):
        return a
    else:
        return b
    
# Q5
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


# Q6
def tables2(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            print("{:3}".format(i*j),end=' ')
            retur
        print("\n")
        
# Q7
def tables3(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
            print(j,end=' ')
        print("\n")

# Q8
def tables4(x):
    for i in range(1,x+1):
        for j in range(1,x+1):
           # print("____",end=' ')
            print("{:3}".format(i*j),end=' ')
           # print("____",end=' ')
        print("\n")
        print("__________")

# Q9
def tables5(x):
    for i in  range(1,x+1):
        for j in range(1,x+1):
            print("{:3}".format(1),end=' ')
        print("\n")

# Q10
def fizzbizz(x):
    if x > 0:
        l=[]
        for i in range (1,x+1):
            if i % 15 == 0 :
                print("fizzbizz")
                l.append("fizzbizz")
            elif i % 5 == 0:
                print("bizz")
                l.append("bizz")
            elif i % 3 == 0:
                print("fizz")
                l.append("fizz")
            else:
                print(i)
                l.append(i)
        return l
    else:
        return 0

# Q11
def biggest_in_list(x):
    # x.sort(reverse=True)
    # print(x[0])
    temp = x[0]
    for i in x:
        if i > temp:
            temp = i 
    return temp

# Q12
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
        

# Q13
def panagram(s):
    sen = s.lower()
    for i in "abcdefghijklmnopqrstuvwxyz":
        if i not in sen:
            return False
    return True

# Q14
def freq(s):
    d = {}
    for i in s:
        if i in d:
            d[i] = d[i] + 1
        else:
            d[i] = 1
    return d

    
# Q15
import math
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def dist_to_origin(self):
        return math.sqrt(self.x**2 + self.y**2)
    def quadrant(self):
        if self.x > 0 and self.y > 0:
            return (1)
        elif self.x < 0 and self.y > 0:
            return (2)
        elif self.x < 0 and self.y < 0:
            return(3)
        elif self.x > 0 and self.y < 0:
            return(4)


# Q16
def breakdown(p):
    q = p
    l=[2000,500,200,100,50,20,10,5,2,1]
    for i in l:
        f = p // i
        rem = p % i
        p = rem
        if f == 0:
            continue
        print("{} * {} = {}".format(i,f,i*f))
    print("------------------------")
    print(q)

#import collections
def breakdown2(p,d):
    #d = collections.OrderedDict(d) This is not working
    q = p
    l = sorted(d.keys(),reverse=True)
    for i in l:
        f = p // i
        rem = p % i
        if f > d[i]:
            f = d[i]
            rem = p - (i * d[i])
        p = rem
        print("p",p)
        print("f",f)
        if p < l[-1]:
            print("Not Possible")
            break
        print("{} * {} = {}".format(i,f,i*f))
       
    print("------------------------")
    print(q)


def evaluate(s):
    stack = []
    o = ["+","-","*","/"]
    for i in s:
        if i.isnumeric():
            stack.append(i)
        else:
            a = int(stack.pop())
            b = int(stack.pop())
            if i == "+":
                c = a + b
            elif i == "-":
                c = b - a
            elif i == "*":
                c = a * b
            elif i == "/":
                c = b/a
            stack.append(c)
    return stack.pop()
            
            
