import cv2
import numpy as np

video = cv2.VideoCapture(0)

classNames = []
classFile = "coco.names"
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

while True:
    ret, frame = video.read()
    cv2.imshow("video",frame)
    r = frame[:,:,2:]
    g = frame[:,:,1:2]
    b = frame[:,:,:1]
    # imageROI = cv2.selectROI(frame)
    # cv2.imshow("roi",imageROI)
    
    #dividing up video region
    (h, w)= frame.shape[:2]
    width, height = (w // 2),(h // 2)
    # sq1 = frame[0:width,0:height]
    # sq2 = frame[0:width,0:height]
    # cv2.imshow("sq1",sq1)
    # cv2.imshow("sq2",sq2)
    
    #find the mean
    r_mean = np.mean(r)
    g_mean = np.mean(g)
    b_mean = np.mean(b)

    
    # quit key
    c = cv2.waitKey(1)
    if c == 27:
        break
    
    #display the most prominant color:
    if(b_mean > g_mean and g_mean > r_mean):
        print("Blue")
    elif(g_mean > b_mean and b_mean > r_mean):
        print("Green")
    else:
        print("Red")
cv2.destroyAllWindows()