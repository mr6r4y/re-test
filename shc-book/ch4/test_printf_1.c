#include <stdio.h>


int main(int argc, char const *argv[])
{
	int i = 0;

	printf("%2$*1$d\n", 10, 7);
	printf("%*d\n", 10, 7);
	printf("aaaa%015x%n\n", i, &i);
	printf("%d\n", i);

	return 0;
}