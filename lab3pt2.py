import cv2
import numpy as np
from matplotlib import pyplot as plt


# excercise 3

img = cv2.imread('data/robot_010.png', cv2.IMREAD_COLOR)
# Now convert the image to RGB rather than BGR, for convenience when plotting it
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# Create a new image the same size as the original
new_img = np.zeros(img.shape, np.uint8)
blue_img = np.zeros(img.shape, np.uint8)
yellow_img = np.zeros(img.shape, np.uint8)

# Iterate over the pixels in the image
# (i.e. the elements in the underlying array)
# and mark red pixels in the new image
#cv2.imshow('colour red', new_img)

# # Remember OpenCV 's colour channels are B,G,R so the red channel is index 2 but didnt we convert to rgb so its now colour channel 0 
# for i in range(img.shape[0]):
#     for j in range(img.shape[1]):
#         # Channel 0 is red in RGB format
#         if img[i,j,0] >= 140:
#             new_img[i,j,0] = 255
# # Code to show images is omitted for brevity. You know how to do that.

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        # Channel 0 is red, 1 is green and 2 is blue
        if img[i,j,0] >= 140 and img[i,j,1] <= 100 and img[i,j,2] <= 100:
            new_img[i,j,0] = 255


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        # Channel 0 is red, 1 is green and 2 is blue
        if img[i,j,2] >= 140 and img[i,j,1] <= 200 and img[i,j,0] <= 200:
            blue_img[i,j,2] = 255


for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        # Channel 0 is red, 1 is green and 2 is blue
        if img[i,j,0] >= 140 and img[i,j,1] >= 140 and img[i,j,2] <= 100:
            yellow_img[i,j,0] = 255
            yellow_img[i,j,1] = 255





# Display the original and the processed images side by side using matplotlib
fig, axs = plt.subplots(1, 4, figsize=(10, 5))

axs[0].imshow(img)
axs[0].axis('off')
axs[0].set_title('Original Image')

axs[1].imshow(new_img)
axs[1].axis('off')
axs[1].set_title('Red Pixels Marked')

axs[2].imshow(blue_img)
axs[2].axis('off')
axs[2].set_title('Blue Pixels Marked')

axs[3].imshow(yellow_img)
axs[3].axis('off')
axs[3].set_title('Yellow Pixels Marked')

plt.show()

