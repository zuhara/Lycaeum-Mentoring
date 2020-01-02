def function1(p):
    m = [[False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],
         [False , False , False , False , False , False , False , False],]
    if p == []:
        return m
    else:
        for i in p:
            m[i[0]][i[1]] = True
        return m
    
def next_gen(l):
     for i in range(8):
         for j in range(8):
             if l[i][j]:
                 print([i,j])
                 print(l[i-1][j])
                 #write a functin to find the neighbours
                 #put [i,j] in that function and get the neighbours
                 #check $ rules
     
    
                 
list = [[False , False , False , False , False , False , False , False],
        [False , False , False , False , False , False , False , False],
        [False , False , False , False , False , False , False , False],
        [False , False , False , True , False , False , False , False],
        [False , False , False , True  , False , False , False , False],
        [False , True , False , False , False , False , False , False],
        [False , True , False , False , False , False , False , False],
        [False , True , False , False , False , False , False , False],]

next_gen(list)
