# Setup OpenCV With CUDA

## Pre Requirements

- If **OpenCV** has been installed previously, remove it using `sudo apt purge libopencv*`.
- Install some dependancy as follow:
  ``` sh
  ~$ sudo apt install cmake libavcodec-dev libavformat-dev libavutil-dev \
      libeigen3-dev libglew-dev libgstreamer-plugins-base1.0-dev libgstreamer1.0-dev \
      libgtk2.0-dev libgtk-3-dev libjpeg-dev libpng-dev libpostproc-dev \
      libswscale-dev libtbb-dev libtiff5-dev libv4l-dev libxvidcore-dev libx264-dev \
      python-dev python-numpy python-py python-pytest \
      python3-dev python3-numpy python3-py python3-pytest \
      pkg-config qt5-default zlib1g-dev
  ```

## Build Process

### Clone OpenCV and OpenCV_Contrib Repository

- Clone this repository `https://github.com/opencv/opencv.git`.
- Clone this repository `https://github.com/opencv/opencv_contrib`.
- Change the branch to the most recent **4.2** version _(the last version used was **4.2.0**)_.

### Build OpenCV

- Create `build` directory inside **OpenCV** repository and `cd` to that directory.
- Create Makefiles with the following options:
  ``` sh
  ~$ cmake -D CMAKE_BUILD_TYPE=RELEASE \
      -D CMAKE_INSTALL_PREFIX="/usr/local/" \
      -D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib/modules \
      -D WITH_CUDA=ON \
      -D CUDA_ARCH_BIN=${ARCH_BIN} \
      -D CUDA_ARCH_PTX="" \
      -D ENABLE_FAST_MATH=ON \
      -D CUDA_FAST_MATH=ON \
      -D WITH_CUBLAS=ON \
      -D WITH_LIBV4L=ON \
      -D WITH_GSTREAMER=ON \
      -D WITH_GSTREAMER_0_10=OFF \
      -D WITH_QT=ON \
      -D WITH_OPENGL=ON \
      -D WITH_OPENCL=ON \
      -D BUILD_opencv_python2=OFF \
      -D BUILD_opencv_python3=OFF \
      OPENCV_GENERATE_PKGCONFIG=YES \
      ..
  ```
- Build **OpenCV** with `make -j$(nproc)` command.

  :::{Note}
  If there is a problem with **OpenGL** support, fix it with creating a new patch file which contain the following text:
  ```
  diff --git a/cuda_gl_interop.h b/cuda_gl_interop.h
  index 0f4aa17..e8c538c 100644
  --- a/cuda_gl_interop.h
  +++ b/cuda_gl_interop.h
  @@ -59,13 +59,13 @@
  >
   #else /* __APPLE__ */
  >
  -#if defined(__arm__) || defined(__aarch64__)
  -#ifndef GL_VERSION
  -#error Please include the appropriate gl headers before including cuda_gl_interop.h
  -#endif
  -#else
  +//#if defined(__arm__) || defined(__aarch64__)
  +//#ifndef GL_VERSION
  +//#error Please include the appropriate gl headers before including cuda_gl_interop.h
  +//#endif
  +//#else
  #include <GL/gl.h>
  -#endif
  +//#endif
  >
   #endif /* __APPLE__ */
  ```
  And then patch `cuda_gl_interop.h` header inside **CUDA**'s header directory using `sudo patch -N <header_file> <patch_file>` command.
  :::

  :::{Note}
  If there is a problem with **Eigen** header, make sure that it has been installed.
  If it has been installed, check the include directory of `Eigen/`, **OpenCV** expects that it is placed in the root. If it is placed in another directory _(example in `eigen3/Eigen/`)_, create symbolic link of that place to `Eigen/` using `ln -s <source_directory> <target_directory>` command.
  :::

## Post Install

### Configure OpenCV Library Path

- Create new file `opencv.conf` inside `/etc/ld.so.conf.d/` and fill it with the following text:
  ```
  /usr/local/lib
  ```
- Reload library path using `sudo ldconfig` command.

### Build OpenCV-python

- Install **OpenCV-python** using `pip`
  ``` sh
  ~$ sudo pip install opencv-python
  ```
