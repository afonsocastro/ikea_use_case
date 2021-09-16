#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import time


def callback_pick_object(data):
    # pub = rospy.Publisher('object_picked', String, queue_size=10)

    global_state = rospy.get_param("/state")
    # print(global_state)

    if global_state == "picking_object":
        print("Going to grab the object...")
        rospy.sleep(5)  # time that it takes to pick the object up
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        is_object_picked = "object caught at " + str(current_time)
        print(is_object_picked)
        # pub.publish(is_object_picked)
        rospy.set_param("/state", "approaching_human")


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.

    rospy.init_node('object_picker', anonymous=False)
    rospy.Subscriber("trackers/object_pose", String, callback_pick_object)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()

