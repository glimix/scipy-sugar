try:
    import scipy_sugar
    version = scipy_sugar.__version__
except ImportError:
    version = 'unknown'

extensions = [
    'sphinx.ext.autodoc', 'sphinx.ext.doctest', 'sphinx.ext.intersphinx',
    'sphinx.ext.viewcode'
]
napoleon_google_docstring = True
templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'scipy-sugar'
copyright = '2017, Danilo Horta'
author = 'Danilo Horta'
release = version
language = None
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
pygments_style = 'sphinx'
todo_include_todos = False
html_theme = 'default'
html_static_path = ['_static']
htmlhelp_basename = 'scipy-sugardoc'
latex_elements = {}
latex_documents = [
    (master_doc, 'scipy-sugar.tex', 'scipy-sugar Documentation',
     'Danilo Horta', 'manual'),
]
man_pages = [(master_doc, 'scipy-sugar', 'scipy-sugar Documentation', [author],
              1)]
texinfo_documents = [
    (master_doc, 'scipy-sugar', 'scipy-sugar Documentation', author,
     'scipy-sugar', 'One line description of project.', 'Miscellaneous'),
]
intersphinx_mapping = {'https://docs.python.org/': None}
