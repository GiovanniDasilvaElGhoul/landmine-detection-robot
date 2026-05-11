import rclpy
from rclpy.node import Node
from visualization_msgs.msg import Marker
from geometry_msgs.msg import Point
from std_msgs.msg import Header

class MineMarkerPublisher(Node):
    def __init__(self):
        super().__init__('mine_marker_publisher')
        self.marker_pub = self.create_publisher(Marker, 'visualization_marker', 10)
        self.timer = self.create_timer(1.0, self.publish_marker)  # Publish every 1 second

    def publish_marker(self):
        # Create the marker for the mine
        marker = Marker()
        marker.header = Header()
        marker.header.frame_id = "map"
        marker.header.stamp = self.get_clock().now().to_msg()

        marker.ns = "mines"
        marker.id = 0  # Unique ID for the mine
        marker.type = Marker.CYLINDER  # Use CYLINDER for visualization
        marker.action = Marker.ADD
        marker.pose.position = Point(x=3.0, y=2.0, z=0.0)  # Coordinates where the mine is
        marker.scale.x = 0.2  # Radius of the mine
        marker.scale.y = 0.2
        marker.scale.z = 0.1  # Height (for disk shape)
        marker.color.a = 1.0  # Transparency
        marker.color.r = 1.0  # Red color for mines

        # Publish the marker
        self.marker_pub.publish(marker)

def main(args=None):
    rclpy.init(args=args)
    mine_marker_publisher = MineMarkerPublisher()
    rclpy.spin(mine_marker_publisher)
    mine_marker_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
