# Setup OpenCV

- Install dependencies
  ```sh
  $ sudo apt-get install build-essential
  $ sudo apt-get install cmake git libgtk2.0-dev pkg-config libavcodec-dev libavformat-dev libswscale-dev
  $ sudo apt-get install python-dev python-numpy libtbb2 libtbb-dev libjpeg-dev libpng-dev libtiff-dev libjasper-dev libdc1394-22-dev
  ```
- Clone OpenCV from repository
  ``` sh
  $ cd ~/Downloads
  $ git clone https://github.com/opencv/opencv.git
  $ cd opencv
  $ git checkout 3.3.0
  ```
- Clone OpenCV Contrib from repository
  ```sh
  $ cd ~/Downloads
  $ git clone https://github.com/opencv/opencv_contrib.git
  $ cd opencv_contrib
  $ git checkout 3.3.0
  ```
- Build and Install OpenCV
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