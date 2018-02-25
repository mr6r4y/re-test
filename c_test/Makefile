all: test_memcmp test_stdio

test_memcmp: test_memcmp.c
	gcc -o $@ $^

test_stdio: test_stdio.c
	gcc -o $@ $^

clean:
	rm test_memcmp test_stdio


.PHONY: clean all
