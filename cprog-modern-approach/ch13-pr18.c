#include <ctype.h>
#include <string.h>
#include <stdio.h>


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


void date_convert(const char *date_to_convert, char *converted_date)
{
	strcpy(converted_date, date_to_convert);
}


int main()
{
	#define N 100
	char buf[N];
	char date[N];

	while(1) {
		printf("Enter a date (mm/dd/yyyy): ");
		read_line(buf, N - 1);
		if(*buf == '\0') 
			break;
		else
			date_convert(buf, date);
		printf("You entered the date %s\n\n", date);
	}
}