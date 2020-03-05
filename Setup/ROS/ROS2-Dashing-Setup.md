# Configure APT Repository

- Add **ROS2**'s **APT** key.
  ```sh
  ~$ curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
  ```
- Add **ROS2**'s repository to the sources list.
  ```sh
  ~$ sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
  ```
- Update the **APT** repositories.
  ```sh
  ~$ sudo apt update
  ```

# ROS2 Installation

- Install either **ROS2** Base _(minimal package)_ using `apt` command.
  ```sh
  ~$ sudo apt install ros-dashing-ros-base
  ```

# Additional Installation

## Colcon Installation

- install **Colcon** to build **ROS2** packages using `apt` command.
  ```sh
  ~$ sudo apt install python3-colcon-common-extensions
  ```

## RMW Cyclone DDS Installation

- Install **RMW Cyclone DDS** using `apt` command.
  ```sh
  ~$ sudo apt install ros-dashing-rmw-cyclonedds-cpp
  ```
