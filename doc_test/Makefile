all: hello.pdf hello.pandoc.pdf

hello.pdf: hello.tex
	pdflatex $^

hello.pandoc.pdf: hello.tex
	pandoc $^ -o $@

clean:
	rm -f hello.pdf hello.pandoc.pdf *.log *.aux

.PHONY: all clean