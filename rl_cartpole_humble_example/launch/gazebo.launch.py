
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node


# generate launch description file
def generate_launch_description():
    package_name = 'rl_cartpole_humble_example'
    share_dir = get_package_share_directory(package_name)
    world_file = os.path.join(share_dir, 'worlds', 'my_world.sdf')
    robot_file = os.path.join(share_dir, 'urdf', 'my_robot.urdf')

    return LaunchDescription([
        Node(
            package='ignition_gazebo',
            executable='ignition',
            arguments=['gazebo', '-v', '4', world_file],
            output='screen'
        ),

        Node(
            package='ignition_gazebo_ros',
            executable='ignition_gazebo_ros',
            arguments=['urdf_publisher', '-v', '4', robot_file],
            output='screen'
        )
    ])
