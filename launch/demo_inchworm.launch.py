import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch.actions import DeclareLaunchArgument
from launch_ros.actions import Node


def generate_launch_description():
#this is technology 
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    urdf_file_name = 'one_inchworm.urdf'
    urdf = os.path.join(
        get_package_share_directory('urdf_tutorial_r2d2'),
        urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='false',
            description='Use simulation (Gazebo) clock if true'),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': use_sim_time, 'robot_description': robot_desc}],
            arguments=[urdf]),
        Node(
            package='urdf_tutorial_r2d2',
            executable='state_publisher',
            name='state_publisher',
            output='screen'),
    ])


# <!-- Spawn the robot sdf into the sim -->
#   <node name="spawn_scene" pkg="gazebo_ros" type="spawn_model" args="-param $(arg model)/robot_description_sdf -sdf -model $(arg model)" output="screen" />

#   <!-- Publishes world -> iw_root transform. -->
#   <node name="iw_tf_republisher" pkg="inchworm_description" type="iw_tf_republisher.py" />

#   <!-- Informs the assembly sim about magnet states. -->
#   <node name="magnet_state_observer" pkg="inchworm_description" type="magnet_state_observer.py" output="screen" />

#   <!-- Startup RViz-->
#   <node name="rviz" pkg="rviz" type="rviz" args="-d $(find inchworm_description)/rviz/inchworm_frames.rviz" if="$(arg rviz)"/>
