
%.tex: %.ipynb hidecode_selective.tplx
	jupyter nbconvert --execute --allow-errors --to latex --template=hidecode_selective.tplx $<

%.pdf: %.tex %.ipynb
	pdflatex $<
	pdflatex $<

clean:
	rm -f *.{out,log,aux,toc}
	rm -rf auto
	rm -f W*tex
	rm -rf W*files
	rm -rf __pycache__
