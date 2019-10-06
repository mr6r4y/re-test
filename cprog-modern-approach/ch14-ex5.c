#include <alloca.h>
#include <string.h>
#include <stdio.h>


#define TOUPPER(c) ('a' <= (c) && (c) <= 'z' ? (c) - 'a' + 'A' : (c))


int main()
{
    char *s = alloca(10);
    int i = 0;

    strcpy(s, "abcd");
    putchar(TOUPPER(s[++i]));

    i = 0;
    strcpy(s, "0123");
    putchar(TOUPPER(s[++i]));

    printf("\n");
}