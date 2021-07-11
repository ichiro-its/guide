Setup a Doxygen Project
=======================

This section will explain a guide on setting up a :ref:`Doxygen <doxygen-guide>` project.

.. seealso::

   `Doxygen installation <https://www.doxygen.nl/manual/install.html>`_ and `getting started on Doxygen <https://www.doxygen.nl/manual/starting.html>`_ on the official Doxygen documentation.

Doxygen Installation
--------------------

Doxygen is available on :ref:`APT <apt-guide>` as :code:`doxygen` package.

.. code-block:: bash

   $ apt install doxygen

Create a Doxygen Project
------------------------

Use :code:`doxygen` command with a :code:`-g` option to create a configuration file (:code:`Doxyfile`) for the Doxygen project.

.. code-block:: bash

   $ doxygen -g

The resulted configuration file contains a lot of options with a description on it.
But it could be simplified as follows:

.. code-block::

   PROJECT_NAME           = "My Project"
   PROJECT_NUMBER         = "v0.1.0"
   PROJECT_BRIEF          = "A brief description"
   TAB_SIZE               = 2
   INPUT                  = ./include
   RECURSIVE              = YES
   GENERATE_HTML          = YES
   HTML_OUTPUT            = html
   GENERATE_LATEX         = YES
   LATEX_OUTPUT           = latex
