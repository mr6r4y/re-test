#include <fcntl.h>
#include <stdio.h>
#include <string.h>
#include <unistd.h>

int main(int argc, char* argv[], char* envp[])
{
	printf("stdin: %x %d\n", stdin->_fileno, stdin->_fileno);
	printf("stdout: %x %d\n", stdout->_fileno, stdout->_fileno);
	printf("stderr: %x %d\n", stderr->_fileno, stderr->_fileno);
	
}