import sys
#from sys import argv

def content(file):
    with open(file) as f:
        return f.read()


def lines(s):
    return len(s.splitlines())

def words(s):
    w = 0
    for i in s.splitlines():
        if i == "":
            continue
        else:
            a = i.split(" ")
            w = w + len(a)
    return w

def characters(s):
    return len(s)


sys.argv.pop(0)
for file in sys.argv:
    r = content(file)
    print(lines(r)," ",words(r)," ",characters(r)," ",file )
