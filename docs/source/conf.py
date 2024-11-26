# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import os
import sys
from datetime import datetime

sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------

project = "AequilibraE for QGIS"
copyright = f"{str(datetime.now().date())}, AequilibraE developers"
author = "Pedro Camargo"

# The short X.Y.Z version

a = open("../../qaequilibrae/metadata.txt", "r")
for line in a.readlines():
    if "version" in line.rstrip():
        version = line.rstrip()[8:]

# The full version, including alpha/beta/rc tags
release = version

# -- General configuration ---------------------------------------------------

# Sphinx extension module names
extensions = ["sphinx_panels", "sphinx_subfigure", "sphinx_design"]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
source_suffix = ".rst"

# The master toctree document.
master_doc = "index"

# The language for content autogenerated by Sphinx.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = "pydata_sphinx_theme"

# Theme options are theme-specific and customize the look and feel of a theme
# further. For a list of options available for each theme, see the
# documentation.
html_theme_options = {
    "navbar_center": ["navigation_header"],
    "navbar_start": ["navbar-logo"],
    "navbar_end": ["theme-switcher", "navbar-icon-links"],
    "navbar_persistent":["search-button"],
    "navbar_align": "left",
    "github_url": "https://github.com/AequilibraE/qaequilibrae",
    "logo": {
        "text": "AequilibraE",
        "image_light": "_static/large_icon.png",
        "image_dark": "_static/large_icon.png",
        "link": "https://www.aequilibrae.com/dev/home.html",
    },
}

# The name for this set of Sphinx documents. If None, it defaults to
html_title = f"AequilibraE for QGIS"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

html_css_files = ["custom.css"]

# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = "AequilibraEdoc"

# -- Options for LaTeX output ------------------------------------------------
latex_documents = [("_latex/index", "qaequilibrae.tex", "AequilibraE for QGIS", author, "manual")]

latex_appendices = [
    "development/softwaredevelopment",
    "development/i18n",
    "development/support",
    "development/citation",
]

# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "aequilibrae", "AequilibraE for QGIS", [author], 1)]

# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author, dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "AequilibraE",
        "AequilibraE for QGIS",
        author,
        "AequilibraE",
        "A QGIS plugin for transportation modeling",
        "Miscellaneous",
    )
]

# -- Options for intersphinx extension ---------------------------------------
add_module_names = False
