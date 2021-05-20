Start TigerVNC Server Using Existing Display
============================================

This section will explain a guide on starting a VNC server to remote desktop an existing display using `TigerVNC <https://tigervnc.org/>`_ scraping server.

Setup TigerVNC Scraping Server
------------------------------

Use :ref:`APT <apt-guide>` to install TigerVNC Scraping Server.

.. code-block:: bash

  $ sudo apt install tigervnc-scraping-server

Generate VNC Password Configuration
-----------------------------------

Run the following command to generate a VNC password configuration on ``~/.vnc/passwd``.

.. code-block:: bash

  $ vncpasswd

.. note::

  After inputting the password, the program will ask to enter a view-only password.
  It's recommended to ignore this and use the same password for the view-only mode.

Start TigerVNC Scraping Server
------------------------------

Run the following command to start TigerVNC scraping server using the existing display.
After that, the server could be accessed using VNC client on port ``5900`` (the default port).

.. code-block:: bash

  $ x0vncserver -passwordfile ~/.vnc/passwd

.. note::

  The password file option should be provided.
  Else, some clients may refuse to connect to the server.

.. seealso::

  `X0vncserver manual <https://tigervnc.org/doc/x0vncserver.html>`_ on the official TigerVNC documentation.
