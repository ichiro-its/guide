# Pre Requirements

- A **Linux x86/x64** host _(it is recommended to use **Ubuntu 16.04/18.04**)_.
- A **Jetson TX2 Developer Kit** _(connected to the host with **USB Micro AB cable**)_.

# Prepare the Host

## Setup Dependencies in the Host

- Install **Python** and **XTERM** using `sudo apt install python xterm`.
- If there is **TLP** installed, remove it using `sudo apt remove tlp`.

## Setup NVIDIA SDK Manager

- Download the **NVIDIA SDK Manager** from [here](https://developer.nvidia.com/nvidia-sdk-manager)
  _(a **NVIDIA Developer account** is needed to download it)_.
- Install it with `dpkg -i <deb_file>` command. Or you can follow the **Setting up** instructions in the Download page.

## Run NVIDIA SDK Manager

- Run **NVIDIA SDK Manager** with `sdkmanager` command or dirrectly from software launcher.
- Login with **NVIDIA Developer account**.

> **Note:** There is a small problem with **NVIDIA SDK Manager** that it won't work in **1366x768** or lower resolution *(the button and some bottom user interfaces are cropped in that resolution)*.
> So either you could use **Tab** button to scroll the page *(to display the bottom of truncated user interfaces)*.

# Configure Flash Options

## Development Environment

- In **Hardware Configuration**, choose **Jetson TX2 (P3310)** for the Target Hardware.
- In **Target Operating System**, choose Linux JetPack with the most recent version
  _(the last version used was **JetPack 4.3**)_.
- Continue to the next step.

## Details and License

- In **Target Components**, only choose **Jetson OS** and **Jetson SDK Components**.
- Accept the terms and conditions.
- Continue to the next step.

# Flash Process

## Prepare Flash Component

- Enter the **superuser** password.
- The **NVIDIA SDK Manager** will download required components and install it to the host.
- After those processes finished, you will be prompted to connect the host with the **Jetson TX2**.
- Then, you may choose a **Manual Setup** *(from its default choice, **Automatic Setup**)* to do a fresh installation.

## Manual Setup

- Boot the **Jetson TX2** in recovery mode by pressing the **Reset button** _(RES)_ while holding the **Recovery Force button** _(REC)_.
  After that, hold the **Recovery Force button** _(REC)_ for about 2 seconds.

> **Note:** Recovery mode is indicated by both LEDs next to the **Recovery Force button** _(REC)_ turned on and the connected display is not showing anything.

> **Note:** Make sure the **Jetson TX2** is connected to the host with `lsusb` command _(indicated as **Nvidia Corp.**)_.

- Click flash to continue.

> **Note:** In case of failed _(device not connected or haven't set to recovery mode)_, reboot the **Jetson TX2** in recovery mode. If still failed, reboot the host.

## Ubuntu Setup

- Set the language _(default is **English**)_.
- Set the keyboard layout _(default is **English (US)**)_.
- Set the timezone _(default is **Jakarta**/GMT+7)_.
- Set the username _(default is **ichiro**)_.
- Set the hostname _(use robot name, in lowercase)_.
- Set the password.

> **Note:** It is recommended to connect to the internet in this process.

## SDK Components Install

- Input the IP address if **Jetson TX2** is using different IP address from the default _(default is **192.168.55.1**)_.
- Input the username and password of **Jetson TX2**.
- Click install to continue.

# Post Flash

- The **Jetson TX2** comes with some unused program that won't be used for developing like **LibreOffice**, **Thunderbird**, **Rhythmbox**, and **Shotwell**. You may remove them using `sudo apt remove <program>`.
- Sometimes the clock is wrongly set. You may fix this manually using `sudo date -s "<DD> <MON> <YYYY> <HH>:<MM>:<SS>"` or automatically using `sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"` _(require an internet access)_.