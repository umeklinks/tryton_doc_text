# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))
# import sphinx_rtd_theme
import sys

sys.setrecursionlimit(1000)


# -- Project information -----------------------------------------------------

project = 'Tryton Test'
copyright = '2020, Ume Abraham Kalu (Test Documentation)'
author = 'Ume Abraham Kalu'

# The full version, including alpha/beta/rc tags
release = '0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_copybutton'
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
import sphinx_rtd_theme                                                      
html_theme = 'sphinx_rtd_theme'                                              
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
#
# html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
# on_rtd = os.environ.get('READTHEDOCS', None) == 'True'

# if not on_rtd:  # only import and set the theme if we're building docs locally   
    # import sphinx_rtd_theme                                                      
    # html_theme = 'sphinx_rtd_theme'                                              
    # html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]                   
    # Override default css to get a larger width for local build                 
    # def setup(app):                                                              
    #     app.add_css_file('custom.css'),
    #     app.add_javascript("custom.js"),                                       
    #     app.add_javascript("https://cdn.jsdelivr.net/npm/clipboard@1/dist/clipboard.min.js")                                
# else:                                                                            
    # Override default css to get a larger width for ReadTheDoc build            
    # html_context = {                                                             
    #     'add_css_file': [                                                           
    #         'https://media.readthedocs.org/css/sphinx_rtd_theme.css',            
    #         'https://media.readthedocs.org/css/readthedocs-doc-embed.css',       
    #         '_static/custom.css',
    #     ],                                                                       
    # }

# from sphinx.writers.html import HTMLTranslator
# class PatchedHTMLTranslator(HTMLTranslator):
#     def visit_reference(self, node):
#         if node.get('newtab') or not (node.get('target') or node.get('internal') or 'refuri' not in node):
#             node['target'] = '_blank'
#         super().visit_reference(node)

# def setup(app):
#     app.set_translator('html', PatchedHTMLTranslator)
#
