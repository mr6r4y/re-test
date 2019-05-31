#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <stdio.h>


int main(int argc, char * argv[])
{
    int r;
    struct stat * statbuf;
    statbuf = malloc(sizeof(struct stat));

    if(statbuf != NULL) {
        r = fstat(1, statbuf);
        printf("Stat result: %d\n", r);
    } else 
        printf("Error: Could not malloc statbuf");
    
    while (1)
    {
        sleep (1);
    }
}
