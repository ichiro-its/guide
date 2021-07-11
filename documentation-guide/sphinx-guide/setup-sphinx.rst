Setup a Sphinx Project
======================

This section will explain a guide on setting up a :ref:`Sphinx <sphinx-guide>` project.

.. seealso::

   `Sphinx installation <https://www.sphinx-doc.org/en/master/usage/installation.html>`_ and `getting started on Sphinx <https://www.sphinx-doc.org/en/master/usage/quickstart.html>`_ on the official Sphinx documentation.

Sphinx Installation
-------------------

Sphinx is available on :ref:`pip <pip-guide>` as :code:`sphinx` package.

.. code-block:: bash

   $ pip install -U sphinx

Alternatively, Sphinx is also available on :ref:`APT <apt-guide>` as :code:`python3-sphinx` package.

.. code-block:: bash

   $ apt install python3-Sphinx

Create a Sphinx Project
-----------------------

Use :code:`sphinx-quickstart` command to create a configuration file (:code:`conf.py`) for the Sphinx project.

.. code-block:: bash

   $ sphinx-quickstart
