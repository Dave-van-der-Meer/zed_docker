#!/usr/bin/env bash

if [ ${#} -lt 1 ]; then
    #echo "Usage: ${0} <docker image> <cmd (optional)>"
    #exit 1
    IMG="local/zed:humble"
    CMD="bash"

fi

ENVS="--env ROS_NAMESPACE=${ROS_NAMESPACE}"
if [ -n "${ROS_DOMAIN_ID}" ]; then
    ENVS="${ENVS} --env ROS_DOMAIN_ID=${ROS_DOMAIN_ID}"
fi
if [ -n "${ROS_LOCALHOST_ONLY}" ]; then
    ENVS="${ENVS} --env ROS_LOCALHOST_ONLY=${ROS_LOCALHOST_ONLY}"
fi

DOCKER_RUN_CMD=(
    docker run
    --interactive
    --tty
    --network host
    --ipc host
    --pid host
    --rm
    --privileged
    --gpus all # replaces --runtime nvidia
    --security-opt "seccomp=unconfined"
    --volume "/etc/localtime:/etc/localtime:ro"
    --volume "/dev:/dev"
    --volume "/dev/shm:/dev/shm"
    --volume "/tmp/.X11-unix/:/tmp/.X11-unix"
    --volume "/tmp/zed_ai/:/usr/local/zed/resources/"
    --volume "${PWD}/../ros2_ws/src/zed2_camera:/root/ros2_ws/src/zed2_camera"
    --env ROS_NAMESPACE=${ROS_NAMESPACE}
    --env ROS_DOMAIN_ID=${ROS_DOMAIN_ID}
    --env ROS_LOCALHOST_ONLY=${ROS_LOCALHOST_ONLY}
    --env FASTRTPS_DEFAULT_PROFILES_FILE=/root/.ros/ddsconfig/fastdds.xml
    --env RMW_IMPLEMENTATION=rmw_fastrtps_cpp
    --name "leo_zed"
    "${IMG}"
    "${CMD}"
)

echo -e "\033[1;30m${DOCKER_RUN_CMD[*]}\033[0m" | xargs

# shellcheck disable=SC2048
exec ${DOCKER_RUN_CMD[*]}
