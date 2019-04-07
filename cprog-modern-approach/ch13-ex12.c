#include <ctype.h>
#include <string.h>
#include <stdio.h>


void get_extension_v1(const char *filename, char *ext)
{
	int i;
	
	i =  strlen(filename);
	while (i >= 0) {
		if (filename[i] == '.') {
			strncpy(ext, filename + i + 1, 10);
			return;
		}
		i--;
	}

	*ext = '\0';
}


char * get_extension_v2(const char *filename)
{
	int len, i;
	char *ext;
	
	i = len =  strlen(filename);
	ext = filename + len;

	while (i >= 0) {
		if (*ext == '.') {
			ext++;
			return ext;
		}
		ext--; 
		i--;
	}

	return filename + len;
}


int read_line(char str[], int n)
{
 	int ch, i = 0;

 	while (isspace(ch = getchar()));
 	while (ch != '\n' && ch != EOF) {
 		if (i < n) str[i++] = ch;
 		ch = getchar();
  	}
	str[i] = '\0';
	return i;
}


int main()
{	
	char e[100] = {};

	// get_extension("memo.txt", e);
	// printf("%s\n", e);

	// get_extension("memo", e);
	// printf("%s\n", e);

	#define N 100
	char buf[N] = {};

	while(1) {
		printf("Enter filename: ");
		read_line(buf, N - 1);
		if(*buf == '\0') 
			break;
		// get_extension_v1(buf, e);
		printf("%s\n", get_extension_v2(buf));
	}
}