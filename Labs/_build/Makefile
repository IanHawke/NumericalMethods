
%.tex: %.ipynb hidecode_selective.tplx
	jupyter nbconvert --execute --allow-errors --to latex --template=hidesolution_selective.tplx $<

%.pdf: %.tex %.ipynb
	pdflatex $<
	pdflatex $<

Essential-Exercises-Solutions.pdf: Essential-Exercises.ipynb
	jupyter nbconvert Essential-Exercises.ipynb --execute --allow-errors --to latex --template=hidecode_selective.tplx --output Essential-Exercises-Solutions.tex
	pdflatex Essential-Exercises-Solutions
	pdflatex Essential-Exercises-Solutions

clean:
	rm -f *.{out,log,aux,toc}
	rm -rf auto
	rm -f [01PE]*tex
	rm -rf [01PE]*files
	rm -rf __pycache__
