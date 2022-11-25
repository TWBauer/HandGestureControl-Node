#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
import cv2 
import mediapipe as mp
#import pyautogui
import time
from geometry_msgs.msg import Twist



def count_fingers(lst):
    cnt = 0

    thresh = (lst.landmark[0].y*100 - lst.landmark[9].y*100)/2

    if (lst.landmark[5].y*100 - lst.landmark[8].y*100) > thresh:
        cnt += 1

    if (lst.landmark[9].y*100 - lst.landmark[12].y*100) > thresh:
        cnt += 1

    if (lst.landmark[13].y*100 - lst.landmark[16].y*100) > thresh:
        cnt += 1

    if (lst.landmark[17].y*100 - lst.landmark[20].y*100) > thresh:
        cnt += 1

    if (lst.landmark[5].x*100 - lst.landmark[4].x*100) > 6:
        cnt += 1


    return cnt 


def talker():
    pub = rospy.Publisher('Gesture', Twist, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
    
        cap = cv2.VideoCapture(0)

        drawing = mp.solutions.drawing_utils
        hands = mp.solutions.hands
        hand_obj = hands.Hands(max_num_hands=1)


        start_init = False 

        prev = -1

        while True:
            hello_str = ""
            end_time = time.time()
            _, frm = cap.read()
            frm = cv2.flip(frm, 1)

            res = hand_obj.process(cv2.cvtColor(frm, cv2.COLOR_BGR2RGB))

            if res.multi_hand_landmarks:

                hand_keyPoints = res.multi_hand_landmarks[0]

                cnt = count_fingers(hand_keyPoints)

                if not(prev==cnt):
                    if not(start_init):
                        start_time = time.time()
                        start_init = True

                    elif (end_time-start_time) > 0.2:
                        if (cnt == 1):
                         
                            #hello_str = " derecha "
                            twist_msg = Twist()
                            twist_msg.linear.x=0
                            twist_msg.linear.y=0.0
                            twist_msg.linear.z=0.0
                            twist_msg.angular.x=0.0
                            twist_msg.angular.y=0.0
                            twist_msg.angular.z=-1
                            pub.publish(twist_msg)


                        elif (cnt == 2):
                            #pyautogui.press("left")
                            #hello_str = " izquierda"
                            twist_msg = Twist()
                            twist_msg.linear.x=0
                            twist_msg.linear.y=0.0
                            twist_msg.linear.z=0.0
                            twist_msg.angular.x=0.0
                            twist_msg.angular.y=0.0
                            twist_msg.angular.z=1
                            pub.publish(twist_msg)                            

                        elif (cnt == 3):
                            #pyautogui.press("up")
                            #hello_str = " atras "
                            twist_msg = Twist()
                            twist_msg.linear.x=-1
                            twist_msg.linear.y=0.0
                            twist_msg.linear.z=0.0
                            twist_msg.angular.x=0.0
                            twist_msg.angular.y=0.0
                            twist_msg.angular.z=0
                            pub.publish(twist_msg)

                        elif (cnt == 4):
                            #pyautogui.press("down")
                            #hello_str = " para "
                            twist_msg = Twist()
                            twist_msg.linear.x=0
                            twist_msg.linear.y=0.0
                            twist_msg.linear.z=0.0
                            twist_msg.angular.x=0.0
                            twist_msg.angular.y=0.0
                            twist_msg.angular.z=0.0
                            pub.publish(twist_msg)

                        elif (cnt == 5):
                            #pyautogui.press("space")
                            #hello_str = " adelante "
                            twist_msg = Twist()
                            twist_msg.linear.x=1
                            twist_msg.linear.y=0.0
                            twist_msg.linear.z=0.0
                            twist_msg.angular.x=0.0
                            twist_msg.angular.y=0.0
                            twist_msg.angular.z=0.0
                            pub.publish(twist_msg)
                        
                       #elif (cnt == 0):
                            #hello_str = " cero "

                        #prev = cnt
                        start_init = False


                


                drawing.draw_landmarks(frm, hand_keyPoints, hands.HAND_CONNECTIONS)

            cv2.imshow("window", frm)

            if cv2.waitKey(1) == 27:
                cv2.destroyAllWindows()
                cap.release()
                break

            #rospy.loginfo(hello_str)
            #pub.publish(hello_str)
            #rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass