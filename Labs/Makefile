labs: 00-Installing-On-Own-Machine.ipynb 01-Initial-Labs.ipynb Python-Essentials.ipynb
	cp -r figs _build/
	cp *.tplx _build/
	cp *.py _build/
	cp *.ipynb _build/
	make -C _build 00-Installing-On-Own-Machine.pdf
	make -C _build 01-Initial-Labs.pdf
	make -C _build Python-Essentials.pdf
	make -C _build Essential-Exercises.pdf
	make -C _build Essential-Exercises-Solutions.pdf
	make -C _build clean

clean:
	rm -f *.{out,log,aux,toc}
	rm -rf auto
	rm -f [01PE]*tex
	rm -rf [01PE]*files
	rm -rf __pycache__
