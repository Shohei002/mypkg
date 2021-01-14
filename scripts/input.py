#!/usr/bin/env python3

import rospy
from std_msgs.msg import String

rospy.init_node('input')
pub = rospy.Publisher('input', String, queue_size=1)
while not rospy.is_shutdown():
    str = input("アルファベットを入力してください:")
    pub.publish(str)
