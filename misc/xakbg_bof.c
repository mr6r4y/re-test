#include <stdio.h>
#include <stdlib.h>

struct data {
    char a[10];
    int b;
};

void never_called_function() {
    printf("Success");
    fflush( stdout );
}

int main() {
    struct data d;
    scanf("%s", d.a);
    return 0;
}