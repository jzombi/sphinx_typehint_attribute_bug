import os
import sys
sys.path.insert(0, os.path.abspath('../../mymodule'))
sys.path.insert(0, os.path.abspath('../../'))

project = 'mymodule'
copyright = '2022, x'
author = 'x'

release = 'x'

extensions = [
    'sphinx.ext.autodoc',
]

autodoc_default_options = {
    'inherited-members': False,
    'show-inheritance': True,
}
autodoc_default_flags = ['members', 'inherited-members', 'show-inheritance']
autodoc_typehints = 'description'
autodoc_typehints_description_target = 'documented'
autodoc_typehints_format = 'short'

templates_path = ['_templates']

exclude_patterns = []

html_theme = 'alabaster'

html_static_path = ['_static']
