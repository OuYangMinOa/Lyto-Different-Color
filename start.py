import numpy as np
import cv2
from mss import mss
from PIL import Image

def find_different(arr):
    for num,i in enumerate(arr):
        if (arr.count(i)==1):
            return num
    else:
        return 0
        
mon = {'top': 179, 'left': 706, 'width': 1214-706, 'height': 1080-179}

sct = mss()

while 1:
    sct.get_pixels(mon)
    img = np.array(Image.frombytes('RGB', (sct.width, sct.height), sct.image))
    
    
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT,1.2,10)
    
    if circles is not None:
        # convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")
        # loop over the (x, y) coordinates and radius of the circles
        this = []
        for (x, y, r) in circles:
            this.append(list(img[y,x,:]))
            # draw the circle in the output image, then draw a rectangle
            # corresponding to the center of the circle
        #print(circles)
        nn = find_different(this)
        for num,(x, y, r) in enumerate(circles):
            if num==nn:
                cv2.circle(img, (x, y), r, (0, 255, 0), 4)
                cv2.rectangle(img, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
            
        
            
    cv2.imshow('test', np.array(img))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break







