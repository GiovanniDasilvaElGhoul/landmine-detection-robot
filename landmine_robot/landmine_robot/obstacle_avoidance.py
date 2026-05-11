import rclpy
from rclpy.node import Node
from sensor_msgs.msg import LaserScan
from geometry_msgs.msg import Twist
import math
import random


class Explorer(Node):

    def __init__(self):
        super().__init__('explorer')

        self.scan_sub = self.create_subscription(
            LaserScan,
            '/scan',
            self.scan_callback,
            10)

        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)

        self.timer = self.create_timer(0.1, self.control_loop)

        self.scan_data = None

        self.obstacle_threshold = 0.7
        self.forward_speed = 0.2
        self.turn_speed = 0.8

        self.random_turn_timer = 0

      
        self.obstacle_detected = False

    def scan_callback(self, msg):
        self.scan_data = msg

    def control_loop(self):

        if self.scan_data is None:
            return

        ranges = list(self.scan_data.ranges)
        size = len(ranges)

        if size == 0:
            return

        mid = size // 2

        # Front sector (180° LiDAR)
        front_sector = ranges[mid - 15: mid + 15]

        
        front_sector = [r if not math.isinf(r) else 10.0 for r in front_sector]

        min_front = min(front_sector)

        twist = Twist()


        if min_front < self.obstacle_threshold:

            
            if not self.obstacle_detected:
                self.get_logger().info("⚠️ Obstacle detected")
                self.obstacle_detected = True

            twist.linear.x = 0.0
            twist.angular.z = self.turn_speed

            self.random_turn_timer = 0

        else:
   
            self.obstacle_detected = False


            if self.random_turn_timer <= 0:
                if random.random() < 0.05:
                    self.random_turn_timer = random.uniform(1.0, 2.0)
                    twist.linear.x = 0.0
                    twist.angular.z = random.choice([-1.0, 1.0])
                else:
                    twist.linear.x = self.forward_speed
                    twist.angular.z = 0.0
            else:
                twist.linear.x = 0.0
                twist.angular.z = random.choice([-1.0, 1.0])
                self.random_turn_timer -= 0.1

        self.cmd_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = Explorer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
