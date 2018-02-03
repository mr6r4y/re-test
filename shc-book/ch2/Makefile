all: overflow.x86 overflow.x64 overflow.x86.no overflow.x64.no victim.x86 victim.x64 victim.x86.no victim.x64.no find_start

overflow.x86:
	gcc -m32 -o overflow.x86 overflow.c

overflow.x64:
	gcc -o overflow.x64 overflow.c

overflow.x86.no:
	gcc -m32 -fno-stack-protector -mpreferred-stack-boundary=2 -o overflow.x86.no overflow.c
	execstack -s overflow.x86.no

overflow.x64.no:
	gcc -fno-stack-protector -o overflow.x64.no overflow.c
	execstack -s overflow.x64.no

victim.x86:
	gcc -m32 -o victim.x86 victim.c

victim.x64:
	gcc -o victim.x64 victim.c

victim.x86.no:
	gcc -m32 -fno-stack-protector -mpreferred-stack-boundary=2 -o victim.x86.no victim.c

victim.x64.no:
	gcc -fno-stack-protector -o victim.x64.no victim.c

find_start:
	gcc -o find_start find_start.c

clean:
	rm overflow.x86 overflow.x64 overflow.x86.no overflow.x64.no victim.x86 victim.x64 victim.x86.no victim.x64.no find_start


.PHONY: clean all