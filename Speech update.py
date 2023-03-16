#!/usr/bin/env python
import sys
import rospy
from std_msgs.msg import String
from difflib import SequenceMatcher
from SoundsLike.SoundsLike import Search
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient

A_name = ["Sharon", "John", "Betty"]

#rosrun sound_play say.py "Hello World"
def callback(data):
    # Ordered this way to minimize wait time.
    rospy.init_node('say', anonymous=True)
    soundhandle = SoundClient()
    rospy.sleep(1)
    a = 0
    voice = 'voice_kal_diphone'
    volume = 1.0
    
    argv = rospy.myargv()


    if len(argv) == 1:
        s = sys.stdin.read()
    else:
        s = argv[1]

        if len(argv) > 2:
            voice = argv[2]
        if len(argv) > 3:
            volume = float(argv[3])
    name = Search.closeHomophones(data.data)
    for i in range(len(name)):
    	s = SequenceMatcher(None, name[i], A_name[i]).ratio()
    	if s > (0.75):
    		rospy.loginfo('Hello there %s', A_name[i])
    		soundhandle.say(('Hello there %s', A_name[i]), voice, volume)
    		rospy.sleep(1)
    		a = 1
    	if (a == 0):
    		rospy.loginfo('I did not catch that')
    		soundhandle.say('I did not catch that', voice, volume)  


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
