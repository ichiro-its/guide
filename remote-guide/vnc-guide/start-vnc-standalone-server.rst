Start VNC Server Using Virtual Display
======================================

This section will explain a guide on starting a :ref:`VNC <vnc-guide>` server to remote desktop a virtual display using `TigerVNC <https://tigervnc.org/>`_ standalone server (:code:`vncserver`).

Setup TigerVNC Standalone Server
--------------------------------

TigerVNC standalone server is available on :ref:`APT <apt-guide>` as :code:`tigervnc-standalone-server` package.

.. code-block:: bash

   $ apt install tigervnc-standalone-server

Generate VNC Password Configuration
-----------------------------------

Run the following command to generate a VNC password configuration on :code:`~/.vnc/passwd`.

.. code-block:: bash

   $ vncpasswd

.. note::

   After inputting the password, the program will ask to enter a view-only password.
   It's recommended to ignore this and use the same password for the view-only mode.

Configure X Display for VNC
---------------------------

Create or modify :code:`~/.vnc/xstartup` with the following content:

* For `Gnome Desktop <https://www.gnome.org/>`_:

  .. code-block:: bash

     #!/bin/bash

     unset SESSION_MANAGER
     unset DBUS_SESSION_BUS_ADDRESS
     export XKL_XMODMAP_DISABLE=1

     gnome-session &
     gnome-panel &
     gnome-settings-daemon &
     metacity &
     nautilus &

* For `Budgie Desktop <https://github.com/solus-project/budgie-desktop>`_:

  .. code-block:: bash

     #!/bin/bash

     unset SESSION_MANAGER
     unset DBUS_SESSION_BUS_ADDRESS

     gnome-session --session=budgie-desktop &
     budgie-wm &
     budgie-panel &

Start a TigerVNC Standalone Server
----------------------------------

Run the following command to start a TigerVNC standalone server using a virtual display.
After that, the server could be accessed using VNC client on port :code:`5900 + display_id` (e.g. server with display id :code:`:1` could be accessed on port :code:`5901`).

.. code-block:: bash

   $ vncserver -localhost no -passwordfile ~/.vnc/passwd

.. note::

   The password file option should be provided.
   Else, some clients may refuse to connect to the server.

List All Running TigerVNC Standalone Servers
--------------------------------------------

Run the following command to list all running TigerVNC standalone servers.

.. code-block:: bash

   $ vncserver -list

Kill a Running TigerVNC Standalone Server
-----------------------------------------

Run :code:`vncserver` command with :code:`-kill` options followed by server's display id to kill a running TigerVNC standalone server.
For example, the following command will kill a running server with display id :code:`:1`.

.. code-block:: bash

   $ vncserver -kill :1
