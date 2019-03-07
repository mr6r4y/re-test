#include <stdio.h>

int main()
{
	int i = 0, j = 0;
	char s[100] = {0};
	printf("Enter value: ");
	scanf("%d%s%d", &i, s, &j);

	printf("i=%d\n", i);
	printf("s=%s\n", s);
	printf("j=%d\n", j);
}