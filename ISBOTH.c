#include <stdio.h>

int main(void) {
	int k;
	scanf("%d",&k);
	if(k%5==0 && k%11==0)
	{printf("BOTH");}
	else if(k%5==0 || k%11==0)
	{printf("ONE");}
	else{printf("NONE");}
	return 0;
}

