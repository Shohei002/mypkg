#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def cb(message):
    char = message.data
    print(char.upper())

rospy.init_node('output_up')
sub = rospy.Subscriber('input', String, cb)
rospy.spin()
