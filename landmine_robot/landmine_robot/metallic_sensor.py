import rclpy
from rclpy.node import Node
from nav_msgs.msg import Odometry
import math
import os
import threading


class GPRDetector(Node):

    def __init__(self):
        super().__init__('metallic_sensor')

        # Subscribe to robot position
        self.subscription = self.create_subscription(
            Odometry,
            '/odom',
            self.odom_callback,
            10
        )

        # 💣 ALL MINE COORDINATES (match your world file)
        self.mines = [
            (0, 3),      # Metal mines
            (-2, 1),
            (3, -1),
            (-4, 2),
            (5, 0),
            (-3, -3),
            (2, -4),
        ]

        # 🪵 ALL WOODEN PEG COORDINATES (match your world file)
        self.wooden_pegs = [
            (-1, -2),    # Wooden pegs
            (1, -3),
            (3, 2),
        ]

        # Detection radius (meters)
        self.detection_radius = 0.8

        # Keep track of detected mines and wooden pegs
        self.detected_mines = set()
        self.detected_wooden_pegs = set()

        # 🔊 Path to beep sound
        self.sound_path = os.path.join(
            os.path.dirname(__file__),
            'beep.wav'
        )

        self.get_logger().info("Metallic Sensor Node 🚀")

    def play_beep(self):
        os.system('powershell.exe -Command "[console]::beep(1000,300)"')

    def odom_callback(self, msg):

        robot_x = msg.pose.pose.position.x
        robot_y = msg.pose.pose.position.y

        # --- Check for mines ---
        for i, (mine_x, mine_y) in enumerate(self.mines):

            distance = math.sqrt(
                (robot_x - mine_x) ** 2 +
                (robot_y - mine_y) ** 2
            )

            if distance < self.detection_radius:

                # Detect only once per mine
                if i not in self.detected_mines:

                    self.get_logger().info(
                        f"💣 MINE {i+1} DETECTED at ({mine_x}, {mine_y})"
                    )

                    # 🔊 Play sound in separate thread
                    threading.Thread(
                        target=self.play_beep,
                        daemon=True
                    ).start()

                    self.detected_mines.add(i)

        # --- Check for wooden pegs ---
        for i, (peg_x, peg_y) in enumerate(self.wooden_pegs):

            distance = math.sqrt(
                (robot_x - peg_x) ** 2 +
                (robot_y - peg_y) ** 2
            )

            if distance < self.detection_radius:

                # Detect only once per wooden peg
                if i not in self.detected_wooden_pegs:

                    self.get_logger().info(
                        f"🪵 WOODEN PEG {i+1} DETECTED at ({peg_x}, {peg_y})"
                    )

                    self.detected_wooden_pegs.add(i)


def main(args=None):
    rclpy.init(args=args)
    node = GPRDetector()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
