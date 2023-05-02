import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory('rl_cartpole_humble_example'),
        'urdf',
        'robot.urdf'
    )
    spawn_entity = Node(
        package='gazebo_ros',
        executable='spawn_entity.py',
        arguments=['-entity', 'rl_cartpole', '-file', urdf_file],
        output='screen',
    )

    return LaunchDescription([
        spawn_entity
    ])