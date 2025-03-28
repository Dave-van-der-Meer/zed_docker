# zed_docker
Docker files to run the ZED camera with ROS 2

## Preparation

Make sure to follow the instructions from the [zed-ros2-wrapper](https://github.com/stereolabs/zed-ros2-wrapper) repository on GitHub to create the correct Docker image.
In short, you have to clone the repository:

```bash
git clone https://github.com/stereolabs/zed-ros2-wrapper.git
```

Then  enter the docker directory and build the image for the Jetson Orin Nano:

```bash
cd zed-ros2-wrapper/docker

# Jetson with JP6.0 and ZED SDK v4.2.3
./jetson_build_dockerfile_from_sdk_and_l4T_version.sh l4t-r36.3.0 zedsdk-4.2.3
```

**Hint**: find the Jetpack version of your Jetson using `sudo apt-cache show nvidia-jetpack`.

Once this is done, you can proceed with the instructions for using this repository.


## Useage

Clone the repository:

```bash
git clone https://github.com/Dave-van-der-Meer/zed_docker.git
```

Then, enter the folder called `docker` and run the package using Docker compose:

```bash
cd zed_docker/docker
docker compose up
```


This will automatically start the ZED2 camera with the `ROS_NAMESPACE` from the host.

Make sure the image name inside the `docker-compose.yaml` file matches the name of the Docker image that you created earlier.


## Convenience scripts

You can add the `-d` flag to run Docker compose in daemon mode, or simply run the `compose_up.sh` script.

The `docker-compose.yaml` file is configured to mount the `ros2_ws` directory as a volume. This allows you to change the parameters outside the Docker container.

The `docker-compose.yaml` file is configured to automatically restart after rebooting the device. This allows you to simply turn on the robot, and the camera will start without the need to log-in to the robot.

The modified `launch` files and `URDF` files are configured to provide a namespace to all the nodes, topics and TF links. At the moment, the namespace is hard-coded and shoudl be changed according to the user needs.
