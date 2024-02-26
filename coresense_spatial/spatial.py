import numpy as np

import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

from coresense_msgs.srv import GetObjectRelation
from coresense_msgs.msg import ObjectUpdate
from spatial_spec.logic import Spatial
from spatial_spec.geometry import Polygon, PolygonCollection, StaticObject, IColor


class SpatialService(Node):

    def __init__(self):
        super().__init__('spatial')
        self.spatial = Spatial()
        self.objects = {}

        self.subscription = self.create_subscription(
            ObjectUpdate,
            'update_message_topic',
            self.object_update_callback,
            10)
        self.subscription  # prevent unused variable warning
        self.srv = self.create_service(GetObjectRelation, 'spatial_relation', self.spatial_callback)

    def object_update_callback(self, msg: ObjectUpdate):
        self.get_logger().info('I heard: "%s"' % msg)
        np_array = []
        for p in msg.polygon.points:
            np_array.append([p.x, p.y])
        #TODO: object permanence, i.e. identification, uids, DynamicObject
        obj = StaticObject(PolygonCollection({Polygon(vertices=np.array(np_array, np.float32), color=IColor.N, convex_hull=True)}))
        self.spatial.assign_variable(msg.uid, obj)
        self.objects[msg.uid] = obj


    def spatial_callback(self, request, response):
        self.get_logger().info('Incoming request\na: %s' % request.formula)
        value = self.spatial.parse_and_interpret(request.formula)
        self.get_logger().info('Response is: %d' % value)
        response.value = float(value)
        return response

    def rectangle_around_center(center: np.ndarray, box_length1: float, box_length2: float) -> np.ndarray:
        return np.array(
            [center + [-box_length1 / 2, -box_length2 / 2],
             center + [box_length1 / 2, -box_length2 / 2],
             center + [box_length1 / 2, box_length2 / 2],
             center + [-box_length1 / 2, box_length2 / 2]])


def main():
    rclpy.init()

    spatial_service = SpatialService()

    rclpy.spin(spatial_service)
    spatial_service.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
