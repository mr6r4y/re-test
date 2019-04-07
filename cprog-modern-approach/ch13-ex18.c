#include <ctype.h>
#include <string.h>
#include <stdio.h>


void remove_filename(char *url)
{
	int len;
	len = strlen(url);
	
	for (char *u = url + len; len >= 0; len--, u--)
		if (*u == '/') {
			*u = '\0';
			break;
		}
}


int main(void)
{
	char u1[100] = "http://abv.bg/index.html";
	remove_filename(u1);
	printf("%s\n", u1);


	char u2[100] = "https://google.com/path1/path2/index.php?q=1";
	remove_filename(u2);
	printf("%s\n", u2);

}