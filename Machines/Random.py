import rospy
import smach

from States import GenerateRandom, PrintLess, PrintMore

if __name__ == '__main__':
    rospy.init_node('test')
    sm = smach.StateMachine(outcomes=['succeeded', 'aborted', 'preempted'])
    with sm:
        smach.StateMachine.add("GET_RANDOM_NUMBER", GenerateRandom(),
        transitions={
        "succeeded": "PRINT_MORE",
        "aborted": "PRINT_LESS",
        "preempted": "preempted"
        }),
        smach.StateMachine.add("PRINT_LESS", PrintLess(),
        transitions={
        "succeeded": "succeeded",
        "preempted": "preempted"
        }),
        smach.StateMachine.add("PRINT_MORE", PrintMore(),
        transitions={
        "succeeded": "succeeded",
        "preempted": "preempted"
        })

    outcome = sm.execute()