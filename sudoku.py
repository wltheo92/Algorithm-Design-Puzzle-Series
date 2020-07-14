#Test case 1
P=[[5,3,0,0,7,0,0,0,0],[6,0,0,1,9,5,0,0,0],[0,9,8,0,0,0,0,6,0],
   [8,0,0,0,6,0,0,0,3],[4,0,0,8,0,3,0,0,1],[7,0,0,0,2,0,0,0,6],
   [0,6,0,0,0,0,2,8,0],[0,0,0,4,1,9,0,0,5],[0,0,0,0,8,0,0,7,9]]
"""
#Test case 2
P=[[0,0,2,7,0,0,0,0,1],[0,0,1,2,6,0,7,0,0],[4,0,0,0,5,1,3,0,0],
   [9,7,6,1,0,0,0,4,0],[0,3,0,0,4,0,0,7,0],[0,4,0,0,0,5,9,2,6],
   [0,0,4,5,3,0,0,0,9],[0,0,3,0,2,9,4,0,0],[6,0,0,0,0,8,2,0,0]]
   
#Test case 3
P=[[2,0,0,0,7,9,0,6,0],[0,3,0,5,0,0,0,0,8],[0,6,0,2,3,0,0,7,0],
   [8,2,3,9,0,0,6,0,0],[0,0,1,0,6,0,7,0,0],[0,0,6,0,0,4,1,8,2],
   [0,1,0,0,8,3,0,4,0],[4,0,0,0,0,1,0,3,0],[0,7,0,4,9,0,0,0,6]]

#Test case 4
P=[[8,0,0,0,7,0,6,2,0],[0,0,0,0,9,6,0,7,8],[0,6,0,8,0,0,3,0,5],
   [0,9,0,6,0,8,0,0,0],[3,0,0,0,0,0,0,0,6],[0,0,0,2,0,1,0,3,0],
   [9,0,7,0,0,4,0,6,0],[2,5,0,9,8,0,0,0,0],[0,3,4,0,6,0,0,0,2]]

#Test case 5
P=[[3,0,0,0,0,5,1,0,0],[1,0,0,9,6,0,0,5,0],[0,0,0,0,1,0,0,0,0],
   [5,3,1,0,0,0,9,0,8],[0,9,0,0,0,0,0,4,0],[8,0,2,0,0,0,6,3,5],
   [0,0,0,0,2,0,0,0,0],[0,5,0,0,8,3,0,0,6],[0,0,8,7,0,0,0,0,3]]

#Test case 6
P=[[7,3,0,0,0,0,0,6,0],[0,0,0,0,0,1,0,0,0],[6,4,2,8,0,0,1,0,5],
   [5,0,0,4,7,0,9,0,0],[0,0,0,0,0,0,0,0,0],[0,0,9,0,5,3,0,0,2],
   [8,0,3,0,0,9,7,2,4],[0,0,0,3,0,0,0,0,0],[0,9,0,0,0,0,0,3,6]]
   
#Test case 7
P=[[0,0,0,0,8,0,0,7,0],[9,3,5,2,7,0,0,0,6],[0,0,0,0,0,5,0,2,1],
   [4,0,0,0,0,0,0,0,0],[0,8,0,9,0,4,0,3,0],[0,0,0,0,0,0,0,0,8],
   [8,2,0,3,0,0,0,0,0],[7,0,0,0,6,8,2,5,9],[0,5,0,0,4,0,0,0,0]]
   
#Test case 8
P=[[0,0,0,0,0,5,0,7,0],[1,0,0,0,0,0,0,4,9],[5,7,2,0,0,0,0,0,0],
   [0,0,8,0,6,0,0,0,7],[0,0,0,0,0,2,3,0,6],[9,0,0,5,0,7,0,0,0],
   [7,0,0,0,0,9,0,0,5],[0,9,0,0,5,0,0,0,0],[0,0,0,0,0,3,0,2,8]]
   
#Test case 9
P=[[0,0,0,6,0,0,0,0,0],[0,0,0,0,0,7,0,0,1],[5,1,3,9,0,0,6,0,0],
   [0,6,0,0,0,0,0,0,0],[0,8,0,0,0,5,0,9,0],[0,0,0,0,0,6,2,0,4],
   [9,0,0,0,7,8,0,1,0],[1,5,0,0,2,0,0,0,0],[3,0,0,0,0,0,9,2,0]]
"""

#Grid object
class grid:
    def __init__(self,r,c):
        self.r=r
        self.c=c
        self.solved=0
        self.others=[]

#Definition of functions 
def complement(A):
    return [i for i in range(1,10) if i not in A]

def getRC(r):
    if r>=0 and r<3:return [0,1,2]
    elif r>=3 and r<6:return [3,4,5]
    else:return [6,7,8]

def solveIndividual(g):
    r,c=g.r,g.c
    for j in range(9):
        if j!=c:
            n=P[r][j]
            if n!=0 and n not in g.others:g.others.append(n)
    for j in range(9):
        if j!=r:
            n=P[j][c]
            if n!=0 and n not in g.others:g.others.append(n)
    for i in getRC(r):
        for j in getRC(c):
            if (i,j)!=(r,c):
                n=P[i][j]
                if n!=0 and n not in g.others:g.others.append(n)
    if len(g.others)==8:
        P[r][c]=complement(g.others)[0]
        g.solved=1

def solveBlock(ROWS,COLS):
    N,index=[],[]
    for r in ROWS:
        for c in COLS:
            if P[r][c]!=0:N.append(P[r][c])
            else:
                for j in range(len(Grids)):
                    g=Grids[j]
                    if g.solved==0 and g.r==r and g.c==c:index.append(j)
    for n in complement(N):
        p,tr,tc,It=0,None,None,None
        for j in index:
            if n not in Grids[j].others:
                p+=1
                tr=Grids[j].r
                tc=Grids[j].c
                It=index[j]
        if p==1:
            P[tr][tc]=n
            Grids[It].solved=1
            for e in Grids:
                if e.solved==0 and (e.r==tr or e.c==tc or e.r in ROWS or e.c in COLS):solveIndividual(e)

def solveRow(r):
    N,index=[],[]
    for c in range(9):
        if P[r][c]!=0:N.append(P[r][c])
        else:
            for j in range(len(Grids)):
                if Grids[j].solved==0 and Grids[j].r==r and Grids[j].c==c:index.append(j)
    for n in complement(N):
        p,tc,It=0,None,None
        for j in index:
            if n not in Grids[j].others:
                p+=1
                tc=Grids[j].c
                It=index[j]
        if p==1:
            P[r][tc]=n
            Grids[It].solved=1
            for e in Grids:
                if e.solved==0 and (e.r==r or e.c==tc or e.r in getRC(r) or e.c in getRC(tc)):solveIndividual(e)

def solveCol(c):
    N,index=[],[]
    for r in range(9):
        if P[r][c]!=0:N.append(P[r][c])
        else:
            for j in range(len(Grids)):
                if Grids[j].solved==0 and Grids[j].r==r and Grids[j].c==c:index.append(j)
    for n in complement(N):
        p,tr,It=0,None,None
        for j in index:
            if n not in Grids[j].others:
                p+=1
                tr=Grids[j].r
                It=index[j]
        if p==1:
            P[tr][c]=n
            Grids[It].solved=1
            for e in Grids:
                if e.solved==0 and (e.r==tr or e.c==c or e.r in getRC(tr) or e.c in getRC(c)):solveIndividual(e)

def count(Grids):
    out=0
    for e in Grids:
        if e.solved==0:out+=1
    return out

#Overall flow
Grids=[]
for r in range(9):
    for c in range(9):
        if P[r][c]==0:Grids.append(grid(r,c))

while count(Grids):
    for e in Grids:
        if e.solved==0:solveIndividual(e)
    for i in range(0,7,3):
        for j in range(0,7,3):solveBlock(getRC(i),getRC(j))
    for r in range(9):solveRow(r)
    for c in range(9):solveCol(c)


