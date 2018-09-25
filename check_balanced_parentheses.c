/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include<stdlib.h>
#define max 20

char stack[max];
int top =-1;
void push(char ch){
    if(top ==max){
        printf("Overflow\n");
        return;
    }
    stack[++top] = ch;
    
}
char pop(){
    char ch ;
    if(top ==-1)
    {
        printf("Underflow\n");
        return 'a';
    }
    ch = stack[top--];
    return ch;
}
void check(char a[],int n){
    int i=0;
    while(i!=n){
          if(a[i]=='[' || a[i] == '(' || a[i] =='{'){
          //  printf("where are you \n");
            char val = a[i];
            push(val);
           // printf("%d ",top);
        }
        
        
        
        if(a[i]==']' || a[i] == ')' || a[i] =='}'){
           char val = pop(); 
          // printf("hey i am present here with %c and %c\n",a[i],val);
           if(val =='a')
           {
               printf("The parentheses are not in proper order\n");
               return;
           }
           else if(a[i] ==']'){
              if(val == '{' || val =='('){
                printf("The parentheses are not in proper order\n");
                return;
           }
           }
            else if(a[i] =='}'){ 
                if(val == '[' || val =='('){
                printf("The parentheses are not in proper order\n");
                return;
           }
           }
           else if(a[i] ==')'){ 
                if(val == '{' || val ==']'){
                printf("The parentheses are not in proper order\n");
                return;
           }
           }
           
        }
    i++; 
    }
    printf("The parentheses are in perfect oreder\n ");
}


int main()
{
    char a[8]= {'[','{','(',')','(',')','}',']'};
   
     check(a,8);

    return 0;
}







