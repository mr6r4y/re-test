#include <stdio.h>


int main()
{
	int j[2]={1, 2};;
	int a, *i;

	i = (int *)j;
	a = *i++;

	printf("j[0] = %d\n", j[0]);
	printf("j[1] = %d\n", j[1]);
	printf("a = %d\n", a);
	printf("*i = %d\n", *i);
}