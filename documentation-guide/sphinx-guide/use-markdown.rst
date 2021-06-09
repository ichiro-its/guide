Enable Markdown in Sphinx
=========================

This section will explain a guide on enabling `Markdown <https://daringfireball.net/projects/markdown/>`_ in a :ref:`Sphinx <sphinx-guide>` project using `MyST <https://myst-parser.readthedocs.io/en/latest/index.html>`_.

.. seealso::

   * `Getting Started on MyST <https://myst-parser.readthedocs.io/en/latest/using/intro.html>`_ on the official MyST documentation.
   * `Use Markdown in Sphinx <https://www.sphinx-doc.org/en/master/usage/markdown.html>`_ on the official Sphinx documentation.

MyST Installation
-----------------

MyST is available on :ref:`pip <pip-guide>` as :code:`myst-parser` package.

.. code-block:: bash

   $ pip install myst-parser

Configure MyST in a Sphinx Project
----------------------------------

Modify :code:`conf.py` of the project by adding :code:`myst-parser` in the :code:`extensions` list and :code:`'.md'` in the :code:`source_suffix`.

.. code-block:: python

   import sphinx_rtd_theme

   extensions = [
     ...
     "mystparser",
   ]

   source_suffix = {
     '.rst': 'restructuredtext',
     '.md': 'markdown',
   }
