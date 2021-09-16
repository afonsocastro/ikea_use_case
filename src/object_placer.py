#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time


def callback_place_object(data):
    # pub = rospy.Publisher('object_picked', String, queue_size=10)

    global_state = rospy.get_param("/state")
    # print(global_state)

    if global_state == "object_placing":
        print("hearing the decision...")
        print("the decision was" + data.data)
        print("placing the object...")
        rospy.sleep(5)  # time that it takes to place the object
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        is_object_placed = "object placed at " + str(current_time)
        print(is_object_placed)
        # pub.publish(is_object_picked)
        rospy.set_param("/state", "picking_object")


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.init_node('object_placer', anonymous=False)
    rospy.Subscriber("decision", String, callback_place_object)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()

