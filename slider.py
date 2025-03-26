import cv2
import numpy as np


minred=0
has_changed=True

def sliderCallback(x):
    # need to declare variables used callbacks and main program as global
    global minred
    global has_changed
    minred=x
    has_changed=True
    print(x)


img=cv2.imread('data/robot_010_sm.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
new_img=np.zeros(img.shape, np.uint8)

cv2.namedWindow('Tracker sample',cv2.WINDOW_AUTOSIZE)
cv2.createTrackbar('Red', 'Tracker sample', 0, 255, sliderCallback)


while(1):
    # Only process the image if the slider value has changed
    if has_changed:
        has_changed=False
        for i in range(img.shape[0]):
            for j in range(img.shape[1]):
                if img[i,j,0] >= minred:
                    new_img[i,j,2] = 255
                else:
                    new_img[i,j,2] = 0
        cv2.imshow('Tracker sample', new_img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cv2.destroyAllWindows()