/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include<stdlib.h>
#define max 30
int stack[max];
int top =-1;
void push(int ch){
    if(top ==max){
        printf("Overflow\n");
        return;
    }
    stack[++top] = ch;
    
}
int pop(){
    int ch ;
    if(top ==-1)
    {
        printf("Underflow\n");
        return -1;
    }
    ch = stack[top--];
    return ch;
}

int main()
{
   long long int x;
   scanf("%li",&x);
  // int p = printf("%li",x);
  // printf("\n%d\n",p);
   int a[30];
   int i=0,r=0;
   while(x){
       r = x%2;
       a[i++]=r;
       push(r);
       x = x/2;
   }
   for(int j =0;j<i;j++){
       int q = pop();
       if(q==-1){
           printf("\nEnd");
       }
       else
       printf("%d",q);
   }
   

    return 0;
}
