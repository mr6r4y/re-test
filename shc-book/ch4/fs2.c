#include <stdio.h>


void fs(char *s)
{
	printf(s);
}


void never_called(void)
{
	printf("You never called me!\n");
}


int main(int argc, char **argv)
{
	fs(argv[1]);
}