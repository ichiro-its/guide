# YOLO Setup

## Clone YOLO Repository

- Clone this repository `https://github.com/pjreddie/darknet`.

## Build YOLO

- Inside `Makefile` in the **YOLO** repository, modify the `GPU`, `CUDNN`, and `OPENCV` parameter into `1` using `sed`.
  ``` sh
  ~$ sudo sed -i 's/GPU=0/GPU=1/g' Makefile
  ~$ sudo sed -i 's/CUDNN=0/CUDNN=1/g' Makefile
  ~$ sudo sed -i 's/OPENCV=0/OPENCV=1/g' Makefile
  ```
- Build **YOLO** with `make -j` command.
