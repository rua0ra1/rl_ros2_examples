import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from pathlib import Path

def generate_launch_description():
    # Get path to the URDF file
    package_name = 'rl_cart_pole_example'
    urdf_file = os.path.join(get_package_share_directory(package_name), 'urdf', 'my_robot.urdf')

    # Load robot model in Gazebo
    robot_state_publisher_node = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'my_robot', '-file', urdf_file],
        output='screen'
    )

    # Launch Gazebo
    gazebo_node = Node(
        package='gazebo_ros',
        executable='gazebo',
        arguments=['-s', 'libgazebo_ros_init.so', '-s', 'libgazebo_ros_factory.so'],
        output='screen'
    )

    return LaunchDescription([
        robot_state_publisher_node,
        gazebo_node
    ])
