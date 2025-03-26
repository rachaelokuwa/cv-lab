#prewitt filter for edge detection

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('data/test04.jpg', cv2.IMREAD_GRAYSCALE)


gx = np.array([ [1, 0, -1], #meant to detect horizontal edges
                [1, 0, -1],
                [1, 0, -1]])    
gy = np.array([ [1, 1, 1], #detects vertical edges
                [0, 0, 0],
                [-1, -1, -1]])   

#can be combined using pythag...
fgx = cv2.flip(gx, -1,) # we must flip kernals that arent symmetric, ie theyre directional in order to perform true cconvolution
fgy = cv2.flip(gy, -1)

flipped_kernel = cv2.flip(gx, -1)  # Flip the kernel before applying
imgFlipped = cv2.filter2D(img, -1, fgx)  # Flipped

# prewittGX= cv2.filter2D(img, -1, fgx)
prewittGY= cv2.filter2D(img, -1, fgy)




fig, axs = plt.subplots(1, 3, figsize=(12, 8))
# Original Image
axs[0].imshow(img, cmap='gray')
axs[0].axis('off')
axs[0].set_title('Original Image')

# Prewitt X 
axs[1].imshow(imgFlipped, cmap='gray')
axs[1].axis('off')
axs[1].set_title('Prewitt X ')

# Prewitt Y 
axs[2].imshow(prewittGY, cmap='gray')
axs[2].axis('off')
axs[2].set_title('Prewitt Y')

plt.show()
# what a mess