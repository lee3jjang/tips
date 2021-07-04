Sphinx 설정하기
================

1. cmd 창에서 ``pip install git+https://github.com/bashtage/sphinx-material.git``
2. ``sphinx-quickstart`` 커맨드 입력 후 ``conf.py`` 을 열어서 아래처럼 수정

.. code-block:: python

    import os
    import sys
    sys.path.insert(0, os.path.abspath('..'))

    html_theme = 'sphinx_material'

    extensions = [
        'sphinx.ext.autodoc',
        "sphinx.ext.githubpages",
        'nbsphinx',
        'sphinx.ext.autosummary',
        'IPython.sphinxext.ipython_console_highlighting',
        'IPython.sphinxext.ipython_directive',
        'numpydoc',
    ]

    html_sidebars = {
        "**": ["globaltoc.html", "localtoc.html", "searchbox.html", "logo-text.html"]
    }

    html_theme_options = {
        "nav_title": '타이틀',
        "nav_links": [
            {"href": "https://www.naver.com", "title": "네이버", "internal": False},
        ],
        "heroes": {
            "index": "설명",
        },
        'color_primary': 'red',
        'color_accent': 'light-red',
        'repo_url': 'https://github.com/lee3jjang/tips',
        'repo_name': 'tips',
        'repo_type': 'github',
        'logo_icon': '&#xe80e',
    }
