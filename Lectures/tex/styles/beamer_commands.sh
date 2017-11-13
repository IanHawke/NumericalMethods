# For inclusion in a .bashrc file

export TEXMFHOME=$HOME/Dropbox/LaTeXGeneral/texmf

#Compile beamer lectures
pdflecture()
{
cat ~/Dropbox/LaTeXGeneral/BeamerLectureHeader.tex ${*%.*}.tex | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^%LECTURE%//" > yap.tex
pdflatex yap.tex
pdflatex yap.tex
cp yap.pdf ${*%.*}.pdf
/bin/rm yap.*
}

pdfhandout()
{
cat ~/Dropbox/LaTeXGeneral/BeamerLectureHeader.tex ${*%.*}.tex | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^%HANDOUT%//" > yap.tex
pdflatex yap.tex
pdflatex yap.tex
cp yap.pdf ${*%.*}_Handout.pdf
/bin/rm yap.*
}

pdfsmallhandout()
{
cat ~/Dropbox/LaTeXGeneral/BeamerLectureHeader.tex ${*%.*}.tex | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^%SMALLHANDOUT%//" > yap.tex
pdflatex yap.tex
pdflatex yap.tex
cp yap.pdf ${*%.*}_SmallHandout.pdf
/bin/rm yap.*
}

pdftinyhandout()
{
cat ~/Dropbox/LaTeXGeneral/BeamerLectureHeader.tex ${*%.*}.tex | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^%TINYHANDOUT%//" > yap.tex
pdflatex yap.tex
pdflatex yap.tex
cp yap.pdf ${*%.*}_TinyHandout.pdf
/bin/rm yap.*
}

pdfnotes()
{
cat ~/Dropbox/LaTeXGeneral/BeamerLectureHeader.tex ${*%.*}.tex | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^%LECTURE%//" > yap.tex
pdflatex yap.tex
/bin/rm yap.tex
cat ~/Dropbox/LaTeXGeneral/BeamerLectureHeader.tex ${*%.*}.tex | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^%NOTES%//" > yap.tex
pdflatex yap.tex
pdflatex yap.tex
cp yap.pdf ${*%.*}_Notes.pdf
/bin/rm yap.*
}

pdfall()
{
pdflecture $*
pdfhandout $*
#pdfsmallhandout $*
#pdftinyhandout $*
#pdfnotes $*
}

# To compile problem sheets or coursework without solutions
pdfprobs()
{
cat ~/Dropbox/LaTeXGeneral/ProblemsHeader.tex ${*%.*}.tex | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^[\]usepackage/%usepackage/" | sed -e "s/^%PROBLEMS%//" > yap.tex
pdflatex yap.tex
pdflatex yap.tex
cp yap.pdf ${*%.*}.pdf
/bin/rm yap.*
}

# To compile problem sheets or coursework with solutions
pdfsolns()
{
cat ~/Dropbox/LaTeXGeneral/ProblemsHeader.tex ${*%.*}.tex | sed -e "s/^[\]documentclass/%documentclass/" | sed -e "s/^[\]usepackage/%usepackage/" | sed -e "s/^%SOLUTIONS%//" > yap.tex
pdflatex yap.tex
pdflatex yap.tex
cp yap.pdf ${*%.*}_Solutions.pdf
/bin/rm yap.*
}

# To compile both problem sheets and solutions
pdfprobsolns()
{
pdfprobs $*
pdfsolns $*
}
