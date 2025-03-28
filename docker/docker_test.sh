#!/usr/bin/env bash

if [ ${#} -lt 1 ]; then
    #echo "Usage: ${0} <docker image> <cmd (optional)>"
    #exit 1
    IMG="zed_ros2_l4t_36.3.0_sdk_4.2.3"
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
    --runtime nvidia
    --security-opt "seccomp=unconfined"
    # --volume "/etc/localtime:/etc/localtime:ro"
    --volume "/dev:/dev"
    --volume "/dev/shm:/dev/shm"
    --volume "/tmp/.X11-unix/:/tmp/.X11-unix"
    --volume "/usr/local/zed/resources:/usr/local/zed/resources"
    # --volume "${PWD}/../ros2_ws/src/zed2_camera:/root/ros2_ws/src/zed2_camera"
    --volume "${PWD}/../ros2_ws/src/zed2_camera:/root/ros2_ws/src/zed2_camera"
    --env ROS_NAMESPACE=${ROS_NAMESPACE}
    --env ROS_DOMAIN_ID=${ROS_DOMAIN_ID}
    --env ROS_LOCALHOST_ONLY=${ROS_LOCALHOST_ONLY}
    --name "zed_leo"
    "${IMG}"
    "${CMD}"
)

echo -e "\033[1;30m${DOCKER_RUN_CMD[*]}\033[0m" | xargs

# shellcheck disable=SC2048
exec ${DOCKER_RUN_CMD[*]}


docker run
-v /usr/local/zed/settings:/usr/local/zed/settings
-v "${PWD}/../ros2_ws/src/zed2_camera:/root/ros2_ws/src/zed2_camera"
