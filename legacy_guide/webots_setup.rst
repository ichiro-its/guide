Webots Setup
============

Installation Using APT
----------------------

Pre Requirements
~~~~~~~~~~~~~~~~

Verifying Graphics Driver Installation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Make sure that **Nvidia** driver was already installed in the PC, for more information please refers `here <https://cyberbotics.com/doc/guide/verifying-your-graphics-driver-installation>`_.

Configure APT Repository
^^^^^^^^^^^^^^^^^^^^^^^^

-  Add **Cyber Robotics**'s **APT** keys.

   .. code:: bash

      ~$ curl -s -L https://www.cyberbotics.com/Cyberbotics.asc | sudo apt-key add -
   ..
-  Add **Cyber Robotics**'s **APT** repository.

   .. code-block:: bash
      
      ~$ sudo apt-add-repository 'deb https://www.cyberbotics.com/debian/ binary-amd64/'
   ..
-  Update the **APT** repository using ``sudo apt update`` command.

Installation
~~~~~~~~~~~~

-  Install as usual using ``apt install`` command.

   .. code-block:: bash

      ~$ sudo apt install webots
   ..
   
   .. note:: 

      **Webots** requires large amount of space *(around 2 GB)*, so the installation process will take a lot of time.
   ..
   

Post Install
~~~~~~~~~~~~

-  Run **Webots** from application launcher or from ``webots`` command.
-  On the first start you will be asked to chose theme and try some example simulation. 
   
   .. note::
      
      If there is a warning about unsupported graphics driver, make sure that graphics drivers already installed properly as in `Pre Requirements <#Pre-Requirements>`_ section. *(Although sometimes simulation could still be run without graphics driver installed)*.
   ..
   
   .. note::

      If you are new in **Webots** it is recommended to try the tutorial first in `here <https://cyberbotics.com/doc/guide/tutorials>`_.
   ..
   

Configure Webots with Linux Environment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. note::
   For each new controller created, add a ``WEBOTS_HOME`` variable that contains path to the **Webots**'s controller in the controller's ``Makefile`` file.
..

Add Webots Home Path to Environment Variable
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  In your ``~/.bashrc`` file (or ``~/.zshrc`` if using **Zsh**), add the following text in the bottom of the file to export WEBOTS\_HOME environment variable that contains a path to **Webots** directory (usually it is ``/usr/local/webots``).
   
   .. code-block:: bash
   
      export WEBOTS_HOME=/usr/local/webots
   ..
-  Reload the environment with ``source`` command.

Configure Webots Library Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Create a symbolic link from some of **Webots**'s library to the default library path.

   .. code-block:: bash
      
      ~$ sudo ln -s $WEBOTS_HOME/lib/controller/libController.so /usr/local/lib/libWebotsController.so
      ~$ sudo ln -s $WEBOTS_HOME/lib/controller/libCppController.so /usr/local/lib/libWebotsCppController.so
      ~$ sudo ln -s $WEBOTS_HOME/lib/webots/libpng12.so.0 /usr/local/lib/libpng12.so.0
   ..

Configure Webots Include Path
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

-  Create a symbolic link from **Webots**'s include path to the default include path.
   
   .. code-block:: bash
      
      ~$ sudo ln -s $WEBOTS_HOME/include/controller/cpp/webots /usr/local/include/webots
   ..

Installation from Source
------------------------

Clone the Github Repository
~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Clone the repository.

   .. code-block:: bash

      ~$ git clone --recurse-submodules --branch release https://github.com/RoboCup-Humanoid-TC/webots
      ~$ cd webots
   ..

Install Prerequisites Packages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  Install the **Webots** dependencies.
   
   .. code-block:: bash
      
      ~$ sudo scripts/install/linux_compilation_dependencies.sh
      ~$ sudo scripts/install/linux_optional_compilation_dependencies.sh
   ..
-  Install the other required packages.
   
   .. code-block:: bash

      ~$ sudo apt install python-is-python3
   ..

Build Webots
~~~~~~~~~~~~

-  Compile **Webots**. 

   .. code-block:: bash
   
      ~$ make
   ..

Setup Your Bash Profile
~~~~~~~~~~~~~~~~~~~~~~~

-  Append the string in ``WEBOTS_HOME=/path/to/webots`` to ``~/.bashrc``.
   
   .. code-block:: bash
      
      ~$ echo WEBOTS_HOME=/path/to/webots >> ~/.bashrc
   ..

Post Install
~~~~~~~~~~~~

-  Build the latest version of the official RoboCup Humanoid TC fork of the `GameController <https://github.com/RoboCup-Humanoid-TC/GameController>`__.
   
   .. code-block:: bash
   
      ~$ sudo apt-get install ant
      ~$ git clone https://github.com/RoboCup-Humanoid-TC/GameController
      ~$ cd GameController
      ~$ ant
   ..
-  Install Python dependencies.
   
   .. code-block:: bash
   
      ~$ cd webots/projects/samples/contests/robocup/controllers/referee
      ~$ pip3 install -r requirements.txt
   ..
-  Build the controllers. 
   
   .. code-block:: bash
      
      ~$ apt-get install protobuf-compiler libprotobuf-dev libjpeg9-dev
      ~$ cd webots/projects/samples/contests/robocup
      ~$ make
   ..

Run the Demo
~~~~~~~~~~~~

-  Open the `robocup.wbt <https://github.com/RoboCup-Humanoid-TC/webots/blob/release/projects/samples/contests/robocup/worlds/robocup.wbt>`_ world file in Webots and run it until you see the GameController window showing up.
   
   .. code-block:: bash
   
      export GAME_CONTROLLER_HOME=/path/to/GameController JAVA_HOME=/usr
      ./webots ./projects/samples/contests/robocup/worlds/robocup.wbt
   ..

   You have to pass the environment variables ``GAME_CONTROLLER_HOME`` which points to the ``GameController`` folder and ``JAVA_HOME`` which points to your Java installation (which might be under ``/usr``).
-  You can manually move the robots and the ball using the mouse (Shift-right-click-and-drag).
