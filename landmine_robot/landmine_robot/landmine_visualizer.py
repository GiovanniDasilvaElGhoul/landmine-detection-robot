import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point

class LandmineVisualizer(Node):
    def __init__(self):
        super().__init__('landmine_visualizer')

        # Publisher for the markers
        self.publisher = self.create_publisher(Marker, '/landmine_markers', 10)

        # Predefined landmine coordinates
        self.mines = [(0, 3), (-2, 1), (3, -1), (-4, 2), (5, 0), (-3, -3), (2, -4)]

        # Timer to publish markers every 1 second
        self.timer = self.create_timer(1.0, self.publish_landmines)

    def publish_landmines(self):
        # Create the Marker message
        marker = Marker()
        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()
        marker.ns = "landmines"
        marker.id = 0
        marker.type = Marker.SPHERE_LIST
        marker.action = Marker.ADD
        marker.pose.orientation.w = 1.0
        marker.scale.x = 0.2
        marker.scale.y = 0.2
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 1.0  # Red color for landmines
        marker.color.g = 0.0
        marker.color.b = 0.0

        # Add landmine positions as points
        for (x, y) in self.mines:
            point = Point()
            point.x = float(x)  # Ensure that x is a float
            point.y = float(y)  # Ensure that y is a float
            point.z = 0.1  # Place the landmine a little above the ground
            marker.points.append(point)

        # Publish the markers
        self.publisher.publish(marker)

def main(args=None):
    rclpy.init(args=args)
    visualizer = LandmineVisualizer()
    rclpy.spin(visualizer)
    visualizer.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
