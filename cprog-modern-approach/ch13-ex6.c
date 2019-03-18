#include <ctype.h>
#include <string.h>
#include <stdio.h>

int read_line(char str[], int n)
{
  int ch, i = 0;

  while (isspace(ch = getchar()))
    ;
  while (ch != '\n' && ch != EOF) {
    if (i < n)
      str[i++] = ch;
    ch = getchar();
  }
  str[i] = '\0';
  return i;
}


int censor(char str[])
{
	char *pattern = "foo";
	int ptrn_len = strlen(pattern);
	int str_len = strlen(str);
	char *t_str = str;
	int c = 0;

	while(*t_str) {
		if(strncmp(t_str, pattern, ptrn_len) == 0) strncpy(t_str, "xxx", ptrn_len), c++;
		t_str++;
	}

	return c;
}


int main()
{
	#define N 100
	char buf[N] = {};

	while(1) {
		printf("Enter string and `foo` will be replaced with `xxx`: ");
		read_line(buf, N - 1);
		if(*buf == '\0') 
			break;
		censor(buf);
		printf("Result: %s\n\n", buf);
	}
}