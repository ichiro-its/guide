import sphinx_rtd_theme

project = 'ICHIRO ITS Guide'

copyright = '2019-2021, ICHIRO ITS'
author = 'ICHIRO ITS'

version = ''
release = ''

extensions = [
    'myst_parser',
    'sphinx_rtd_theme',
]

templates_path = ['_templates']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

master_doc = 'index'

language = None

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = None

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
htmlhelp_basename = 'guidedoc'
