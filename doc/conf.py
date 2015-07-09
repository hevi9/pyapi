## path definitions are relative to package root (where Makefile is run)

import sys

from pyapi.INFO import *
project = name
copyright = author + ". " + license

## sphinx
extensions = [
  'sphinx.ext.autodoc', 
  'sphinx.ext.doctest', 
  'sphinx.ext.intersphinx', 
  'sphinx.ext.todo', 
  'sphinx.ext.coverage', 
  'sphinx.ext.viewcode',
  'sphinx.ext.autosummary']
source_suffix = ".rst"
master_doc = "index"
templates_path = ['doc']
sys.path.append(".")

## autodoc

autodoc_default_flags = [
  'members'             
]


autodoc_default_flags2 = [
  'members', 
  'undoc-members', 
  'private-members', 
  'no-special-members', 
  'inherited-members',
  'show-inheritance'
]

## formatting
add_function_parentheses = True
add_module_names = True

pygments_style = 'sphinx'

## html output
html_theme = 'default'
rightsidebar = True
#html_logo = None
#html_favicon = None
#html_static_path = ['doc']
html_last_updated_fmt = '%Y-%m-%d %H:%M'