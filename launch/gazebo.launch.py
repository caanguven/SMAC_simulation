import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Replace 'urdf_tutorial_r2d2' with the name of your package if different
    package_dir = get_package_share_directory('urdf_tutorial_r2d2')

    urdf_file_name = 'one_inchworm.urdf'
    urdf = os.path.join(package_dir, urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    # Set the GAZEBO_MODEL_PATH environment variable
    os.environ['GAZEBO_MODEL_PATH'] = os.path.join(
        package_dir, 'urdf'
    ) + ':' + os.environ.get('GAZEBO_MODEL_PATH', '')

    return LaunchDescription([
        # Start Gazebo with an empty world
        Node(
            package='gazebo_ros',
            executable='gzserver',
            arguments=['--verbose', '-s', 'libgazebo_ros_factory.so'],
            output='screen'
        ),
        Node(
            package='gazebo_ros',
            executable='gzclient',
            output='screen'
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': robot_desc}]
        ),
        Node(
            package='gazebo_ros',
            executable='spawn_entity.py',
            arguments=['-entity', 'one_inchworm', '-topic', 'robot_description'],
            output='screen'
        )
    ])
