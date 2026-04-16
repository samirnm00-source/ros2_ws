#! /usr/bin/env python3
import rclpy
import random
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node
from std_msgs.msg import String

class Talker(Node):
    def __init__(self):
        super().__init__("talker_T1")
        self.i = 0
        self.pub = self.create_publisher(String, "T1", 10)
        timer_period = 1.0
        self.tmr = self.create_timer(timer_period, self.timer_callback)

    def timer_callback(self):
        msg = String()
        msg.data = "Hello robotics students: {0}".format(self.i)
        self.i += 1
        self.get_logger().info('Publishing: "{0}"'.format(msg.data))
        self.pub.publish(msg)


def main(args=None):
    rclpy.init(args=args)

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import rclpy
from rclpy.executors import ExternalShutdownException
from rclpy.node import Node

from std_msgs.msg import String


class Listener(Node):
    node = Talker()

    try:
        rclpy.spin(node)
    except (KeyboardInterrupt, ExternalShutdownException):
        pass
    finally:
        node.destroy_node()
        rclpy.try_shutdown()


if __name__ == "__main__":
    main()
