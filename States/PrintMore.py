import smach
import rospy

class RandomNumber(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['succeeded', 'preempted'])

    def execute(self, userdata):

        if self.preempt_requested():
            return 'preempted'

        print("Valor maior que 5")
        
        return 'succeeded'
        
    def request_preempt(self):
        super().request_preempt()