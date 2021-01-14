#!/usr/bin/env python3
import rospy
from std_msgs.msg import String


def cb(message):
    char = message.data
    print(char.lower())

rospy.init_node('output_low')
sub = rospy.Subscriber('input', String, cb)
rospy.spin()
