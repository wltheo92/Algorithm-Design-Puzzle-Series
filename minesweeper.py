import pygame as p
import sys
p.init()
w=p.display.set_mode((300,600))
p.display.set_caption("Mine sweeper")
clock=p.time.Clock()
fps=60
font=p.font.Font("OpenSans-BoldItalic.ttf",12)

class g:
    def __init__(self,state,center_number):
        self.state=state
        self.center_number=center_number

def solve(r,c):
    count=0
    g=Grids[r][c]
    if g.state==1:
        if g.center_number==0:
            for dr in range(-1,2):
                for dc in range(-1,2):
                    rr,cc=r+dr,c+dc
                    if rr>=0 and rr<20 and cc>=0 and cc<10:
                        if Grids[rr][cc].state==0:
                            Grids[rr][cc].state=1
                            Grids[rr][cc].center_number=int(center_numbers[rr][cc])
                            count+=1
        else:
            danger,unknown,unknown_grid_xy=0,0,[]
            for dr in range(-1,2):
                for dc in range(-1,2):
                    rr,cc=r+dr,c+dc
                    if rr>=0 and rr<20 and cc>=0 and cc<10:
                        if Grids[rr][cc].state==0:
                            unknown+=1
                            unknown_grid_xy.append((rr,cc))
                        if Grids[rr][cc].state==2: danger+=1
            if danger==0:
                if unknown==g.center_number:
                    for rr,cc in unknown_grid_xy:
                        Grids[rr][cc].state=2
                        count+=1
            else:
                if g.center_number==danger and unknown!=0:
                    for rr,cc in unknown_grid_xy:
                        Grids[rr][cc].state=1
                        Grids[rr][cc].center_number=int(center_numbers[rr][cc])
                        count+=1
                else:
                    if g.center_number==unknown+danger:
                        for rr,cc in unknown_grid_xy:
                            Grids[rr][cc].state=2
                            count+=1
    return count

#Test case 1
center_numbers=[[-1,3,1,1,1,1,2,-1,1,0],
                [-1,3,-1,2,2,-1,2,1,1,0],
                [1,3,2,3,-1,3,2,1,0,0],
                [1,2,-1,2,1,2,-1,2,1,0],
                [1,-1,2,1,0,1,2,-1,2,1],
                [2,2,2,0,0,0,2,4,-1,3],
                [1.-1,1,0,0,0,1,-1,-1,-1],
                [1,1,1,0,1,1,3,4,5,3],
                [0,1,1,1,1,-1,2,-1,-1,1],
                [0,1,-1,1,1,1,2,3,3,2],
                [0,1,1,1,0,0,0,2,-1,2],
                [0,0,0,1,2,2,1,2,-1,2],
                [0,1,2,3,-1,-1,1,1,2,2],
                [0,2,-1,-1,4,3,2,0,1,-1],
                [0,2,-1,4,3,-1,1,1,2,2],
                [0,1,1,2,-1,2,1,1,-1,1],
                [0,0,0,1,1,1,0,2,2,2],
                [1,1,1,0,1,1,1,1,-1,1],
                [2,-1,1,0,2,-1,2,1,1,1],
                [-1,2,1,0,2,-1,2,0,0,0]]

Grids=[[g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(1,2),g(1,1),g(1,2),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(1,2),g(1,1),g(1,0),g(1,1),g(1,2),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(1,2),g(1,0),g(1,0),g(1,0),g(1,2),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(1,1),g(1,0),g(1,0),g(1,0),g(1,1),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(1,1),g(1,0),g(1,1),g(1,1),g(1,3),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(1,1),g(1,1),g(1,1),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)],
       [g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0),g(0,0)]]

old_count=26

                
while 1:
    new_count=old_count
    for r in range(20):
        for c in range(10):new_count+=solve(r,c)
    for e in p.event.get():
        if e.type==p.QUIT:
            p.quit()
            sys.exit()
    w.fill(p.Color("white"))
    for r in range(20):
        for c in range(10):
            g=Grids[r][c]
            textsurf=font.render(str(g.center_number),1,p.Color("black"))
            p.draw.rect(w,p.Color("white" if g.state==0 else ("blue" if \
            g.state==1 else "red")),p.Rect(c*30,r*30,30,30))
            w.blit(textsurf,(c*30+10,r*30+10))
    p.display.update()
    clock.tick(fps)
    if new_count==old_count: break
    old_count=new_count
