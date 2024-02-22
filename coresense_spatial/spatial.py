import rclpy
from rclpy.node import Node

from spatial_spec.logic import Spatial

class SpatialService(Node):

    def __init__(self):
        super().__init__('spatial')
        self.spatial = Spatial()
        #self.subscription = self.create_subscription(
        #    UpdateMessageClass,
        #    'update_message_topic',
        #    self.object_update_callback,
        #    10)
        #self.subscription  # prevent unused variable warning
        #self.srv = self.create_service(ServiceInterfaceClass, 'spatial', self.spatial_callback)

    def object_update_callback(self, msg):
        self.get_logger().info('I heard: "%s"' % msg.data)

    def spatial_callback(self, request, response):
        #response.sum = request.a + request.b
        #self.get_logger().info('Incoming request\na: %d b: %d' % (request.a, request.b))

        return response


def main():
    rclpy.init()

    spatial_service = SpatialService()

    rclpy.spin(spatial_service)
    spatial_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
