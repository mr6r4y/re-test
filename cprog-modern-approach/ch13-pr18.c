#include <ctype.h>
#include <string.h>

#include <stdio.h>
#include <stdlib.h>


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


#define ERROR_DATE_CONVERT -1
#define SUCCESS_DATE_CONVERT 1


int date_convert(const char *date_to_convert, char *converted_date)
{
	int dd = 0, mm = 0, yyyy = 0;
	sscanf(date_to_convert, "%02d/%02d/%d", &mm, &dd, &yyyy);

	if (!dd || !mm || !yyyy)
		return ERROR_DATE_CONVERT;

	if (mm > 12 || mm < 1)
		return ERROR_DATE_CONVERT;

	char *month;
	switch (mm) {
		case 1:
		month = "Jan";
		break;

		case 2:
		month = "Feb";
		break;

		case 3:
		month = "Mar";
		break;

		case 4:
		month = "Apr";
		break;

		case 5:
		month = "May";
		break;

		case 6:
		month = "Jun";
		break;

		case 7:
		month = "Jul";
		break;

		case 8:
		month = "Aug";
		break;

		case 9:
		month = "Sep";
		break;

		case 10:
		month = "Oct";
		break;

		case 11:
		month = "Nov";
		break;

		case 12:
		month = "Dec";
		break;
	}

	sprintf(converted_date, "%s %d, %d", month, dd, yyyy);
	return SUCCESS_DATE_CONVERT;
}


int main()
{
	#define N 100
	char buf[N];
	char date[N];
	int convert_res;

	while(1) {
		memset(buf, 0, N);
		memset(date, 0, N);
		printf("Enter a date (mm/dd/yyyy): ");
		read_line(buf, N - 1);
		if(*buf == '\0')
			break;
		else {
			convert_res = date_convert(buf, date);

			if (convert_res == SUCCESS_DATE_CONVERT)
				printf("You entered the date %s\n\n", date);
			else
				printf("You entered an invalid date!\n");
		}
	}
}