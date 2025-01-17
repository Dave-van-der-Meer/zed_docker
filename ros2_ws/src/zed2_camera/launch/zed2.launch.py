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
from launch.actions import LogInfo


ROBOT_NAMESPACE = None
try:
    ROBOT_NAMESPACE = os.environ['ROS_NAMESPACE']
except Exception as e:
    print(e)
    ROBOT_NAMESPACE = ""

CAMERA_NAME = "zed2"
if ROBOT_NAMESPACE != "":
    CAMERA_NAME = f"{ROBOT_NAMESPACE}/{CAMERA_NAME}"


def generate_launch_description():

    # Camera model (force value)
    camera_model = 'zed2' # Included in the config file
    camera_name = CAMERA_NAME

    config = os.path.join(
        get_package_share_directory('zed2_camera'),
        'config',
        'common.yaml'
        )

    # ZED Wrapper node
    zed_wrapper_launch = IncludeLaunchDescription(
        launch_description_source=PythonLaunchDescriptionSource([
            get_package_share_directory('zed_wrapper'),
            '/launch/zed_camera.launch.py'
        ]),
        launch_arguments={
            'camera_model': camera_model,
            'camera_name': camera_name,
            # 'publish_map_tf': 'false',
            # 'publish_tf': 'false',
            # 'depth_mode': 'NONE',
            'config_path': config,
        }.items()
    )


    # OBSOLETE Warning
    # warning_0 = LogInfo(msg='============================================================================================================')
    # warning_1 = LogInfo(msg=' !!! WARNING !!! This launch file is obsolete and it will be removed in the next release.')
    # warning_2 = LogInfo(msg=' Please use \"ros2 launch zed_wrapper zed_camera.launch.py camera_model:=\'zed2\' camera_name:=\'zed\'\" instead.')
    # warning_3 = LogInfo(msg='============================================================================================================')
    
    # Define LaunchDescription variable
    ld = LaunchDescription()
    
    # Add nodes to LaunchDescription
    # ld.add_action(warning_0)
    # ld.add_action(warning_1)
    # ld.add_action(warning_2)
    # ld.add_action(warning_3)
    ld.add_action(zed_wrapper_launch)

    return ld
