#! /usr/bin/env python3
import rclpy
import random
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import Int32


class TalkerT1(Node):
    def __init__(self):
        super().__init__("talker_T1")
        self.pub = self.create_publisher(Int32, "T1", 10)
        self.tmr = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = Int32()
        msg.data = random.randint(0, 100)
        self.get_logger().info('Publishing T1: "%s"' % msg.data)
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = TalkerT1()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()