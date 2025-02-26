import cv2
import numpy as np
from matplotlib import pyplot as plt


# Load the image in grayscale
img = cv2.imread('data/test01_noisy.jpg', cv2.IMREAD_GRAYSCALE)

# Define different kernels for experimentation
kernel1 = [[1/9, 1/9, 1/9],
            [1/9, 1/9, 1/9],
                    [1/9, 1/9, 1/9]]  # Blurring kernel


kernel2 = [[ 0, 1/6, 0],
                    [1/6, 2/6, 1/6],
                    [ 0, 1/6, 0]]  # Slight edge enhancement

kernel3 = [[-1, 0, 1],
                   [-1, 0, 1],
                   [-1, 0, 1]] # enhancing vertical lines


# Apply convolution with different kernels

img_blur =  cv2.filter2D(img, -1, np.array(kernel1)) # performs the convolution.  the kernal array has to be a numpy arras for the filter2d to work
img_sharpen = cv2.filter2D(img, -1, np.array(kernel2))
filter_noise = cv2.medianBlur(img, 3) # median filtering- it removes noise quite good actually
img_lines = cv2.filter2D(img, -1, np.array(kernel3))

#Plot original and filtered images
fig, axs = plt.subplots(2, 3, figsize=(15, 10))

axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].axis('off')
axs[0, 0].set_title('Original Image')

axs[0, 1].imshow(img_blur, cmap='gray')
axs[0, 1].axis('off')
axs[0, 1].set_title('Blurred Image (3x3)')

axs[0, 2].imshow(img_sharpen, cmap='gray')
axs[0, 2].axis('off')
axs[0, 2].set_title('Sharpened Image')

axs[1, 0].imshow(img_lines, cmap='gray')
axs[1, 0].axis('off')
axs[1, 0].set_title('Enhance Vertical Lines')

axs[1, 1].imshow(filter_noise, cmap='gray')
axs[1, 1].axis('off')
axs[1, 1].set_title('Filtering Noise')

plt.tight_layout()
plt.show()


# fig, axs = plt.subplots(1, 3)

# axs[0].imshow(img, cmap='gray')
# axs[0].axis('off')
# axs[0].set_title('Original Image')

# axs[1].imshow(img_blur, cmap='gray')
# axs[1].axis('off')
# axs[1].set_title('Blurred Image (3x3)')

# axs[2].imshow(img_sharpen, cmap='gray')
# axs[2].axis('off')
# axs[2].set_title('Sharpened Image')


plt.tight_layout()
plt.show()
cv2.waitKey()