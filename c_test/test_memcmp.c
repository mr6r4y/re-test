#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[], char* envp[])
{
	char buf[4] = {'b', 'b', 'b', 'b'};
	int f;

	f = open("./test_memcmp.txt", O_RDONLY);
	read(f, buf, 4);

	int a1 = memcmp(buf, "aaab", 4);
	int a2 = memcmp(buf, "baab", 4);
	int a3 = memcmp(buf, "aaaa", 4);
	int a4 = memcmp(buf, "rrrr", 4);
	int a5 = memcmp(buf, "dddd", 4);
	int a6 = memcmp(buf, "    ", 4);

	printf("memcmp('aaaa', 'aaab'): %x %d\n", a1, a1);
	printf("memcmp('aaaa', 'baab'): %x %d\n", a2, a2);
	printf("memcmp('aaaa', 'aaaa'): %x %d\n", a3, a3);
	printf("memcmp('aaaa', 'rrrr'): %x %d\n", a4, a4);
	printf("memcmp('aaaa', 'dddd'): %x %d\n", a5, a5);
	printf("memcmp('aaaa', '    '): %x %d\n", a6, a6);
}