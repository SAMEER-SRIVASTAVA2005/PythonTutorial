# Introduction to Python Parser. In this article, parsing is defined as the processing of a piece of Python program and converting these codes into machine language

# So “parsing” or “parsed” means to make something understandable. 


# Docstrings in python------Python docstrings are the string literals that appear RIGHT AFTER the definition of a function (or right above the function body), method, class, or module.(can be considered as a description)   --written inside '''  '''    i.e. three single inverted commas

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) 
print(type(square))
#docstrings are not ignored like comments 
# docstring change krke program k output change ho skte hai but comment change krke program k output change nhi hote

def square(n):
    print(n)
    '''Takes in a number n, returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__) 
# is baaar '''takes in...........of n''' ye docstring print nhi hogi kyuki docstring none ho gyi hai(docstring should be written just right after def. of func. aur yaha pr just after print(n) hai and that gives none)

# another ex-
def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    -------- 
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
print(add(57,90))
print(add.__doc__)



# PEP 8------ is a document that provides guidelines and best practices on how to write Python code. It was written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan. The primary focus of PEP 8 is to improve the readability and consistency of Python code.

# PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes new features proposed for Python and documents aspects of Python, like design and style, for the community.

# The Zen of Python
# Long time Pythoneer Tim Peters succinctly channels the BDFL’s guiding principles for Python’s design into 20 aphorisms, only 19 of which have been written down.

# open terminal or powershell then write "python" and then "import this"

# this is an easter egg in python 
# The Zen of Python, by Tim Peters

# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.     
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.     
# Errors should never pass silently.      
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!








