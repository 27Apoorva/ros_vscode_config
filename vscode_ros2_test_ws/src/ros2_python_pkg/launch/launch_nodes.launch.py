from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        Node(
            package="my_ros2_python_pkg", 
            executable="talker",
            name="talker_node",
            parameters=[
            ]
        ),
        Node(
            package="my_ros2_python_pkg", 
            executable="listener",
            name="listener_node",
            parameters=[
            ]
        ),
    ])