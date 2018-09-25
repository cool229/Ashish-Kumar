/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <stdio.h>

int main() {
	//code
	int n,m=0,p,l,a,b,c;
	//scanf("%d",&n);
	for(int i =1;i<=3;i++){
	        m = 0,l=1;
	        while(l<= i){
	            a=2*l;
	            b=(l+1)*(l+1);
	            c =(l*l+4);
	        m +=((2*l)+(l+1)*(l+1))-(l*l+4) ;
	        l++;
	       // printf("%d",m);
	       }
             printf("%d\n",m);
	    }
	return 0;
}
