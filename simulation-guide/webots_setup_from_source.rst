Webots Setup
============

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
