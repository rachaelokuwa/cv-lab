import cv2
import numpy as np

cv2.destroyAllWindows()


# Default values
hue, hue_range = 0, 180  
min_sat, max_sat = 0, 255  
min_val, max_val = 0, 255  
has_changed = True

def set_hue(x):
    global hue, has_changed
    hue = x
    has_changed = True

def set_hue_range(x):
    global hue_range, has_changed
    hue_range = x
    has_changed = True

def set_min_saturation(x):
    global min_sat, has_changed
    min_sat = x
    has_changed = True

def set_max_saturation(x):
    global max_sat, has_changed
    max_sat = x
    has_changed = True

def set_min_value(x):
    global min_val, has_changed
    min_val = x
    has_changed = True

def set_max_value(x):
    global max_val, has_changed
    max_val = x
    has_changed = True

# Load the image
img = cv2.imread('data/robot_010_sm.png', cv2.IMREAD_COLOR)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Create a window for trackbars
cv2.namedWindow('HSV Selector')

# Trackbars
cv2.createTrackbar('Hue', 'HSV Selector', hue, 179, set_hue)
cv2.createTrackbar('Hue Range', 'HSV Selector', hue_range, 180, set_hue_range)
cv2.createTrackbar('Min Saturation', 'HSV Selector', min_sat, 255, set_min_saturation)
cv2.createTrackbar('Max Saturation', 'HSV Selector', max_sat, 255, set_max_saturation)
cv2.createTrackbar('Min Value', 'HSV Selector', min_val, 255, set_min_value)
cv2.createTrackbar('Max Value', 'HSV Selector', max_val, 255, set_max_value)

while True:
    if has_changed:
        has_changed = False

        # Calculate hue range
        min_hue = max(0, hue - hue_range)
        max_hue = min(179, hue + hue_range)

        lower_bound = np.array([min_hue, min_sat, min_val])
        upper_bound = np.array([max_hue, max_sat, max_val])

        mask = cv2.inRange(img_hsv, lower_bound, upper_bound)
        result = cv2.bitwise_and(img, img, mask=mask)

        cv2.imshow('HSV Selector', result)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


# not sure this is fully corrcet but red shows ar 179 but not 0 
cv2.destroyAllWindows()
