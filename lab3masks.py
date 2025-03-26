import cv2
import numpy as np
from matplotlib import pyplot as plt



img = cv2.imread('data/robot_010_sm.png', cv2.IMREAD_COLOR)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# Create a new image the same size as the original
mask_img = np.zeros(img.shape, np.uint8)
# Set a rectangle in the middle of the image to white
mask_img[100:300,100:300] = 255
# This is the part that does the masking
final_img = cv2.bitwise_and(img, mask_img)



## for final masking task
# Set threshold values for V channel (brightness)
vmin = 100
vmax = 255

# Apply threshold on V channel
ret_img, ret_thresh = cv2.threshold(img[:,:,2], vmin, vmax, cv2.THRESH_BINARY)





fig,axs = plt.subplots(1,4)
axs[0].imshow(img)

axs[1].imshow(mask_img,cmap='gray')
axs[2].imshow(final_img)
axs[3].imshow(ret_thresh)


plt.show()
