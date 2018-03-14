all: fs1 fs2_wr fs3_wr fs2 fs3 test_printf_1

fs1:
	gcc -o fs1 fs1.c

fs2_wr:
	gcc --static -g -Wl,--omagic -o fs2_wr fs2.c

fs3_wr:
	gcc --static -g -Wl,--omagic -o fs3_wr fs3.c

fs2:
	gcc -o fs2 fs2.c

fs3:
	gcc -o fs3 fs3.c

test_printf_1:
	gcc -o test_printf_1 test_printf_1.c

clean:
	rm fs1 fs2_wr fs3_wr fs2 fs3 test_printf_1


.PHONY: clean all