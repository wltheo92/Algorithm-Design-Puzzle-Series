def solve(r,c):
    k,unknown,danger,Unknown=P[r][c],0,0,[]
    if not k:
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                R,C=r+dr,c+dc
                if R>=0 and R<ROWS and C>=0 and C<COLS:
                    if P[R][C]==-1:P[R][C]=Data[R][C]
    else:
        for dr in [-1,0,1]:
            for dc in [-1,0,1]:
                R,C=r+dr,c+dc
                if R>=0 and R<ROWS and C>=0 and C<COLS:
                    if P[R][C]==-1:
                        unknown+=1
                        Unknown.append((R,C))
                    elif P[R][C]==-2:danger+=1
        if not danger:
            if unknown==k:
                for i,j in Unknown:P[i][j]=-2
        else:
            if danger==k:
                for i,j in Unknown:P[i][j]=Data[i][j]
            elif danger+unknown==k:
                for i,j in Unknown:P[i][j]=-2

def count(P,ROWS,COLS):
    o=0
    for i in range(ROWS):
        for j in range(COLS):
            if P[i][j]==-1:o+=1
    return o

#Test case 1
Data=[[0,0,0,0,0,0],[0,1,2,2,1,0],[0,1,-2,-2,2,0],
      [0,1,3,-2,3,1],[0,0,1,2,-2,1],[0,0,0,1,1,1],
      [0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0],
      [-2,1,0,0,1,1],[1,1,0,0,1,-2],[1,2,2,3,3,2],
      [-2,2,-2,-2,-2,1]]

P=[[0,0,0,0,0,0],[0,1,2,2,1,0],[0,1,-1,-1,2,0],
   [0,1,3,-1,3,1],[0,0,1,2,-1,-1],[0,0,0,1,1,1],
   [0,0,0,0,0,0],[0,0,0,0,0,0],[1,1,0,0,0,0],
   [-1,1,0,0,1,1],[-1,1,0,0,1,-1],[-1,2,2,3,3,-1],
   [-1,-1,-1,-1,-1,-1]]

ROWS=13
COLS=6
"""
#Test case 2

Data=[[1,1,1,0,0,0],[2,-2,1,0,0,0],[-2,2,1,0,0,0],
      [1,1,0,0,0,0],[1,1,0,0,0,0],[-2,1,0,0,0,0],
      [3,3,1,0,0,0],[-2,-2,1,1,1,1],[2,2,1,1,-2,1]]

P=[[-1,-1,1,0,0,0],[-1,-1,1,0,0,0],[-1,2,1,0,0,0],
   [-1,1,0,-1,0,0],[-1,1,0,0,0,0],[-1,1,0,0,0,0],
   [-1,3,1,0,0,0],[-1,-1,1,1,1,1],[-1,-1,-1,-1,-1,-1]]

ROWS=9
COLS=6

#Test case 3
Data=[[1,-2,1,0,0,0,1,2,-2,-2],
      [1,1,1,0,1,2,4,-2,4,2],
      [0,1,2,2,2,-2,-2,-2,3,0],
      [0,1,-2,-2,3,2,4,-2,2,0],
      [0,1,3,-2,2,0,1,1,1,0],
      [1,1,1,1,1,0,0,1,1,1],
      [-2,1,0,0,0,0,1,2,-2,1],
      [1,1,0,0,0,0,1,-2,2,1],
      [1,2,2,1,0,0,1,2,2,1],
      [1,-2,-2,1,0,0,0,1,-2,2],
      [2,3,2,1,0,0,0,1,3,-2],
      [-2,1,0,0,0,1,1,1,2,-2],
      [1,1,0,1,1,3,-2,2,1,1],
      [0,0,0,1,-2,4,-2,3,0,0],
      [1,1,0,1,1,3,-2,2,1,1],
      [-2,2,0,0,0,1,1,1,1,-2],
      [-2,3,2,1,2,1,1,1,2,2]]

P=[[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
   [-1,-1,-1,-1,3,2,4,-1,-1,-1],
   [-1,-1,-1,-1,2,0,1,1,-1,-1],
   [-1,1,1,1,1,0,0,1,-1,-1],
   [-1,1,0,0,0,0,1,2,-1,-1],
   [-1,1,0,0,0,0,1,-1,-1,-1],
   [-1,2,2,1,0,0,1,2,-1,-1],
   [-1,-1,-1,1,0,0,0,1,-1,-1],
   [-1,3,2,1,0,0,0,1,-1,-1],
   [-1,1,0,0,0,1,1,1,-1,-1],
   [1,1,0,1,1,3,-1,-1,-1,-1],
   [0,0,0,1,-1,-1,-1,-1,-1,-1],
   [1,1,0,1,1,3,-1,-1,-1,-1],
   [-1,2,0,0,0,1,-1,-1,-1,-1],
   [-1,3,2,1,2,1,-1,-1,-1,-1]]

ROWS=17
COLS=10
"""

#main function
while count(P,ROWS,COLS):
    for r in range(ROWS):
        for c in range(COLS):
            if P[r][c]>=0:solve(r,c)

#Additional code to visualize result
import pygame as p,sys
p.init()
w=p.display.set_mode((30*COLS,30*ROWS))
p.display.set_caption("Mine sweeper")
clock=p.time.Clock()
fps=60
font=p.font.Font("OpenSans-BoldItalic.ttf",12)
while 1:
    for e in p.event.get():
        if e.type==p.QUIT:
            p.quit()
            sys.exit()
    w.fill(p.Color("white"))
    for r in range(ROWS):
        for c in range(COLS):
            g=P[r][c]
            p.draw.rect(w,p.Color("white" if g==-1 else ("red" if \
            g==-2 else "blue")),p.Rect(c*30,r*30,30,30))
            if g>=0:
                textsurf=font.render(str(g),1,p.Color("black"))
                w.blit(textsurf,(c*30+10,r*30+10))
    p.display.update()
    clock.tick(fps)
