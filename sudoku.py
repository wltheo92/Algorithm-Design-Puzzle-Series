class g:
    def __init__(self,number):
        self.number=number
        self.others=[]

Grids=[[g(5),g(3),g(-1),g(-1),g(7),g(-1),g(-1),g(-1),g(-1)],
       [g(6),g(-1),g(-1),g(1),g(9),g(5),g(-1),g(-1),g(-1)],
       [g(-1),g(9),g(8),g(-1),g(-1),g(-1),g(-1),g(6),g(-1)],
       [g(8),g(-1),g(-1),g(-1),g(6),g(-1),g(-1),g(-1),g(3)],
       [g(4),g(-1),g(-1),g(8),g(-1),g(3),g(-1),g(-1),g(1)],
       [g(7),g(-1),g(-1),g(-1),g(2),g(-1),g(-1),g(-1),g(6)],
       [g(-1),g(6),g(-1),g(-1),g(-1),g(-1),g(2),g(8),g(-1)],
       [g(-1),g(-1),g(-1),g(4),g(1),g(9),g(-1),g(-1),g(5)],
       [g(-1),g(-1),g(-1),g(-1),g(8),g(-1),g(-1),g(7),g(9)]]

def complement(S):
    for j in range(1,10):
        if j not in S:return j

def update(r,c):
    g=Grids[r][c]
    if g.number==-1:
        for j in range(9):
            nr=Grids[r][j].number
            if nr!=-1 and nr not in g.others:g.others.append(nr)
            nc=Grids[j][c].number
            if nc!=-1 and nc not in g.others:g.others.append(nc)
        if r>=0 and r<3:ROWS=[0,1,2]
        elif r>=3 and r<6:ROWS=[3,4,5]
        else: ROWS=[6,7,8]
        if c>=0 and c<3:COLS=[0,1,2]
        elif c>=3 and c<6:COLS=[3,4,5]
        else: COLS=[6,7,8]
        for r in ROWS:
            for c in COLS:
                n=Grids[r][c].number
                if n!=-1 and n not in g.others:g.others.append(n)
        if len(g.others)==8:
            g.number=complement(g.others)
            return 1
    return 0

def solveBlock(r,c):
    count=0
    if r>=0 and r<3:ROWS=[0,1,2]
    elif r>=3 and r<6:ROWS=[3,4,5]
    else: ROWS=[6,7,8]
    if c>=0 and c<3:COLS=[0,1,2]
    elif c>=3 and c<6:COLS=[3,4,5]
    else: COLS=[6,7,8]
    nums,xy_list=[],[]
    for i in ROWS:
        for j in COLS:
            if Grids[i][j].number!=-1:nums.append(Grids[i][j].number)
            else:xy_list.append((i,j))
    for I in range(1,10):
        if I not in nums:
            possible=0
            store=[]
            for i,j in xy_list:
                g=Grids[i][j]
                if I not in g.others:
                    possible+=1
                    store.append((i,j))
            if possible==1:
                r,c=store[0]
                Grids[r][c].number=I
                count+=1
    return count

old_count=30

import pygame as p
import sys
p.init()
w=p.display.set_mode((270,270))
p.display.set_caption("Sudoku")
clk=p.time.Clock()
font=p.font.Font("OpenSans-BoldItalic.ttf",12)

while 1:
    for e in p.event.get():
        if e.type==p.QUIT:
            p.quit()
            sys.exit()
    new_count=old_count
    for i in range(9):
        for j in range(9):new_count+=update(i,j)
    for i in range(9):
        for j in range(9):new_count+=solveBlock(i,j)
    for r in range(9):
        for c in range(9):
            g=Grids[r][c]
            p.draw.rect(w,p.Color("light blue" if g.number!=-1 else "yellow"),p.Rect(c*30,r*30,30,30))
            p.draw.line(w,p.Color("black"),(0,0),(0,270),3)
            p.draw.line(w,p.Color("black"),(30,0),(30,270),1)
            p.draw.line(w,p.Color("black"),(60,0),(60,270),1)
            p.draw.line(w,p.Color("black"),(90,0),(90,270),3)
            p.draw.line(w,p.Color("black"),(120,0),(120,270),1)
            p.draw.line(w,p.Color("black"),(150,0),(150,270),1)
            p.draw.line(w,p.Color("black"),(180,0),(180,270),3)
            p.draw.line(w,p.Color("black"),(210,0),(210,270),1)
            p.draw.line(w,p.Color("black"),(240,0),(240,270),1)
            p.draw.line(w,p.Color("black"),(270,0),(270,270),3)
            p.draw.line(w,p.Color("black"),(0,0),(270,0),3)
            p.draw.line(w,p.Color("black"),(0,30),(270,30),1)
            p.draw.line(w,p.Color("black"),(0,60),(270,60),1)
            p.draw.line(w,p.Color("black"),(0,90),(270,90),3)
            p.draw.line(w,p.Color("black"),(0,120),(270,120),1)
            p.draw.line(w,p.Color("black"),(0,150),(270,150),1)
            p.draw.line(w,p.Color("black"),(0,180),(270,180),3)
            p.draw.line(w,p.Color("black"),(0,210),(270,210),1)
            p.draw.line(w,p.Color("black"),(0,240),(270,240),1)
            p.draw.line(w,p.Color("black"),(0,270),(270,270),3)
            
            if g.number!=-1:
                text=font.render(str(g.number),1,p.Color("black"))
                w.blit(text,(c*30+10,r*30+10))
    p.display.update()
    clk.tick(2)
    if new_count==old_count:break
    old_count=new_count




