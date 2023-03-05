import sys
sys.path.insert(0, '/path/to/your/module')

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.napoleon',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    'sphinxcontrib.napoleon',
]

autodoc_member_order = 'bysource'
napoleon_google_docstring = True
napoleon_numpy_docstring = False

