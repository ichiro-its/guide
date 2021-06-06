Build Documentations Using Sphinx
=================================

This section will explain a guide on building documentation from a :ref:`Sphinx <sphinx-guide>` project.

.. seealso ::

   `Getting started on Sphinx <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_ on the official Sphinx documentation.

Build HTML Pages From a Sphinx Project
--------------------------------------

Use ``sphinx-build`` command with ``-b html`` options followed by source files and the output directory.
For example, the following command will build HTML page from current directory to the ``_build`` directory.

.. code-block:: bash

   $ sphinx-build -b html . _build
