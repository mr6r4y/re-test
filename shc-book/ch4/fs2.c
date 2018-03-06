#include <stdio.h>


void fs(char *s)
{
	printf(s);
}


int main(int argc, char **argv)
{
	fs(argv[1]);
}