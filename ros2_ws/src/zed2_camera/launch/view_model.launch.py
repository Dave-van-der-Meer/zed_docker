import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.substitutions import LaunchConfiguration, Command, TextSubstitution
from launch.conditions import IfCondition
from launch_ros.actions import Node


# URDF/xacro file to be loaded by the Robot State Publisher node
default_xacro_path = os.path.join(
    get_package_share_directory('zed2_camera'),
    'urdf',
    'zed2_camera_rig.urdf.xacro'
)

def launch_setup(context, *args, **kwargs):
    camera_name = 'zed2' #LaunchConfiguration('camera_name')
    camera_model = camera_name #LaunchConfiguration('camera_model')

    node_name = camera_name #LaunchConfiguration('node_name')

    publish_urdf = True #LaunchConfiguration('publish_urdf')
    xacro_path = default_xacro_path# LaunchConfiguration('xacro_path')

    camera_name_val = camera_name #.perform(context)
    camera_model_val = camera_model #.perform(context)

    robot_state_publisher = Node(
        package='robot_state_publisher',
        namespace=camera_name_val,
        executable='robot_state_publisher',
        name='zed_state_publisher',
        output='screen',
        parameters=[{
            'robot_description': Command(
                [
                    'xacro', ' ', xacro_path, ' ',
                    'camera_name:=', camera_name_val, ' ',
                    'camera_model:=', camera_model_val, ' '
                ])
        }]
    )
    return [robot_state_publisher]

def generate_launch_description():

    return LaunchDescription([

    # DeclareLaunchArgument(
    #             'publish_tf',
    #             default_value='true',
    #             description='Enable publication of the \
    #                         `odom -> camera_link` TF.',
    #             choices=['true', 'false']),

    DeclareLaunchArgument(
                'camera_name',
                default_value=TextSubstitution(text="zed2"),
                description='The name of the camera. \
                             It can be different from the camera \
                             model and it will be used as node `namespace`.'),

    OpaqueFunction(function=launch_setup)
    ])
