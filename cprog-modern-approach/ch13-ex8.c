#include <ctype.h>
#include <string.h>
#include <stdio.h>


int main()
{
	char str[100] = {};

	strcpy(str, "tire-bouchon");
	strcpy(&str[4], "d-or-wi");
	strcat(str, "red?");

	printf("%s\n", str);
}