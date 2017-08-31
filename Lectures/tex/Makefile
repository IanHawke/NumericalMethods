LECTURES = $(wildcard L*tex)
SLIDES = $(LECTURES:.tex=.pdf)

define pdflecture
	cat ~/Dropbox/LaTeXGeneral/BeamerLectureHeader.tex $(1) | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^%LECTURE%//" > yap.tex
	pdflatex yap.tex
	pdflatex yap.tex
	cp yap.pdf $(1:.tex=.pdf)
	rm yap.*
endef

define pdfhandout
	cat ~/Dropbox/LaTeXGeneral/BeamerLectureHeader.tex $(1) | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^%HANDOUT%//" > yap.tex
	pdflatex yap.tex
	pdflatex yap.tex
	cp yap.pdf $(1:.tex=_Handout.pdf)
	/bin/rm yap.*
endef

all: $(SLIDES)

%.pdf: %.tex
	echo $<
	$(call pdflecture,$<)
	$(call pdfhandout,$<)
