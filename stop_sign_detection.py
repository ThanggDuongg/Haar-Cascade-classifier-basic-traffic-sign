from tkinter import W
from turtle import distance
import cv2

#variables
#distance from camera to object(traffic sign) measured
know_distacne = 30 #cm
#width of traffic sign in the real world or Object Plane
know_width = 14.3
#colors
GREEN = (0,255,0)
RED = (0,0,255)
WHITE = (255,255,255)
fontText = cv2.FONT_HERSHEY_SIMPLEX

cap = cv2.VideoCapture(0)

# Stop Sign Cascade Classifier xml
# stop_sign = cv2.CascadeClassifier('cascade_stop_sign.xml')
# Test diff xml
stop_sign = cv2.CascadeClassifier('stop_sign_classifier_2.xml')
turnRight_sign = cv2.CascadeClassifier('turnLeft_ahead[1].xml')

def FocalLength(measured_distance, real_width, width_in_rf_image):
    focal_length = (width_in_rf_image*measured_distance)/real_width
    return focal_length

#distance estimation func
def Distance_finder(Focal_length, real_sign_width, sign_width_in_frame):
    distance = (real_sign_width * Focal_length)/sign_width_in_frame
    return distance

def TrafficSign_Stop(img):
    traffic_sign_width = 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in stop_sign_scaled:
        # Draw rectangle around the stop sign
        stop_sign_rectangle = cv2.rectangle(img, (x,y),
                                            (x+w, y+h),
                                            GREEN, 3)
        traffic_sign_width = w
        # Write "Stop sign" on the bottom of the rectangle
        stop_sign_text = cv2.putText(img=stop_sign_rectangle,
                                    text="Stop Sign",
                                    org=(x, y+h+30),
                                    fontFace=fontText,
                                    fontScale=1, color=RED,
                                    thickness=2, lineType=cv2.LINE_4)
    return traffic_sign_width

def TrafficSign_TurnRight(img):
    traffic_sign_width = 0
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    turnRight_sign_scaled = turnRight_sign.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in turnRight_sign_scaled:
        # Draw rectangle around the stop sign
        turnRight_sign_rectangle = cv2.rectangle(img, (x,y),
                                            (x+w, y+h),
                                            GREEN, 3)
        traffic_sign_width = w
        # Write "Stop sign" on the bottom of the rectangle
        turnRight_sign_text = cv2.putText(img=turnRight_sign_rectangle,
                                    text="Turn Right Sign",
                                    org=(x, y+h+30),
                                    fontFace=fontText,
                                    fontScale=1, color=RED,
                                    thickness=2, lineType=cv2.LINE_4)
    return traffic_sign_width

ref_image = cv2.imread("stop.png")
ref_image_sign_width = TrafficSign_Stop(ref_image)
Focal_length_StopSign_found = FocalLength(know_distacne, know_width, ref_image_sign_width)
print(Focal_length_StopSign_found)
cv2.imshow("ref_image", ref_image)
abc = cv2.imread("D:/customhaar2/p/024_0001.png")
az = TrafficSign_TurnRight(abc)
cv2.imshow("zz", abc)

while cap.isOpened():
    _, img = cap.read()
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # stop_sign_scaled = stop_sign.detectMultiScale(gray, 1.3, 5)

    # # Detect the stop sign, x,y = origin points, w = width, h = height
    # for (x, y, w, h) in stop_sign_scaled:
    #     # Draw rectangle around the stop sign
    #     stop_sign_rectangle = cv2.rectangle(img, (x,y),
    #                                         (x+w, y+h),
    #                                         (0, 255, 0), 3)
    #     # Write "Stop sign" on the bottom of the rectangle
    #     stop_sign_text = cv2.putText(img=stop_sign_rectangle,
    #                                 text="Stop Sign",
    #                                 org=(x, y+h+30),
    #                                 fontFace=cv2.FONT_HERSHEY_SIMPLEX,
    #                                 fontScale=1, color=(0, 0, 255),
    #                                 thickness=2, lineType=cv2.LINE_4)
    # Distance = Distance_finder(Focal_length=)
    traffic_sign_stop_width_in_frame = TrafficSign_Stop(img)
    # if traffic_sign_stop_width_in_frame != 0:
    #     Distance = Distance_finder(Focal_length_StopSign_found, know_width, traffic_sign_stop_width_in_frame)
    #     cv2.putText(img, f"Distance: {Distance}", (50,50), fontText, 0.6,(RED),2)
    traffic_sign_turnRight_width_in_frame = TrafficSign_TurnRight(img)

    cv2.imshow("img", img)
    key = cv2.waitKey(30)
    if key == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
