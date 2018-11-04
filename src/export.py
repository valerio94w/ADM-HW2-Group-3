# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 19:08:40 2018

@author: mikyl
"""

from IPython.nbformat import v3, v4

with open("CRQ1.py") as fpin:
    text = fpin.read()

nbook = v3.reads_py(text)
nbook = v4.upgrade(nbook)  # Upgrade v3 to v4

jsonform = v4.writes(nbook) + "\n"
with open("output-file.ipynb", "w") as fpout:
    fpout.write(jsonform)