from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument

def generate_launch_description():
    return LaunchDescription([
        # Declare arguments for the map and other configurations
        DeclareLaunchArgument('use_sim_time', default_value='true'),
        
        # Cartographer SLAM node
        Node(
            package='cartographer_ros',
            executable='cartographer_node',
            output='screen',
            parameters=[{'use_sim_time': True}, '/home/roboticsproject/ros2_ws/src/my_tb3_launch/config/costmap_common_params.yaml'],  # Update with actual config path
            remappings=[('/scan', '/scan')]
        ),

        # Map server node (to use with RViz)
        Node(
            package='ros2_navigation',
            executable='map_server',
            name='map_server',
            output='screen',
            parameters=[{'use_sim_time': True}],
            remappings=[('/map', '/map')]
        ),

        # Load the costmap parameters for the robot to consider static obstacles (mines)
        Node(
            package='ros2_navigation',
            executable='costmap_2d',
            name='costmap_2d',
            output='screen',
            parameters=[{'use_sim_time': True}, '/path/to/costmap_common_params.yaml'],  # Update with the path to costmap YAML
        )
    ])
