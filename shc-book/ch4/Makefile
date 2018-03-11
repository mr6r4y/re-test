all: fs1 fs2 fs3 test_printf_1

fs1:
	gcc -o fs1 fs1.c

fs2:
	gcc -O0 -o fs2 fs2.c

fs3:
	gcc -O0 -o fs3 fs3.c

test_printf_1:
	gcc -o test_printf_1 test_printf_1.c

clean:
	rm fs1 fs2 fs3 test_printf_1


.PHONY: clean all