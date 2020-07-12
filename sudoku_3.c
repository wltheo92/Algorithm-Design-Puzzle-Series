#include<stdlib.h>
#include<stdint.h>

typedef struct{
    uint8_t L;
    uint8_t*A;
} list;

typedef struct{
    uint8_t r,c,solved;
    list others;
} grid;

uint8_t contain(uint8_t c,uint8_t*A,uint8_t N){
    for(size_t i=0;i<N;i++){
        if(A[i]==c)return 1;
    }
    return 0;
}

list complement(list A){
    list L;
    L.L=0;
    L.A=(uint8_t*)calloc(9,1);
    for(uint8_t i=1;i<10;i++){
        if(!contain(i,A.A,A.L))L.A[L.L++]=i;
    }
    return L;
}

uint8_t*getRC(uint8_t n){
    uint8_t*o=(uint8_t*)calloc(3,1);
    if(n>=0&&n<3){
        o[0]=0;
        o[1]=1;
        o[2]=2;
    }
    else if(n>=3&&n<6){
        o[0]=3;
        o[1]=4;
        o[2]=5;
    }
    else{
        o[0]=6;
        o[1]=7;
        o[2]=8;
    }
    return o;
}

void solveIndividual(grid*g,uint8_t**P){
    size_t i,j;
    for(i=0;i<9;i++){
        if(i!=g->c){
            if(P[g->r][i]!=0&&!contain(P[g->r][i],g->others.A,g->others.L))g->others.A[g->others.L++]=P[g->r][i];
        }
    }
    for(i=0;i<9;i++){
        if(i!=g->r){
            if(P[i][g->c]!=0&&!contain(P[i][g->c],g->others.A,g->others.L))g->others.A[g->others.L++]=P[i][g->c];
        }
    }
    uint8_t*ROWS=getRC(g->r),*COLS=getRC(g->c);
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            uint8_t R=ROWS[i],C=COLS[j];
            if(R!=g->r&&C!=g->c){
                if(P[R][C]!=0&&!contain(P[R][C],g->others.A,g->others.L))g->others.A[g->others.L++]=P[R][C];
            }
        }
    }
    if(g->others.L==8){
        g->solved=1;
        P[g->r][g->c]=complement(g->others).A[0];
    }
}

void solveBlock(uint8_t*ROWS,uint8_t*COLS,uint8_t**P,grid*Grids,uint8_t GL){
    list N,M;
    N.L=0;
    N.A=(uint8_t*)calloc(9,1);
    uint8_t*index=(uint8_t*)calloc(9,1);
    size_t i,j,k,iL=0;
    for(i=0;i<3;i++){
        for(j=0;j<3;j++){
            uint8_t R=ROWS[i],C=COLS[j];
            if(P[R][C]!=0)N.A[N.L++]=P[R][C];
            else{
                for(k=0;k<GL;k++){
                    if(!Grids[k].solved){
                        if(Grids[k].r==R&&Grids[k].c==C)index[iL++]=k;
                    }
                }
            }
        }
    }
    M=complement(N);
    for(i=0;i<M.L;i++){
        uint8_t n=M.A[i],p=0,tr,tc,It;
        for(j=0;j<iL;j++){
            grid z=Grids[index[j]];
            if(!contain(n,z.others.A,z.others.L)){
                p+=1;
                tr=z.r;
                tc=z.c;
                It=j;
            }
        }
        if(p==1){
            Grids[It].solved=1;
            P[tr][tc]=n;
            for(k=0;k<GL;k++){
                grid w=Grids[k];
                if(!w.solved){
                    if(w.r==tr||w.c==tc||contain(w.r,ROWS,3)||contain(w.c,COLS,3))solveIndividual(&w,P);
                }
            }
        }
    }
}

void solveRow(uint8_t r,uint8_t**P,grid*Grids,uint8_t GL){
    size_t i,j,k,iL=0;
    list N,M;
    N.L=0;
    N.A=(uint8_t*)calloc(9,1);
    uint8_t*index=(uint8_t*)calloc(9,1);
    for(i=0;i<9;i++){
        if(P[r][i]!=0)N.A[N.L++]=P[r][i];
        else{
            for(j=0;j<GL;j++){
                if(!Grids[j].solved){
                    if(Grids[j].r==r&&Grids[j].c==i)index[iL++]=j;
                }
            }
        }
    }
    M=complement(N);
    for(i=0;i<M.L;i++){
        uint8_t n=M.A[i],p=0,tc,It;
        for(j=0;j<iL;j++){
            grid w=Grids[index[j]];
            if(!contain(n,w.others.A,w.others.L)){
                p+=1;
                tc=w.c;
                It=j;
            }
        }
        if(p==1){
            Grids[It].solved=1;
            P[r][tc]=n;
            for(k=0;k<GL;k++){
                grid z=Grids[k];
                if(!z.solved){
                    if(z.r==r||z.c==tc||contain(z.r,getRC(r),3)||contain(z.c,getRC(tc),3))solveIndividual(&Grids[k],P);
                }
            }
        }
    }
}

void solveCol(uint8_t c,uint8_t**P,grid*Grids,uint8_t GL){
    size_t i,j,k,iL=0;
    list N,M;
    N.L=0;
    N.A=(uint8_t*)calloc(9,1);
    uint8_t*index=(uint8_t*)calloc(9,1);
    for(i=0;i<9;i++){
        if(P[i][c]!=0)N.A[N.L++]=P[i][c];
        else{
            for(j=0;j<GL;j++){
                if(!Grids[j].solved){
                    if(Grids[j].r==i&&Grids[j].c==c)index[iL++]=j;
                }
            }
        }
    }
    M=complement(N);
    for(i=0;i<M.L;i++){
        uint8_t n=M.A[i],p=0,tr,It;
        for(j=0;j<iL;j++){
            grid w=Grids[index[j]];
            if(!contain(n,w.others.A,w.others.L)){
                p+=1;
                tr=w.r;
                It=j;
            }
        }
        if(p==1){
            Grids[It].solved=1;
            P[tr][c]=n;
            for(k=0;k<GL;k++){
                grid z=Grids[k];
                if(!z.solved){
                    if(z.r==tr||z.c==c||contain(z.r,getRC(tr),3)||contain(z.c,getRC(c),3))solveIndividual(&Grids[k],P);
                }
            }
        }
    }
}

uint8_t count(grid*Grids,size_t GL){
    uint8_t o=0;
    for(size_t i=0;i<GL;i++){
        if(!Grids[i].solved)o++;
    }
    return o;
}

int main(void){
    size_t i,j;

    //Define Sudoku problem
    uint8_t**P=(uint8_t**)calloc(9,9);
    for(i=0;i<9;i++)P[i]=(uint8_t*)calloc(9,1);
    P[0][0]=0;P[0][1]=0;P[0][2]=0;
    P[1][0]=5;P[1][1]=8;P[1][2]=0;
    P[2][0]=0;P[2][1]=0;P[2][2]=0;
    /*******************************/
    P[0][3]=0;P[0][4]=0;P[0][5]=0;
    P[1][3]=0;P[1][4]=0;P[1][5]=0;
    P[2][3]=0;P[2][4]=5;P[2][5]=6;
    /*******************************/
    P[0][6]=4;P[0][7]=1;P[0][8]=5;
    P[1][6]=0;P[1][7]=6;P[1][8]=3;
    P[2][6]=0;P[2][7]=0;P[2][8]=0;
    /*******************************/
    P[3][0]=0;P[3][1]=9;P[3][2]=4;
    P[4][0]=0;P[4][1]=0;P[4][2]=2;
    P[5][0]=0;P[5][1]=0;P[5][2]=7;
    /*******************************/
    P[3][3]=0;P[3][4]=0;P[3][5]=3;
    P[4][3]=0;P[4][4]=0;P[4][5]=0;
    P[5][3]=0;P[5][4]=0;P[5][5]=9;
    /*******************************/
    P[3][6]=0;P[3][7]=0;P[3][8]=0;
    P[4][6]=3;P[4][7]=9;P[4][8]=6;
    P[5][6]=0;P[5][7]=0;P[5][8]=4;
    /*******************************/
    P[6][0]=0;P[6][1]=0;P[6][2]=5;
    P[7][0]=0;P[7][1]=4;P[7][2]=0;
    P[8][0]=0;P[8][1]=2;P[8][2]=0;
    /*******************************/
    P[6][3]=4;P[6][4]=0;P[6][5]=0;
    P[7][3]=0;P[7][4]=2;P[7][5]=0;
    P[8][3]=0;P[8][4]=6;P[8][5]=1;
    /*******************************/
    P[6][6]=6;P[6][7]=0;P[6][8]=0;
    P[7][6]=0;P[7][7]=0;P[7][8]=0;
    P[8][6]=5;P[8][7]=4;P[8][8]=9;
    
    grid*Grids=(grid*)calloc(81,sizeof(grid));
    uint8_t GL=0;
    for(i=0;i<9;i++){
        for(j=0;j<9;j++){
            if(P[i][j]==0){
                grid g;
                g.r=i;
                g.c=j;
                g.solved=0;
                list w;
                w.L=0;
                w.A=(uint8_t*)calloc(9,1);
                g.others=w;
                Grids[GL++]=g;
            }
        }
    }
    
    while(1){
        for(i=0;i<GL;i++)solveIndividual(&Grids[i],P);
        for(i=0;i<7;i+=3){
            for(j=0;j<7;j+=3)solveBlock(getRC(i),getRC(j),P,Grids,GL);
        }
        for(i=0;i<9;i++)solveRow(i,P,Grids,GL);
        for(i=0;i<9;i++)solveCol(i,P,Grids,GL);
        if(!count(Grids,GL))break;
    }
    return 0;
}
