#!/usr/bin/env python
# coding: utf-8


import argparse
import nbformat as nbf

def parse_cmdline():
    parser = argparse.ArgumentParser(description='Creating an IPython Notebook programatically')
    
    parser.add_argument('filename',
                        type=str,
                        help='name of the file',
                        )
    args = parser.parse_args()
    return args


def convert_to_notebook(filename):
    """ Convert a python file to notebook """
    # # 
    # 
    # The `nbformat` package gives us the necessary tools to create a new Jupyter Notebook without having to know the specifics of the file format, JSON schema, etc.

    # In[1]:


    # Our simple text notebook will only have a text cell and a code cell:

    # In[3]:


    #text = """# My first automatic Jupyter Notebook
    #This is an auto-generated notebook."""

    #code = """%pylab inline
    #hist(normal(size=2000), bins=50);"""



    # Now we create a new notebook object, that we can then populate with cells, metadata, etc:

    # In[2]:


    nb = nbf.v4.new_notebook()

    text = 'Automatically generated from {}'.format(filename)

    code = open(filename).read()

    nb['cells'] = [nbf.v4.new_markdown_cell(text),
                   nbf.v4.new_code_cell(code) ]

    notebook_filename = '{}.ipynb'.format(filename.split('.')[0])
    nbf.write(nb, notebook_filename)


if __name__ == '__main__':
    args = parse_cmdline()
    convert_to_notebook(args.filename)
