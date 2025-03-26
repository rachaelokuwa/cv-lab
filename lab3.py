import cv2
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('data/robot_010.png', cv2.IMREAD_GRAYSCALE)
kernel = np.ones((7,7),np.float32)/49
# Define the kernel and flip it for true convolution
kernel = np.ones((7, 7), np.float32) / 49


flipped_kernel = cv2.flip(kernel, -1, kernel)  # Flip the kernel before applying

# Apply the convolution using the flipped kernel
img_conv = cv2.filter2D(img, -1, flipped_kernel) # for a true convolution, the k3ernal must be flipped left-right and up-down before being applied
# the flipping matters only for non-symmetrical (directional) kernels, like edge-detection filters.

sobel_x = np.array([[1, 0, -1], #meant to detect vertical edges 
                    [2, 0, -2],
                    [1, 0, -1]])
sobel_y = np.array([[1, 2, 1], #detects horizontal edges
                    [0, 0, 0],
                    [-1, -2, -1]])

sobel_x_flipped = cv2.flip(np.array(sobel_x), -1)
sobel_y_flipped = cv2.flip(np.array(sobel_y), -1)

# Apply convolution using both original and flipped kernels
img_sobel_x = cv2.filter2D(img, -1, sobel_x)  # Not flipped
img_sobel_y = cv2.filter2D(img, -1, sobel_y)  # Not flipped

img_sobel_x_flipped = cv2.filter2D(img, -1, sobel_x_flipped)  # Flipped
img_sobel_y_flipped = cv2.filter2D(img, -1, sobel_y_flipped)  # Flipped

fig, axs = plt.subplots(1, 4, figsize = (10, 5)) 

# Plot
fig, axs = plt.subplots(2, 3, figsize=(12, 8))

# Original Image
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].axis('off')
axs[0, 0].set_title('Original Image')

# Sobel X without flip
axs[0, 1].imshow(img_sobel_x, cmap='gray')
axs[0, 1].axis('off')
axs[0, 1].set_title('Sobel X (No Flip)')

# Sobel Y without flip
axs[0, 2].imshow(img_sobel_y, cmap='gray')
axs[0, 2].axis('off')
axs[0, 2].set_title('Sobel Y (No Flip)')

# Sobel X with flip
axs[1, 1].imshow(img_sobel_x_flipped, cmap='gray')
axs[1, 1].axis('off')
axs[1, 1].set_title('Sobel X (Flipped)')

# Sobel Y with flip
axs[1, 2].imshow(img_sobel_y_flipped, cmap='gray')
axs[1, 2].axis('off')
axs[1, 2].set_title('Sobel Y (Flipped)')

# Hide empty subplot
axs[1, 0].axis('off')


#excercise 2 


#Derivative filters (Prewitt, Sobel...) give values for edge strength
#Canny delivers a binary mask

# Calculate the Sobel gradients with explicit conversion to float32
img_sobel_x = cv2.Sobel(img, cv2.CV_32F, 1, 0, ksize=3)
img_sobel_y = cv2.Sobel(img, cv2.CV_32F, 0, 1, ksize=3)

# Calculate the gradient magnitude
magnitude = cv2.magnitude(img_sobel_x, img_sobel_y) # combines both to get the magnitude

# Normalize for visualization
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX)

# Calculate the gradient direction in degrees
angle = cv2.phase(img_sobel_x, img_sobel_y, angleInDegrees=True)

fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Original Image
axs[0].imshow(img, cmap='gray')
axs[0].axis('off')
axs[0].set_title('Original Image')

# Magnitude of the Gradient
axs[1].imshow(magnitude, cmap='gray')
axs[1].axis('off')
axs[1].set_title('Gradient Magnitude')

# Gradient Direction
axs[2].imshow(angle, cmap='gray')# cmap as hsv? who knows... 
axs[2].axis('off')
axs[2].set_title('Gradient Direction')

plt.tight_layout()
plt.show()


plt.tight_layout()
plt.show()
plt.show()