# Pre Requirements

## Configure APT Repository

- Add **ROS2**'s **APT** keys.
  ``` sh
  ~$ sudo apt install curl gnupg2 lsb-release
  ~$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
  ```
- Add **ROS2**'s sources list.
  ``` sh
  ~$ sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
  ```
- Update the **APT** repository using `sudo apt update` command.

# Setup Process

## ROS Installation

- Install **ROS2** Base _(recommended)_.
  ``` sh
  ~$ sudo apt install ros-dashing-ros-base
  ```
- Install **ROS2** Desktop _(alternative)_.
  ``` sh
  ~$ sudo apt install ros-dashing-desktop
  ```

## Initialize Rosdep

- Initialize rosdep using `sudo rosdep init` command.
- Update rosdep using `rosdep update` command.

## Environment Setup

- In the `~/.bashrc`, add the following text on the bottom of the file:
  ```
  source /opt/ros/dashing/setup.bash
  ```
  > **Note:** if you are using **Zsh**, modify `~/.zshrc` instead of `~/.bashrc` and source `/opt/ros/dashing/setup.zsh` instead of `/opt/ros/dashing/setup.bash`.

## Setup Dependencies for Building Packages

- Install basic dependencies for **ROS2**.
  ``` sh
  ~$ rosdep install --from-paths ros2-linux/share --ignore-src --rosdistro dashing -y --skip-keys "console_bridge fastcdr fastrtps libopensplice67 libopensplice69 osrf_testing_tools_cpp poco_vendor rmw_connext_cpp rosidl_typesupport_connext_c rosidl_typesupport_connext_cpp rti-connext-dds-5.3.1 tinyxml_vendor tinyxml2_vendor urdfdom urdfdom_headers"
  ```
- Install **ROS2** build tools dependencies.
  ``` sh
  ~$ sudo apt install python-rosinstall python-rosinstall-generator python-wstool build-essential
  ```
- Install colcon python package for building **ROS2**.
  ``` sh
  ~$ sudo apt install python3-colcon-common-extensions
  ```
- Install rm2-cyclone-dds-cpp package for **ROS2** DDS implementation.
    - install the package
      ``` sh
      ~$ sudo apt install ros-dashing-rmw-cyclonedds-cpp
      ```
    - switch the rmw implementation
      ``` sh
      ~$ export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
      ```
