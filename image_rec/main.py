import cv2
import numpy as np

video = cv2.VideoCapture(0)

while True:
    ret, frame = video.read()
    cv2.imshow("video",frame)
    r = frame[:,:,2:]
    g = frame[:,:,1:2]
    b = frame[:,:,:1]
    
    #find the mean
    r_mean = np.mean(r)
    g_mean = np.mean(g)
    b_mean = np.mean(b)
    
    #display the most prominant color:
    if(b_mean > g_mean and g_mean > r_mean):
        print("Blue")
    elif(g_mean > b_mean and b_mean > r_mean):
        print("Green")
    else:
        print("Red")
