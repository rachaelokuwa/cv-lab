import cv2
import numpy as np

# Load image
img = cv2.imread('data/mixture_01_800.jpg')
#img = cv2.imread('data/coins_01_800.jpg')

# Convert to HSV (Hue, Saturation, Value)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Set threshold values for Hue, Saturation, and Value channels
# (These values will depend on the color of the objects and the background)
# Hue value based on colour, saturation for varying saturations of colours, and value for object brightness
                    # coins   # general  # sd       # mixture
lower_hue = 0     # 100     # 0        # 100        # 0
upper_hue = 10     # 140     # 180      # 170       # 10

lower_sat = 100      # 80      # 100      # 80      # 100
upper_sat = 255     # 255     # 255      # 255      # 255

lower_val = 50       # 30      # 50       # 3      # 150 or 50
upper_val = 255     # 255     # 255      # 255      # 255



# Apply thresholds on the HSV channels to create masks
hue_mask = cv2.inRange(img_hsv, (lower_hue, 0, 0), (upper_hue, 255, 255))
sat_mask = cv2.inRange(img_hsv, (0, lower_sat, 0), (179, upper_sat, 255))
val_mask = cv2.inRange(img_hsv, (0, 0, lower_val), (179, 255, upper_val))


# # Thresholding each channel
# hue_mask = cv2.inRange(img_hsv, (lower_hue, 0, 0), (upper_hue, 255, 255))
# sat_mask = cv2.inRange(img_hsv, (0, lower_sat, 0), (180, upper_sat, 255))
# val_mask = cv2.inRange(img_hsv, (0, 0, lower_val), (180, 255, upper_val))



# Combine masks using logical AND to combine conditions
combined_mask = cv2.bitwise_and(hue_mask, sat_mask)
combined_mask = cv2.bitwise_and(combined_mask, val_mask)




# Show the thresholded images
# cv2.imshow("Hue Mask", hue_mask)
# cv2.imshow("Saturation Mask", sat_mask)
# cv2.imshow("Value Mask", val_mask)
cv2.imshow("Combined Mask", combined_mask) # THIS IS the one we care about



# # Invert the combined mask to get the foreground (objects)  # DOESNT WORK 
# foreground_mask = cv2.bitwise_not(combined_mask)

# # Apply the mask to the original image to get the foreground
# foreground = cv2.bitwise_and(img, img, mask=foreground_mask)

# # Show the foreground image (isolated objects)
# cv2.imshow("Foreground", foreground)

# Wait until a key is pressed, then close all windows





# Manually create a 5X5 structuring element approximating a circle
strel1 =[[0, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
        [0, 1, 1, 1, 0]]

# Do the same thing using a built in function
strel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))


# Execute an erosion using the structuring element
img_eroded = cv2.erode(combined_mask, strel2, iterations=1) #increasing iterations to 3 improves gfaps in coins, but so does tweaking bounds

# Execute a dilation using the structuring element  # ruins picture of coins but imrpoves for sd cards. 3 iterations for sd cards imrpves. loooks better for mixture
img_dilated = cv2.dilate(combined_mask, strel2, iterations=1)



cv2.imshow("Eroded", img_eroded)
cv2.imshow("Dilated", img_dilated)

sdilated = cv2.dilate(img_eroded, strel2, iterations=1)  
cv2.imshow("Closing", sdilated)








cv2.waitKey(0)
cv2.destroyAllWindows()



