/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

void change(int a[],int n)
{
    for(int i=0;i<n;i++)
    {
        if(a[i]==0)
        {
            for(int j=i;j<n-1;j++)
            {
                a[j]=a[j+1];
            }
           a[n-1]=0;
        }
    }
}
int main()
{   int n;
    scanf("%d",&n);
    int a[n];
    for(int i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    change(a,n);
    for(int i=0;i<n;i++)
    {
        printf("%d",a[i]);
    }
    return 0;
}

