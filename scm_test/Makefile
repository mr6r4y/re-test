all: hello

hello: hello.scm
	csc -output-file $@ $^

clean:
	rm -f hello

.PHONY: all clean