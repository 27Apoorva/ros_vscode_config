from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="ros2_cpp_pkg", 
            executable="publisher",
            name="publisher_node",
            parameters=[
            ]
        ),
    ])
