#! /usr/bin/env python3
import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String


class ListenerL3(Node):
    def __init__(self):
        super().__init__("listener_L3")
        self.sub = self.create_subscription(
            String, "T2", self.callback_t2, 10
        )

    def callback_t2(self, msg):
        self.get_logger().info("L3 heard from T2: [%s]" % msg.data)


def main(args=None):
    rclpy.init(args=args)

    node = ListenerL3()
    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()