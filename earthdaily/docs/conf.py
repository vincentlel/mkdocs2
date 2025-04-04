# Configuration file for the Sphinx documentation builder.
#

# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

# import re
import os
import sys
import re

from sphinx_gallery.sorting import ExampleTitleSortKey
import os
os.environ['PYDEVD_DISABLE_FILE_VALIDATION'] = "1"
project = "earthdaily"
copyright = "2024, EarthDailyAgro"
author = "Geosys/EarthDailyAgro"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration


extensions = [
    'sphinx.ext.autodoc',  # For automatic API documentation
    'sphinx.ext.napoleon',  # For Google/NumPy style docstrings
    'sphinx.ext.viewcode',  # To add links to source code
    'sphinx_autodoc_typehints',  # For better type hint support
    "sphinx.ext.autosummary",
    "sphinx.ext.viewcode",
    "sphinx_gallery.gen_gallery",
    "sphinx_copybutton",
    "sphinx_automodapi.automodapi",
    "sphinx_automodapi.smart_resolver",# for a page per function
    "myst_parser",
]
#
automodapi_writereprocessed = True
automodsumm_inherited_members = True
numpydoc_show_class_members = False
sys.path.insert(0, os.path.abspath("."))
sys.path.insert(0, os.path.abspath(".."))


__version__ = re.search(
    r'__version__\s*=\s*[\'"]([^\'"]*)[\'"]',  # It excludes inline comment too
    open("../earthdaily/__init__.py").read(),
).group(1)

source_suffix = [".rst"]

# The master toctree document.

version = __version__
# The full version, including alpha/beta/rc tags.
release = __version__

sphinx_gallery_conf = {
    "backreferences_dir": os.path.join("_modules", "backreferences"),
    "doc_module": "earthdaily",
    # path to your examples scripts
    "examples_dirs": f"..{os.path.sep}examples",
    "filename_pattern": "",
    # path where to save gallery generated examples
    "ignore_pattern": "__",
    "gallery_dirs": ["_auto_examples"],
    # avoid generating too many cross links
    "inspect_global_variables": False,
    "remove_config_comments": True,
    "plot_gallery": "True",
}
pygments_style = "sphinx"
nbsphinx_allow_errors = True
autosummary_generate = True
# numpydoc_show_class_members=False
imported_members = True

autoclass_content = "both"

# Add any paths that contain templates here, relative to this directory.
templates_path = ["templates"]

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"

source_suffix = [".rst", ".md"]

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
pdf_documents = [
    ("index", "earthdaily_documentation", "earthdaily doc", "EarthDaily Agro"),
]


# -- Extension configuration -------------------------------------------------

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False