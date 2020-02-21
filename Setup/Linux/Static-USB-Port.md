## Assign a Static USB Port

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