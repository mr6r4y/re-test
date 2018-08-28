all: hello.arm

hello.arm: hello.go
	GOARCH=arm go build -o $@ $^

clean:
	rm -f hello.arm

.PHONY: all clean