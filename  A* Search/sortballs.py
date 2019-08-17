def applyMove(state,move):
    nstate= list(state)
    x=len(state)
    if move=="PUSH":
        for i in range(0,len(state)):
            if nstate[i] == 0:
                x=i
        
        if x!=0:
            temp=nstate[x]
            nstate[x]=nstate[x-1]
            nstate[x-1]=temp
        return nstate    
        
            
    if move=="PULL":
        for i in range(0,len(state)):
            if nstate[i]==0:
                x=i
                
        if x!= len(state)-1:
            temp=nstate[x]
            nstate[x]=nstate[x+1]
            nstate[x+1]=temp
        return nstate
            
    if move == "SWAP":
        for i in range(0,len(state)):
            if nstate[i]==0:
                x=i
                
        if x>1:
            temp=nstate[x-1]
            nstate[x-1]=nstate[x-2]
            nstate[x-2]=temp
        return nstate
        
    if move=="FLIP":
        l=0
        for i in range(0,len(state)):
            if nstate[i]==0:
                x=i
                
        for i in range(x+1,len(state)):
            if i<len(state)-1-l:
                temp=nstate[i]
                nstate[i]=nstate[len(state)-1-l]
                nstate[len(state)-1-l]=temp
                l=l+1
                
        return nstate  
    
    
def h(state):
    nstate=list(state)
    b=0
    fb=0
    c=0
    fc=0
    for i in range(0,len(state)):
         if nstate[i]==0:
            x=i
             
    fa=x*10   
    for i in range(0,len(state)):
        for j in range(i,len(state)):
            if nstate[i]>nstate[j] and nstate[j] !=0 and nstate[i] !=0:
                b=b+1
        if b>fb:
            fb=b
        b=0
                
    for i in range(len(state)-1,-1,-1):
        for j in range(i-1,-1,-1): 
            if nstate[i]>nstate[j] and nstate[j] !=0 and nstate[i] !=0:
                c=c+1
                
        
        if c>fc:
            fc=c
        c=0
        
             
            
    if  (fb*17)>(8+fc*17):
        d=8+fc*17
    else:
        d=fb*17
        
    final=fa+d
    return final
    
    
    
    
    
def pathcost(path):
    t=0
    for i in path:
        if i=="PUSH":
            t=t+10
        if i=="PULL":
            t=t+5
        if i=="FLIP":
            t=t+8
        if i=="SWAP":
            t=t+17
    return t        
    
    
def getNext(frontier):
    a=100000
    len=0
    flen=0
    for item in frontier:
        x=(h(item['state']))
        cos=pathcost(item['path'])
        x=x+cos
        len=len+1
        
        if x<a:
            a=x
            flen=len-1
        
    for item in frontier:
        x=(h(item['state']))
        cos=pathcost(item['path'])
        x=x+cos
        if a==x:
            q=item
            del frontier[flen]
            return q
        
def astarSearch(state):
  # initialize frontier using initial state of problem
  frontier = [ { 'state': state, 'path': [] } ]
  # while frontier is not empty
  while len(frontier) > 0:
    # choose a leaf node and remove it from frontier
    node = getNext(frontier)
 
    # if node contains a goal state
    if h(node['state']) == 0:
      # return corresponding solution
      return node['path']
 
    # expand the node adding the resulting nodes to the frontier
    for move in [ 'PUSH', 'PULL', 'SWAP', 'FLIP' ]:
      frontier.append( { 'state': applyMove(node['state'], move), 'path': node['path'] + [ move ] } )
 
  # return None if no solution is found
  return None