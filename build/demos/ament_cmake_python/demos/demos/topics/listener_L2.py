#! /usr/bin/env python3
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import Int32, String


class ListenerL2(Node):
    def __init__(self):
        super().__init__("listener_L2")

        self.sub_t1 = self.create_subscription(
            Int32, "T1", self.callback_t1, 10
        )

        self.sub_t2 = self.create_subscription(
            String, "T2", self.callback_t2, 10
        )

    def callback_t1(self, msg):
        self.get_logger().info("L2 heard from T1: [%s]" % msg.data)

    def callback_t2(self, msg):
        self.get_logger().info("L2 heard from T2: [%s]" % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = ListenerL2()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()