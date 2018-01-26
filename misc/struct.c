#include <stdio.h>

struct A {
	int a;
	short int b;
	char c;
};

struct A G_A = {
	3,
	4,
	'B'
};

int main()
{
	
	struct A my_a, my_aa;

	my_a.a = 1;
	my_a.b = 2;
	my_a.c = 'A';

	my_aa.a = G_A.a;
	my_aa.b = G_A.b;
	my_aa.c = G_A.c;

};
