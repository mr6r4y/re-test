all: hello.pdf hello.pandoc.pdf hello.docx hello.odt

hello.pdf: hello.tex
	pdflatex $^

hello.pandoc.pdf: hello.tex
	pandoc $^ -o $@

hello.odt: hello.tex
	pandoc $^ -o $@

hello.docx: hello.tex
	pandoc $^ -o $@

clean:
	rm -f hello.pdf hello.pandoc.pdf *.docx *.odt *.log *.aux

.PHONY: all clean