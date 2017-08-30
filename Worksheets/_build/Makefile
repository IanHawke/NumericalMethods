SHEETS = Worksheet1_Notebook.pdf Worksheet2_Notebook.pdf Worksheet3_Notebook.pdf Worksheet4_Notebook.pdf Worksheet5_Notebook.pdf Worksheet6_Notebook.pdf Worksheet7_Notebook.pdf
SOLUTIONS := $(SHEETS:.pdf=-Solutions.pdf)

all: sheets solutions

sheets: $(SHEETS)

solutions: $(SOLUTIONS)

%-Solutions.pdf: %-Solutions.tex %.ipynb
	echo $<
	pdflatex $<
	pdflatex $<

%-Solutions.tex: %.ipynb hidecode_selective.tplx
	jupyter nbconvert $< --execute --allow-errors --to latex --template=hidecode_selective.tplx --output $(<:.ipynb=-Solutions.tex)

%.tex: %.ipynb hidesolution_selective.tplx
	jupyter nbconvert $< --execute --allow-errors --to latex --template=hidesolution_selective.tplx

%.pdf: %.tex %.ipynb
	pdflatex $<
	pdflatex $<

clean:
	rm -f *.{out,log,aux,toc}
	rm -rf auto
	rm -f W*tex
	rm -rf W*files
	rm -rf __pycache__
