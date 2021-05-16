# ROS Setup

## Pre Requirements

### Configure APT Repository

- Add **ROS**'s sources list.
  ``` sh
  ~$ sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
  ```
- Add **ROS**'s **APT** keys.
  ``` sh
  ~$ curl -sSL 'http://keyserver.ubuntu.com/pks/lookup?op=get&search=0xC1CF6E31E6BADE8868B172B4F42ED6FBAB17C654' | sudo apt-key add -
  ```
- Update the **APT** repository using `sudo apt update` command.

## Setup Process

### ROS Installation

- Install **ROS** Base _(recommended)_.
  ``` sh
  ~$ sudo apt install ros-melodic-ros-base
  ```
- Install **ROS** Desktop _(alternative)_.
  ``` sh
  ~$ sudo apt install ros-melodic-desktop
  ```
- Install **ROS** Desktop Full _(alternative)_.
  ``` sh
  ~$ sudo apt install ros-melodic-desktop-full
  ```

### Initialize Rosdep

- Initialize rosdep using `sudo rosdep init` command.
- Update rosdep using `rosdep update` command.

### Environment Setup

- In the `~/.bashrc`, add the following text on the bottom of the file:
  ```
  source /opt/ros/melodic/setup.bash
  ```
  > **Note:** if you are using **Zsh**, modify `~/.zshrc` instead of `~/.bashrc` and source `/opt/ros/melodic/setup.zsh` instead of `/opt/ros/melodic/setup.bash`.

### Setup Dependencies for Building Packages

- Install the following dependencies for building **ROS** packages.
  ``` sh
  ~$ sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
  ```
