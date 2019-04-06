#include <stdio.h>

int strcmp_v1(char *s, char *t)
{
	int i;

	for (i=0; s[i]==t[i]; i++)
		if (s[i]=='\0')
			return 0;

	return s[i] - t[i];
}


int strcmp_v2(char *s, char *t)
{
	while(*s == *t) {
		if(*s == '\0') return 0;
		s++, t++;
	}

	return *s - *t;
}


int main()
{
	printf("strcmp_v1('aadfa','aadfa')=%d\n", strcmp_v1("aadfa","aadfa"));
	printf("strcmp_v1('ad3adfa','aredfa')=%d\n", strcmp_v1("ad3adfa","aredfa"));

	printf("strcmp_v2('aadfa','aadfa')=%d\n", strcmp_v2("aadfa","aadfa"));
	printf("strcmp_v2('ad3adfa','aredfa')=%d\n", strcmp_v2("ad3adfa","aredfa"));
}