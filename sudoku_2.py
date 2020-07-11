"""
#Test case 1
problem=[[5,3,0,0,7,0,0,0,0],
         [6,0,0,1,9,5,0,0,0],
         [0,9,8,0,0,0,0,6,0],
         [8,0,0,0,6,0,0,0,3],
         [4,0,0,8,0,3,0,0,1],
         [7,0,0,0,2,0,0,0,6],
         [0,6,0,0,0,0,2,8,0],
         [0,0,0,4,1,9,0,0,5],
         [0,0,0,0,8,0,0,7,9]]

#Test case 2
problem=[[0,0,2,7,0,0,0,0,1],
         [0,0,1,2,6,0,7,0,0],
         [4,0,0,0,5,1,3,0,0],
         [9,7,6,1,0,0,0,4,0],
         [0,3,0,0,4,0,0,7,0],
         [0,4,0,0,0,5,9,2,6],
         [0,0,4,5,3,0,0,0,9],
         [0,0,3,0,2,9,4,0,0],
         [6,0,0,0,0,8,2,0,0]]

#Test case 3
problem=[[2,0,0,0,7,9,0,6,0],
         [0,3,0,5,0,0,0,0,8],
         [0,6,0,2,3,0,0,7,0],
         [8,2,3,9,0,0,6,0,0],
         [0,0,1,0,6,0,7,0,0],
         [0,0,6,0,0,4,1,8,2],
         [0,1,0,0,8,3,0,4,0],
         [4,0,0,0,0,1,0,3,0],
         [0,7,0,4,9,0,0,0,6]]

#Test case 4
problem=[[8,0,0,0,7,0,6,2,0],
         [0,0,0,0,9,6,0,7,8],
         [0,6,0,8,0,0,3,0,5],
         [0,9,0,6,0,8,0,0,0],
         [3,0,0,0,0,0,0,0,6],
         [0,0,0,2,0,1,0,3,0],
         [9,0,7,0,0,4,0,6,0],
         [2,5,0,9,8,0,0,0,0],
         [0,3,4,0,6,0,0,0,2]]

#Test case 5
problem=[[3,0,0,0,0,5,1,0,0],
         [1,0,0,9,6,0,0,5,0],
         [0,0,0,0,1,0,0,0,0],
         [5,3,1,0,0,0,9,0,8],
         [0,9,0,0,0,0,0,4,0],
         [8,0,2,0,0,0,6,3,5],
         [0,0,0,0,2,0,0,0,0],
         [0,5,0,0,8,3,0,0,6],
         [0,0,8,7,0,0,0,0,3]]

#Test case 6
problem=[[7,3,0,0,0,0,0,6,0],
         [0,0,0,0,0,1,0,0,0],
         [6,4,2,8,0,0,1,0,5],
         [5,0,0,4,7,0,9,0,0],
         [0,0,0,0,0,0,0,0,0],
         [0,0,9,0,5,3,0,0,2],
         [8,0,3,0,0,9,7,2,4],
         [0,0,0,3,0,0,0,0,0],
         [0,9,0,0,0,0,0,3,6]]

#Test case 7
problem=[[0,0,0,0,8,0,0,7,0],
         [9,3,5,2,7,0,0,0,6],
         [0,0,0,0,0,5,0,2,1],
         [4,0,0,0,0,0,0,0,0],
         [0,8,0,9,0,4,0,3,0],
         [0,0,0,0,0,0,0,0,8],
         [8,2,0,3,0,0,0,0,0],
         [7,0,0,0,6,8,2,5,9],
         [0,5,0,0,4,0,0,0,0]]

#Test case 8
problem=[[0,0,0,0,0,5,0,7,0],
         [1,0,0,0,0,0,0,4,9],
         [5,7,2,0,0,0,0,0,0],
         [0,0,8,0,6,0,0,0,7],
         [0,0,0,0,0,2,3,0,6],
         [9,0,0,5,0,7,0,0,0],
         [7,0,0,0,0,9,0,0,5],
         [0,9,0,0,5,0,0,0,0],
         [0,0,0,0,0,3,0,2,8]]

#Test case 9
problem=[[0,0,0,6,0,0,0,0,0],
         [0,0,0,0,0,7,0,0,1],
         [5,1,3,9,0,0,6,0,0],
         [0,6,0,0,0,0,0,0,0],
         [0,8,0,0,0,5,0,9,0],
         [0,0,0,0,0,6,2,0,4],
         [9,0,0,0,7,8,0,1,0],
         [1,5,0,0,2,0,0,0,0],
         [3,0,0,0,0,0,9,2,0]]
"""

#Grid object
class grid:
    def __init__(self,r,c):
        self.r=r
        self.c=c
        self.solved=0
        self.A=[]

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
            n=problem[r][j]
            if n!=0 and n not in g.A:g.A.append(n)
    for j in range(9):
        if j!=r:
            n=problem[j][c]
            if n!=0 and n not in g.A:g.A.append(n)
    for i in getRC(r):
        for j in getRC(c):
            if (i,j)!=(r,c):
                n=problem[i][j]
                if n!=0 and n not in g.A:g.A.append(n)
    if len(g.A)==8:
        problem[r][c]=complement(g.A)[0]
        g.solved=1
        return 1
    return 0

def solveBlock(ROWS,COLS):
    N,store,count=[],[],0
    for r in ROWS:
        for c in COLS:
            if problem[r][c]!=0:N.append(problem[r][c])
            else:
                for e in Grids:
                    if e.solved==0:
                        if e.r==r and e.c==c:store.append(e)
    for n in complement(N):
        p,grid=0,None
        for e in store:
            if n not in e.A:
                p+=1
                grid=e
        if p==1:
            problem[grid.r][grid.c]=n
            grid.solved=1
            count+=1
            for e in Grids:
                if e.solved==0 and (e.r==grid.r or e.c==grid.c or e.r in ROWS or e.c in COLS):count+=solveIndividual(e)
    return count

def solveRow(r):
    N,store,count=[],[],0
    for c in range(9):
        if problem[r][c]!=0:N.append(problem[r][c])
        else:
            for e in Grids:
                if e.solved==0:
                    if e.r==r and e.c==c:store.append(e)
    for n in complement(N):
        p,grid=0,None
        for e in store:
            if n not in e.A:
                p+=1
                grid=e
        if p==1:
            problem[grid.r][grid.c]=n
            count+=1
            for e in Grids:
                if e.solved==0 and (e.r==grid.r or e.c==grid.c or e.r in getRC(grid.r) or e.c in getRC(grid.c)):count+=solveIndividual(e)
    return count

def solveCol(c):
    N,store,count=[],[],0
    for r in range(9):
        if problem[r][c]!=0:N.append(problem[r][c])
        else:
            for e in Grids:
                if e.solved==0:
                    if e.r==r and e.c==c:store.append(e)
    for n in complement(N):
        p,grid=0,None
        for e in store:
            if n not in e.A:
                p+=1
                grid=e
        if p==1:
            problem[grid.r][grid.c]=n
            count+=1
            for e in Grids:
                if e.solved==0 and (e.r==r or e.c==c or e.r in getRC(grid.r) or e.c in getRC(grid.c)):count+=solveIndividual(e)
    return count

import pygame as p
p.init()
w=p.display.set_mode((540,540))
clk=p.time.Clock()
f=p.font.Font("OpenSans-BoldItalic.ttf",25)
"""
while 1:
    for e in p.event.get():
        if e.type==p.QUIT:
            p.quit()
    for r in range(9):
        for c in range(9):
            p.draw.rect(w,p.Color("blue" if problem[r][c]!=0 else "yellow"),p.Rect(c*60,r*60,60,60))
            p.draw.line(w,p.Color("black"),(0,0),(540,0),5)
            p.draw.line(w,p.Color("black"),(0,60),(540,60),1)
            p.draw.line(w,p.Color("black"),(0,120),(540,120),1)
            p.draw.line(w,p.Color("black"),(0,180),(540,180),3)
            p.draw.line(w,p.Color("black"),(0,240),(540,240),1)
            p.draw.line(w,p.Color("black"),(0,300),(540,300),1)
            p.draw.line(w,p.Color("black"),(0,360),(540,360),3)
            p.draw.line(w,p.Color("black"),(0,420),(540,420),1)
            p.draw.line(w,p.Color("black"),(0,480),(540,480),1)
            p.draw.line(w,p.Color("black"),(0,540),(540,540),5)
            p.draw.line(w,p.Color("black"),(0,0),(0,540),5)
            p.draw.line(w,p.Color("black"),(60,0),(60,540),1)
            p.draw.line(w,p.Color("black"),(120,0),(120,540),1)
            p.draw.line(w,p.Color("black"),(180,0),(180,540),3)
            p.draw.line(w,p.Color("black"),(240,0),(240,540),1)
            p.draw.line(w,p.Color("black"),(300,0),(300,540),1)
            p.draw.line(w,p.Color("black"),(360,0),(360,540),3)
            p.draw.line(w,p.Color("black"),(420,0),(420,540),1)
            p.draw.line(w,p.Color("black"),(480,0),(480,540),1)
            p.draw.line(w,p.Color("black"),(540,0),(540,540),5)
            if problem[r][c]!=0:
                text=f.render(str(problem[r][c]),1,p.Color("black"))
                w.blit(text,(c*60+22,r*60+15))
    p.display.update()
    clk.tick(20)
"""
#Overall flow
Grids=[]
for r in range(9):
    for c in range(9):
        if problem[r][c]==0:Grids.append(grid(r,c))
old=len(Grids)
while 1:
    new=old
    for e in Grids:
        if e.solved==0:new-=solveIndividual(e)
    R=[[0,1,2],[3,4,5],[6,7,8]]
    C=[[0,1,2],[3,4,5],[6,7,8]]
    for r in R:
        for c in C:new-=solveBlock(r,c)
    for r in range(9):new-=solveRow(r)
    for c in range(9):new-=solveCol(c)
    if new==old:break
    old=new

while 1:
    for e in p.event.get():
        if e.type==p.QUIT:
            p.quit()
    for r in range(9):
        for c in range(9):
            p.draw.rect(w,p.Color("blue" if problem[r][c]!=0 else "yellow"),p.Rect(c*60,r*60,60,60))
            p.draw.line(w,p.Color("black"),(0,0),(540,0),5)
            p.draw.line(w,p.Color("black"),(0,60),(540,60),1)
            p.draw.line(w,p.Color("black"),(0,120),(540,120),1)
            p.draw.line(w,p.Color("black"),(0,180),(540,180),3)
            p.draw.line(w,p.Color("black"),(0,240),(540,240),1)
            p.draw.line(w,p.Color("black"),(0,300),(540,300),1)
            p.draw.line(w,p.Color("black"),(0,360),(540,360),3)
            p.draw.line(w,p.Color("black"),(0,420),(540,420),1)
            p.draw.line(w,p.Color("black"),(0,480),(540,480),1)
            p.draw.line(w,p.Color("black"),(0,540),(540,540),5)
            p.draw.line(w,p.Color("black"),(0,0),(0,540),5)
            p.draw.line(w,p.Color("black"),(60,0),(60,540),1)
            p.draw.line(w,p.Color("black"),(120,0),(120,540),1)
            p.draw.line(w,p.Color("black"),(180,0),(180,540),3)
            p.draw.line(w,p.Color("black"),(240,0),(240,540),1)
            p.draw.line(w,p.Color("black"),(300,0),(300,540),1)
            p.draw.line(w,p.Color("black"),(360,0),(360,540),3)
            p.draw.line(w,p.Color("black"),(420,0),(420,540),1)
            p.draw.line(w,p.Color("black"),(480,0),(480,540),1)
            p.draw.line(w,p.Color("black"),(540,0),(540,540),5)
            if problem[r][c]!=0:
                text=f.render(str(problem[r][c]),1,p.Color("black"))
                w.blit(text,(c*60+22,r*60+15))
    p.display.update()
    clk.tick(20)
