import cv2
import numpy as np
from matplotlib import pyplot as plt

# Read the image
img = cv2.imread('data/robot_010_sm.png', cv2.IMREAD_COLOR)

# Convert the image to grayscale
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Otsu's thresholding
threshold, image = cv2.threshold(gray_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)



# Plotting the original, grayscale, and thresholded images
fig, axs = plt.subplots(1, 3, figsize=(15, 5))
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title("Original Image")
axs[0].axis('off')

axs[1].imshow(gray_img, cmap='gray')
axs[1].set_title("Grayscale Image")
axs[1].axis('off')

axs[2].imshow(image, cmap='gray')
axs[2].set_title("Thresholded Image (Otsu)")
axs[2].axis('off')

plt.show()

