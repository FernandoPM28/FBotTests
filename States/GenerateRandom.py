import smach
import rospy
import random

class RandomNumber(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded', 'aborted', 'preempted'])
        
        self.value = 0

    def execute(self, userdata):

        self.value = random.randint(1, 10)

        if self.preempt_requested():
            return 'preempted'

        if self.value > 5:
            return 'succeeded'
        
        return 'aborted'

    def request_preempt(self):
        super().request_preempt()