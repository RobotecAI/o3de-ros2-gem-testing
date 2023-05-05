import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription

import launch_ros.actions
import launch_ros.descriptions
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # launch plugin through rclcpp_components container
        launch_ros.actions.ComposableNodeContainer(
            name='container0',
            namespace='',
            package='rclcpp_components',
            executable='component_container',
            composable_node_descriptions=[
                launch_ros.descriptions.ComposableNode(
                    package='depth_image_proc',
                    plugin='depth_image_proc::PointCloudXyzrgbNode',
                    name='point_cloud_xyzrgb_node',
                    remappings=[('rgb/camera_info', '/FooCameraTest/aligned_depth_to_color/camera_info'),
                                ('rgb/image_rect_color', '/FooCameraTest/color/image_raw'),
                                ('depth_registered/image_rect','/FooCameraTest/aligned_depth_to_color/image_raw'),
                                ('/points','/FooCameraTest/pointcloud')]
                ),
            ],
            output='screen',
            parameters=[{'use_sim_time': True}],
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz',
            output='screen',
            arguments=['-d', [os.path.join(os.path.dirname(__file__), 'point_cloud_xyzrgb.rviz')]],
            parameters=[{'use_sim_time': True}],
        )
    ])
