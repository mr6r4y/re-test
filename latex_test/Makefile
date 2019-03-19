all: hello.pdf hello.pandoc.pdf hello.docx hello.odt figures.pdf

figures.pdf: figures.tex
	pdflatex -interaction=nonstopmode $^

hello.pdf: hello.tex
	pdflatex -interaction=nonstopmode $^

hello.pandoc.pdf: hello.tex
	pandoc $^ -o $@

hello.odt: hello.tex
	pandoc $^ -o $@

hello.docx: hello.tex
	pandoc $^ -o $@

clean:
	rm -f figures.pdf hello.pdf hello.pandoc.pdf *.docx *.odt *.log *.aux

.PHONY: all clean