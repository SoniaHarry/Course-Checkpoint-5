# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'DocCheckPoint5'
copyright = '2024, Sonia D'
author = 'Sonia D'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc',
        'sphinx.ext.intersphinx',
        'sphinx.ext.todo',
        'sphinx.ext.mathjax',
        'sphinx.ext.napoleon',
        'sphinx.ext.autosummary', # solamente si se la quiere usar
        'sphinx.ext.viewcode']

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'#'alabaster'
html_static_path = ['_static']
