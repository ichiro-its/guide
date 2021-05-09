# Pre Requirements

## Verifying Graphics Driver Installation

- Make sure that **Nvidia** driver was already installed in the PC, for more information please refers [here](https://cyberbotics.com/doc/guide/verifying-your-graphics-driver-installation).

## Configure APT Repository

- Add **Cyber Robotics**'s **APT** keys.
  ``` sh
  ~$ curl -s -L https://www.cyberbotics.com/Cyberbotics.asc | sudo apt-key add -
  ```
- Add **Cyber Robotics**'s **APT** repository.
  ``` sh
  ~$ sudo apt-add-repository 'deb https://www.cyberbotics.com/debian/ binary-amd64/'
  ```
- Update the **APT** repository using `sudo apt update` command.

# Installation

- Install as usual using `apt install` command.
  ``` sh
  ~$ sudo apt install webots
  ```
> **Note:** **Webots** requires large amount of space _(around 2 GB)_, so the installation process will take a lot of time.

# Post Install

- Run **Webots** from application launcher or from `webots` command.
- On the first start you will be asked to chose theme and try some example simulation.

> **Note:** If there is a warning about unsupported graphics driver, make sure that graphics drivers already installed properly as in [Pre Requirements](#Pre-Requirements) section. _(Although sometimes simulation could still be run without graphics driver installed)_.

> **Note:** If you are new in **Webots** it is recommended to try the tutorial first in [here](https://cyberbotics.com/doc/guide/tutorials).

# Configure Webots with Linux Environment

> **Note:** For each new controller created, add a `WEBOTS_HOME` variable that contains path to the **Webots**'s controller in the controller's `Makefile` file.

## Add Webots Home Path to Environment Variable

- In your `~/.bashrc` file _(or `~/.zshrc` if using **Zsh**)_, add the following text in the bottom of the file to export WEBOTS_HOME environment variable that contains a path to **Webots** directory _(usually it is `/usr/local/webots`)_.
  ``` sh
  export WEBOTS_HOME=/usr/local/webots
  ```
- Reload the environment with `source` command.

## Configure Webots Library Path
- Create a symbolic link from some of **Webots**'s library to the default library path.
  ``` sh
  ~$ sudo ln -s $WEBOTS_HOME/lib/controller/libController.so /usr/local/lib/libWebotsController.so
  ~$ sudo ln -s $WEBOTS_HOME/lib/controller/libCppController.so /usr/local/lib/libWebotsCppController.so
  ~$ sudo ln -s $WEBOTS_HOME/lib/webots/libpng12.so.0 /usr/local/lib/libpng12.so.0
  ```

## Configure Webots Include Path
- Create a symbolic link from **Webots**'s include path to the default include path.
  ``` sh
  ~$ sudo ln -s $WEBOTS_HOME/include/controller/cpp/webots /usr/local/include/webots
  ```

# Installation from Source

## Clone the Github Repository
- Create the development directory in home directory and clone the repository.
    ```sh
    ~$ git config --global credential.helper store
    ~$ git config --global user.email "you@example.com"
    ~$ git config --global user.name "Your Name"
    ~$ git config --global push.default simple
    ~$ git clone --recurse-submodules -j8 https://github.com/cyberbotics/webots.git
    ~$ cd webots
    ```

## Install Prerequisites Packages
- Install the Webots dependencies.
    ```sh
    ~$ sudo scripts/install/linux_compilation_dependencies.sh
    ```

## Setup Your Bash Profile
- Check the content of `scripts/install/bashrc.linux`.
    ```sh
    ~$ cat scripts/install/bashrc.linux >> ~/.bashrc
    ```
- Adapt the paths to match your system setup, and append it at the end of `~/.bashrc`.
    ```sh
    ~$ source ~/.bashrc
    ```

## Install Optional Dependencies [ optional ]
- Install the Webots optional dependencies.
    ```sh
    ~$ sudo scripts/install/linux_optional_compilation_dependencies.sh
    ```

## Build Webots
- Compile Webots and automatically download the required resources in the dependencies folder.
    ```sh
    ~$ make
    ```

> **Note**: if you find `fatal error: <library name>: No such file or directory`, it because the library is not installed yet.

> **Note**: There are some possible libraries with their installation.
1. `ft2build.h`
    ```sh
    ~$ sudo apt-get install libfreetype6-dev
    ```
2. `GL/gl.h`
    ```sh
    ~$ sudo apt install libglm-dev
    ```
3. `stb/stb_image.h` and `stb/stb_image_write.h`
    ```sh
    ~$ git clone https://github.com/nothings/stb.git
    ~$ sudo cp stb/stb_image.h /usr/local/include/
    ~$ sudo cp stb/stb_image_write.h /usr/local/include/
    ```
4. `libusb/libusb.h`
    ```sh
    ~$ sudo apt-get install libusb-dev
    ```
5. `libssh/libcrypto.h`
    ```sh
    ~$ sudo apt-get install libssl-dev
    ```
6. `zip.h`
    ```sh
    ~$ sudo apt-get install libzip-dev
    ```