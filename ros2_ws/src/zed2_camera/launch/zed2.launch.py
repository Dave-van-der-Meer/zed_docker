## This file has been taken from the zed_wrapper package to be modified for this study.

# Copyright 2022 Stereolabs
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

ROBOT_NAMESPACE = None
try:
    ROBOT_NAMESPACE = os.environ['ROS_NAMESPACE']
except Exception as e:
    print(e)
    ROBOT_NAMESPACE = ""

def generate_launch_description():

    # Camera model (force value)
    camera_model = 'zed2' # Included in the config file
    camera_name = "zed2"

    config = os.path.join(
        get_package_share_directory('zed2_camera'),
        'config',
        'common.yaml'
        )

    namespace_argument = DeclareLaunchArgument(
        'namespace', default_value=ROBOT_NAMESPACE, description='Namespace for the robot'
        )

    # ZED Wrapper node
    zed_wrapper_launch = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource([
            get_package_share_directory('zed2_camera'),
            '/launch/zed_camera.launch.py'
        ]),
        launch_arguments={
            'namespace': LaunchConfiguration('namespace'),
            'camera_model': camera_model,
            'camera_name': camera_name,
            # 'publish_map_tf': 'false',
            # 'publish_tf': 'false',
            # 'depth_mode': 'NONE',
            'config_path': config,
        }.items()
    )


    # Define LaunchDescription variable
    ld = LaunchDescription()

    # Add nodes to LaunchDescription
    ld.add_action(namespace_argument)
    ld.add_action(zed_wrapper_launch)

    return ld
