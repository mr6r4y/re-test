all: test_memcmp test_stdio test_chararr

test_memcmp: test_memcmp.c
	gcc -o $@ $^

test_stdio: test_stdio.c
	gcc -o $@ $^

test_chararr: test_chararr.c
	gcc -o $@ $^ -no-pie

clean:
	rm test_memcmp test_stdio test_chararr


.PHONY: clean all
