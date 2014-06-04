import numpy as np
import matplotlib.pyplot as plt

def highlight_source(module, function):
    """For use inside an IPython notebook: given a module and a function, print the source code."""

    from inspect import getmembers, isfunction, getsource
    from pygments import highlight
    from pygments.lexers import PythonLexer
    from pygments.formatters import HtmlFormatter
    from IPython.core.display import HTML

    internal_module = __import__(module)

    internal_functions = dict(getmembers(internal_module, isfunction))

    return HTML(highlight(getsource(internal_functions[function]), PythonLexer(), HtmlFormatter(full=True)))

def highlight_source_octave(filename):
    """For use inside an IPython notebook: given a filename, print the source code. Octave version (works with Matlab code)."""

    from pygments import highlight
    from pygments.lexers import OctaveLexer
    from pygments.formatters import HtmlFormatter
    from IPython.core.display import HTML

    with open (filename, "r") as myfile:
        data = myfile.read()

    return HTML(highlight(data, OctaveLexer(), HtmlFormatter(full=True)))

def highlight_source_matlab(filename):
    """For use inside an IPython notebook: given a filename, print the source code. Matlab version (works with Octave code)."""

    from pygments import highlight
    from pygments.lexers import MatlabLexer
    from pygments.formatters import HtmlFormatter
    from IPython.core.display import HTML

    with open (filename, "r") as myfile:
        data = myfile.read()

    return HTML(highlight(data, MatlabLexer(), HtmlFormatter(full=True)))
