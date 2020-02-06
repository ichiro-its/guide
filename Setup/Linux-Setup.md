### Enable Autostart on Power Failure

- Enter Intel Visual BIOS (press `f2` when booting)
- Choose `Advanced` -> `Power`
- On `After Power Failure`, select `Power On`

### Linux Installation
Use Ubuntu [14.04.4 Desktop (64-bit)](http://old-releases.ubuntu.com/releases/14.04.4/ubuntu-14.04.4-desktop-amd64.iso)

### Downgrade Linux Kernel

Install Ukuu
```sh
$ sudo add-apt-repository ppa:teejee2008/ppa
$ sudo apt-get update
$ sudo apt-get install ukuu
```

Install kernel `4.2.8`
```sh
$ xhost +
$ sudo ukuu --install v4.2.8-ckt13
$ reboot now
```

### Update date

Update date from google.com (using internet)
```sh
$ sudo date -s "$(wget -qSO- --max-redirect=0 google.com 2>&1 | grep Date: | cut -d' ' -f5-8)Z"
```

### Fix Root Permission
Add user to appropriate groups (dialout for serial, video for camera)
```sh
$ sudo usermod -aG dialout $USER
$ sudo usermod -aG video $USER
```
Increase real-time scheduling priority (for thread)
```sh
$ sudo bash -c 'echo "@"'$USER'" - rtprio 99" > /etc/security/limits.d/'$USER'-rtprio.conf'
```
### Setup Remote Server
Install openssh-server
```sh
$ sudo apt-get install openssh-server sshfs
```
### Setup Samba Share
Install samba
```sh
$ sudo apt-get install samba samba-common python-glade2 system-config-samba
```
Add samba user (using current user password)
```sh
$ sudo smbpasswd -a $USER
```
In `/etc/samba/smb.conf` add this at the bottom
```
[<current_user>]
        path = /home/<current_user>
        writeable = yes
        valid users = <current_user>
```

### Setup DHCP Server
Install DHCP Server
```sh
$ sudo apt-get update
$ sudo apt-get install isc-dhcp-server net-tools
$ sudo apt-get upgrade
```
Find ethernet interface name (ex: eth0) using
```sh
$ ifconfig
```
In `/etc/default/isc-dhcp-server`
```
INTERFACES="eth0"
```
Set robot ip as in [here](https://gitlab.com/ICHIRO-ITS/readme/blob/master/COMMAND.md) (ex: ithaaro 192.168.123.1)
In `/etc/dhcp/dhcpd.conf`
```
subnet 192.168.123.0 netmask 255.255.255.0 {
  range 192.168.123.64 192.168.123.128;
  option routers 192.168.123.1;
  option broadcast-address 192.168.123.255;
  default-lease-time 600;
  max-lease-time 7200;
}
```
In `/etc/network/interfaces` add
```
auto eth0
iface eth0 inet static
address 192.168.123.7
netmask 255.255.255.0
```
Start dhcp server
```sh
$ sudo service isc-dhcp-server start
$ sudo systemctl restart isc-dhcp-server
$ sudo ufw allow  67/udp
$ sudo ufw reload
$ sudo service networking restart
```

### Setup Git
Install git
```sh
$ sudo apt-get install git
```
Setup global user name and email
```sh
$ git config --global user.name 'ichiro-'$USER
$ git config --global user.email "ichiro.its@gmail.com"
```
Generate public ssh key (enter empty passphrase)
```sh
$ ssh-keygen -t rsa
```
- Open [GitLab.com](https://gitlab.com/users/sign_in)
- Sign In as `ICHIRO-ITS-Admin`
- Open setting for [SSH Keys](https://gitlab.com/profile/keys)
- Add Key as in `~/.ssh/id_rsa.pub`

### Setup OpenCV
Install dependencies
```sh
$ sudo apt-get install build-essential
$ sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
$ sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
```
Clone OpenCV from repository
``` sh
$ cd ~/Downloads
$ git clone https://github.com/opencv/opencv.git
$ cd opencv
$ git checkout 3.3.0
```
Clone OpenCV Contrib from repository
```sh
$ cd ~/Downloads
$ git clone https://github.com/opencv/opencv_contrib.git
$ cd opencv_contrib
$ git checkout 3.3.0
```
Build OpenCV
```sh
$ cd ~/Downloads/opencv
$ mkdir build
$ cd build
$ cmake -D CMAKE_BUILD_TYPE=Release -D CMAKE_INSTALL_PREFIX=/usr/local ..
$ make -j4
$ sudo make install
$ sudo sh -c 'echo "/usr/local/lib" >> /etc/ld.so.conf.d/opencv.conf'
$ sudo ldconfig
```

### Setup Zsh

Install Zsh
```sh
$ sudo apt-get install zsh
```
Set Zsh as default
```sh
$ chsh -s /usr/bin/zsh
```
Install Oh My Zsh
```sh
$ sh -c "$(wget https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"
$ cp ~/.oh-my-zsh/templates/zshrc.zsh-template ~/.zshrc
```
Change theme, in `~/.zshrc`, edit following
```sh
ZSH_THEME="agnoster"
```
Reload Zsh
```sh
$ source ~/.zshrc
```

### Library Setup
Install ncurse (terminal interface library)
```sh
$ sudo apt-get install libncurses5-dev
```
Install yaml-cpp (yaml file parser), get source [here](https://github.com/jbeder/yaml-cpp/archive/release-0.3.0.tar.gz)
```sh
$ cd <download_location>
$ tar -xvzf <yaml_file>.tar.gz
$ cd <yaml_folder>
$ mkdir build
$ cd build
$ cmake ..
$ make -j4
$ sudo make install
```
Install eigen (linear algebra library), get source [here](http://bitbucket.org/eigen/eigen/get/3.3.7.tar.bz2)
```sh
$ cd <download_location>
$ tar jxf <eigen_file>.tar.bz2
$ cd <eigen_folder>
$ mkdir build
$ cd build
$ cmake ..
$ make -j4
$ sudo make install
```

### Additional Setup
Install vim (text editor)
```sh
$ sudo apt-get install vim
```
Install screen (terminal emulator)
```sh
$ sudo apt-get install screen
```
Install Visual Studio Code (Code Editor), get .deb file [here](https://go.microsoft.com/fwlink/?LinkID=760868)
```sh
$ cd <download_location>
$ sudo dpkg -i ./<file>.deb
```
Install nmap (IP Address Finder)
```sh
$ sudo apt-get install nmap
```
Install neofetch (system info)
```sh
$ cd ~/Downloads
$ git clone https://github.com/dylanaraps/neofetch
$ cd neofetch
$ sudo make install
```
### Assign a Static USB Port
This part is a procedure to solve the problem where the USB port of devices on a robot not properly connected with the program, especially ROS 2 program (framework). So, assign a static USB port to create a symbolic link for the USB device on robot is its solution. The devices port should be assigned one by one, to do that follow these steps:
- Unplug all of the devices from robot first
- Plug only a device which wants to assign
- Find port where the device plugged in using (usually on `/dev/ttyUSBx`):
```sh
$ ls /dev/
```
where `x` is a number that matches with the device port (ex. `/dev/ttyUSB0`).
- List USB attributes for the device:
```sh
$ udevadm info --name=/dev/ttyUSBx --attribute-walk
```
- In the list, look idVendor. Example:
```sh
  ...
  ATTRS{idVendor}=="1d6b"
  ...
```
- Open (if there is nothing, just create) a file `/etc/udev/rules.d/99-usb-serial.rules`, and append this following line in that rule file:
```sh
KERNEL=="ttyUSB0", ATTRS{idVendor}=="1d6b", SYMLINK+="cm740"
```
set the kernel (i.e `ttyUSB0`), idVendor of the device (i.e `1d6b`), and the name of the symbolic link (i.e `cm740`) which will be an assigned port name for the device (i.e CM740 device).

> **Note**: If on the list of device attribute there is nothing idVendor such as above, the static assignment can be make based on the USB kernel Id (i.e `KERNELS=="1-4:1.0"`).
> Then, in a file `/etc/udev/rules.d/99-usb-serial.rules`, append this following statement `KERNEL=="ttyUSB0", KERNELS=="1-4:1.0", SYMLINK+="cm740"` with the properly USB kernel of device

- Reload the udevadm rules:
```sh
$ udevadm control --reload-rules
```