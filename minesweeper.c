/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

//#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>

//Answer
int Data[10][10]={
    {0,0,1,1,2,-2,1,0,0,0},
    {0,1,2,-2,3,2,1,0,0,0},
    {2,3,-2,3,-2,1,0,1,1,1},
    {-2,-2,2,2,1,1,0,1,-2,1},
    {2,2,1,0,0,0,0,1,1,1},
    {0,0,0,0,0,1,1,1,0,0},
    {0,0,0,0,0,1,-2,3,2,1},
    {0,0,0,0,0,1,2,-2,-2,1},
    {1,1,1,0,0,0,2,3,3,1},
    {2,-2,3,2,1,2,2,-2,2,1}
};

typedef struct{
    int r,c;
} pt;

void solve(int**P,int r,int c,int R,int C){
    int k=P[r][c],i,j,I,J,unknown=0,danger=0;
    pt*Unknown=(pt*)calloc(8,sizeof(pt));
    for(i=-1;i<2;i++){
        for(j=-1;j<2;j++){
            I=r+i;
            J=c+j;
            if(I>=0&&I<R&&J>=0&&J<C){
                if(P[I][J]==-1){
                    pt p={I,J};
                    Unknown[unknown++]=p;
                }
                if(P[I][J]==-2)danger++;
            }
        }
    }
    if(!k){
        if(unknown>0){
            for(i=0;i<unknown;i++){
                pt p=Unknown[i];
                P[p.r][p.c]=Data[p.r][p.c];
            }
        }
    }
    else{
        if(!danger){
            if(unknown>0&&unknown==k){
                for(i=0;i<unknown;i++){
                    pt p=Unknown[i];
                    P[p.r][p.c]=-2;
                }
            }
        }
        else{
            if(danger==k&&unknown>0){
                for(i=0;i<unknown;i++){
                    pt p=Unknown[i];
                    P[p.r][p.c]=Data[p.r][p.c];
                }
            }
            else if(danger+unknown==k&&unknown>0){
                for(i=0;i<unknown;i++){
                    pt p=Unknown[i];
                    P[p.r][p.c]=-2;
                }
            }
        }
    }
}

uint8_t count(int**P,uint8_t R,uint8_t C){
    uint8_t o=0;
    for(size_t i=0;i<R;i++){
        for(size_t j=0;j<C;j++){
            if(P[i][j]==-1)o++;
        }
    }
    return o;
}

int main()
{
    //Define Minesweeper Problem
    int R=10,C=10,i,j;
    int**P=(int**)calloc(R,C*sizeof(int));
    for(i=0;i<R;i++)P[i]=(int*)calloc(C,sizeof(int));
    P[0][0]=-1;P[0][1]=-1;P[0][2]=-1;P[0][3]=-1;P[0][4]=-1;
    P[0][5]=-1;P[0][6]=1;P[0][7]=0;P[0][8]=0;P[0][9]=0;

    P[1][0]=-1;P[1][1]=-1;P[1][2]=-1;P[1][3]=-1;P[1][4]=-1;    
    P[1][5]=2;P[1][6]=1;P[1][7]=0;P[1][8]=0;P[1][9]=0;

    P[2][0]=-1;P[2][1]=-1;P[2][2]=-1;P[2][3]=-1;P[2][4]=-1;
    P[2][5]=1;P[2][6]=0;P[2][7]=1;P[2][8]=1;P[2][9]=1;

    P[3][0]=-1;P[3][1]=-1;P[3][2]=2;P[3][3]=2;P[3][4]=1;
    P[3][5]=1;P[3][6]=0;P[3][7]=1;P[3][8]=-1;P[3][9]=-1;

    P[4][0]=2;P[4][1]=2;P[4][2]=1;P[4][3]=0;P[4][4]=0;
    P[4][5]=0;P[4][6]=0;P[4][7]=1;P[4][8]=-1;P[4][9]=-1;

    P[5][0]=0;P[5][1]=0;P[5][2]=0;P[5][3]=0;P[5][4]=0;
    P[5][5]=1;P[5][6]=1;P[5][7]=1;P[5][8]=-1;P[5][9]=-1;

    P[6][0]=0;P[6][1]=0;P[6][2]=0;P[6][3]=0;P[6][4]=0;
    P[6][5]=1;P[6][6]=-1;P[6][7]=-1;P[6][8]=-1;P[6][9]=-1;

    P[7][0]=0;P[7][1]=0;P[7][2]=0;P[7][3]=0;P[7][4]=0;
    P[7][5]=1;P[7][6]=2;P[7][7]=-1;P[7][8]=-1;P[7][9]=-1;

    P[8][0]=1;P[8][1]=1;P[8][2]=1;P[8][3]=0;P[8][4]=0;
    P[8][5]=0;P[8][6]=2;P[8][7]=-1;P[8][8]=-1;P[0][9]=-1;

    P[9][0]=-1;P[9][1]=-1;P[9][2]=3;P[9][3]=2;P[9][4]=1;
    P[9][5]=2;P[9][6]=2;P[9][7]=-1;P[9][8]=-1;P[9][9]=-1;
    
    uint8_t old=count(P,R,C),new;
    while(1){
        for(i=0;i<R;i++){
            for(j=0;j<C;j++){
                if(P[i][j]>=0)solve(P,i,j,R,C);
            }
        }   
        new=count(P,R,C);
        if(new==old)break;
        old=new;
    }
    //Visualization of result
    /*
    for(i=0;i<R;i++){
        for(j=0;j<C;j++)printf("%d ",P[i][j]);
        printf("\n");
    }
    */
    return 0;
}
