## ROS2 service wrapper around [SpaTiaL](https://github.com/KTH-RPL-Planiacs/SpaTiaL)
This package wraps the SpaTial reasoning framework for use in [CoreSense](https://coresense.eu).

### Dependencies
This package depends on `spatial_spec`, a python package available via pypi.
1. Create and activate a virtual environment as described by the [ROS2 Guide](https://docs.ros.org/en/foxy/How-To-Guides/Using-Python-Packages.html#installing-via-a-virtual-environment)
2. install dependency:
```shell
python3 -m pip install spatial-spec
```
### Build
1. build: 
```shell
colcon build --packages-select coresense_spatial
```
2. source: 
```shell
. install/local_setup.zsh
```
### Run
```shell
ros2 run coresense_spatial spatial
```
