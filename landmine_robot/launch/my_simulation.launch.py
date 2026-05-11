import os
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    # Path to the world file (adjust if necessary)
    world_file = '/home/roboticsproject/ros2_ws/src/landmine_robot/worlds/warzonevfinal.world'

    return LaunchDescription([
        Node(
            package='gazebo_ros',
            executable='gazebo',
            name='gazebo',
            output='screen',
            arguments=['--verbose', world_file]
        ),
        Node(
            package='turtlebot3_gazebo',
            executable='spawn_entity.py',
            name='spawn_turtlebot3',
            output='screen',
            arguments=['-file', '/opt/ros/humble/share/turtlebot3_gazebo/models/turtlebot3_burger/model.sdf', '-entity', 'turtlebot3']
        ),
    ])
