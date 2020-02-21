### Enable Autostart on Power Failure

- Enter Intel Visual BIOS (press `f2` when booting)
- Choose `Advanced` -> `Power`
- On `After Power Failure`, select `Power On`

### Linux Installation
Use Ubuntu [18.04.3 Desktop (64-bit)](http://old-releases.ubuntu.com/releases/bionic/ubuntu-18.04-desktop-amd64.iso)

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
Install net-tools
```sh
$ sudo apt install net-tools
```