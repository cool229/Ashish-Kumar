/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#include<stdlib.h>
#include<string.h>
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
/*int isEmpty(){
    if(top==-1)
        return 0;
    else {
        return 1;
    }
}*/
void check(char a[],int n){
    int i=0,count=0;
    while(i!=n){
          if(a[i]=='[' || a[i] == '(' || a[i] =='{'){
          //  printf("where are you \n");
            char val = a[i];
            push(val);
            count++;
          // printf("%d %d %c\n",top,count,stack[top]);
           
        }
        
        
        
        if(a[i]==']' || a[i] == ')' || a[i] =='}'){
             // printf("%c \n",a[i]);
            if(top==-1){
                printf("The parentheses are not in proper order\n");
                return;
           }
           char val = pop(); 
           count++;
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
                if(val == '{' || val =='['){
                printf("The parentheses are not in proper order\n");
                return;
           }
           }
           
        }
    i++; 
    }
    if(top!=-1){
        printf("The parentheses are not in proper order\n");
        //printf("here i am %d",top);
                return;
    }
    printf("The parentheses are in perfect oreder\n ");
}


int main()
{
    //char a[8]= {'[','{','(',')','(',')','}',']'};
  // printf("Enter \n");
   char a[20];
   scanf("%s",a);
   int l = strlen(a);
     check(a,l);

    return 0;
}










