#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from difflib import SequenceMatcher

def callback(data):
	s = SequenceMatcher(None, data.data , "b s one six one z h").ratio()
	
	if (s > 0.75):
		rospy.loginfo('Hang on ive got this')
		rospy.Sleep()
		rospy.loginfo('You said %s' + ' did you mean to say Hello', data.data)
	
	elif ( s > 0.50 and s < 0.75):
		rospy.loginfo('You said %s' + ' did you mean to say Hello', data.data)
	elif (s < 0.50):
		rospy.loginfo('I did not catch that')

def listenToSpeech():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listenToSpeech', anonymous=True)

    rospy.Subscriber('/speech_recognition/final_result', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listenToSpeech()
