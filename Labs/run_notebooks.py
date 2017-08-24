from runipy.notebook_runner import NotebookRunner
from IPython.nbformat.current import read

files = ["00-Installing-On-Own-Machine.ipynb",
         "01-Initial-Labs.ipynb",
         "Python-Essentials.ipynb"]

for file in files:
    notebook = read(open(file), 'json')
    r = NotebookRunner(notebook)
    r.run_notebook(skip_exceptions=True)
    from IPython.nbformat.current import write
    write(r.nb, open("_build/"+file, 'w'), 'json')
