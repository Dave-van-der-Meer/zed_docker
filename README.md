# zed_docker
Docker files to run the ZED camera with ROS 2

## Use

Clone the repository. Then, enter the folder called `docker` and build the Dockerfile for the corresponding platform.

For Desktop Computers with AMD or Intel CPU, use:

```bash
cd zed_docker/docker
bash docker_build_x86.sh
```

For NVIDIA Jetson devices like the Jetson Xavier or the Jetson Orin, use:

```bash
cd zed_docker/docker
bash docker_build_arm.sh
```

Then, after the build has been completed, use the following line to run a Docker container in the background:

```bash
bash docker_run.sh
```

This will automatically start the ZED2 camera with the `ROS_NAMESPACE` from the host.
