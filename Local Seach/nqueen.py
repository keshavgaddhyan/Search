import time


def printBoard(queen):
  for n in queen:
    print("- "*n+"Q"+" -"*(len(queen)-n-1))


def countAttack(queen):
    count = 0
    for row1 in range( 0, len(queen) ):
        for row2 in range( row1 + 1, len( queen ) ):
            if queen[row1] == queen[row2]:
                count += 1
            elif abs(queen[row1] - queen[row2]) == (row2 - row1):
                count += 1
    return count
    
def printMatrix (queen):
    xqueen= list(queen)
    b=""
    for i in range(0,len(queen)):
        for j in range(0,len(queen)):
            if queen[i]==j:
                b=b+"-  "
            else:
                xqueen[i]=j
                a=countAttack(xqueen)
                b=b+str(a)+"  "
                xqueen=list(queen)
                
        print(b)
        b=""
        
        
def moveOne(queen):
    xqueen= list(queen)
    x=0
    y=0
    b= len(queen)
    for i in range(0,len(queen)):
        for j in range(0,len(queen)):
                
            if xqueen[i]==j:
                continue
            else:
                xqueen[i]=j
                a=countAttack(xqueen)
                if b >= a :
                    b=a
                    x=i
                    y=j
            xqueen=list(queen)
            
    xqueen[x]=y
    return xqueen
    
def printMatrix2(queen):
    xqueen= list(queen)
    b=""
    for i in range(0,len(queen)):
        for j in range(0,len(queen)):
            if i==j:
                b=b+"-  "
            else:
                temp=xqueen[i]
                xqueen[i]=xqueen[j]
                xqueen[j]=temp
                b=b+str(countAttack(xqueen))+"  "
                xqueen=list(queen)
                
        print(b)
        b=""
        
def moveTwo(queen):
    xqueen= list(queen)
    b=len(queen)
    for i in range(0,len(queen)):
        for j in range(0,len(queen)):
            if i==j:
               continue
            else:
                temp=xqueen[i]
                xqueen[i]=xqueen[j]
                xqueen[j]=temp
                a=countAttack(xqueen)
                if b >= a :
                    b=a
                    x=i
                    y=j
                xqueen=list(queen)
                
        
            temp=0
            
    temp=xqueen[x]
    xqueen[x]=xqueen[y]
    xqueen[y]=temp    
    return xqueen
    
def localSearch2(queen):
    
    x=0
    etime=0
    stime=time.clock()
    while countAttack(queen) > 0:
        queen = moveTwo(queen)
        x=x+1
        etime=time.clock()
    
    print("using move two()")
    print("Number of steps = ", x-1)
    print("time taken for execution = ",etime-stime)
    print("")
  
def localSearch(queen):
    x=0
    etime=0
    stime=time.clock()
    while countAttack(queen) > 0:
        queen = moveOne(queen)
        x=x+1
        etime=time.clock()
    print("using move one()")
    print("Number of steps = ", x-1)
    print("time taken for execution = ",etime-stime)
  
  
  
  
  
  
  
  