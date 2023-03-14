import cv2
import numpy as np

def printDotArray(frame, contours):
    counter = 0;
    cv2.rectangle(frame, (0, 0),(480, 480),(0,0,255),5)
    for i in range(8):
        for j in range(8):
            centerupper = ((480//8)*i + 30 + 10,(480//8)*j + 30 + 10)
            centerlower = ((480//8)*i + 30 - 10,(480//8)*j + 30 - 10)
            if(np.abs(cv2.pointPolygonTest(contours, centerupper, True)) < 30 and
               np.abs(cv2.pointPolygonTest(contours, centerlower, True)) < 30):
                cv2.circle(frame, ((480//8)*i + 30,(480//8)*j + 30),10,(238, 245, 37),-1)
                counter = counter + 1
            else:
                cv2.circle(frame, ((480//8)*i + 30,(480//8)*j + 30),10,(0,0,255),-1)
    return counter;

    

# 0 denotes capture from webcam - may need to change for robosub.
video = cv2.VideoCapture(0)

l_b = np.array([88, 78, 74])  # lower hsv bound for green
u_b = np.array([130, 100, 100])  # upper hsv bound to red
cx, cy = 0, 0
while True:
    ret, frame = video.read()
    width = frame.shape[0]
    height = frame.shape[1]
    approx = 0
    print(str(width) + ", " + str(height))
    
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    mask = cv2.inRange(hsv, l_b, u_b)  # color range to look for

    contours, _ = cv2.findContours(
        mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)  # finds contours of object
    print(str(contours))
    if (contours):  # run only if there are contours found (prevents crashing)
        max_contour = contours[0]
        for contour in contours:
            if cv2.contourArea(contour) > cv2.contourArea(max_contour):
                max_contour = contour
            contour = max_contour
            approx = cv2.approxPolyDP(
                contour, 0.01*cv2.arcLength(contour, True), True)  # approximates the contour making it simpler for the box to be drawn around
            # set the x, y, width and height to bound approximations
            x, y, w, h = cv2.boundingRect(approx)

        # bounding box around object
        rect = cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
        # centroid dot
        center = cv2.circle(frame, (cx, cy), 10, (0, 255, 0), -1)
        # c centroid label
        cv2.putText(rect, str(cx) + ", " + str(cy), (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
        # frame width and height label
        

        M = cv2.moments(contour)  # for finding the centroid of the rectangle
        if M["m00"] != 0:  # ensures no division by zero
            cx = int(M["m10"] / M["m00"])
            cy = int(M["m01"] / M["m00"])
        else:
            cx, cy = 0, 0

    # array of dots for gripper cam resolution
        num_green = printDotArray(frame,approx)
        cv2.putText(frame, str(num_green), 
                    (width//3 - 20, height//3 - 10),cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
    cv2.imshow("feed", frame)
    # show the mask feed
    cv2.imshow("mask", mask)

    # quit key
    c = cv2.waitKey(1)
    if c == 27:
        break
cv2.destroyAllWindows()
