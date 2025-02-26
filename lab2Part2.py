import cv2
import numpy as np
from matplotlib import pyplot as plt

# Task 4-5
# Load the image in grayscale
img = cv2.imread('data/test05.jpg', cv2.IMREAD_GRAYSCALE)

# Step 1: Calculate the histogram
hist_data = cv2.calcHist([img], [0], None, [256], [0, 256])

# Step 2: Compute the cumulative distribution function (CDF)
cum_hist = hist_data.cumsum()

# Step 3: Normalize the CDF to the range [0, 255]
cdf_normalized = (cum_hist - cum_hist.min()) * 255 / (cum_hist.max() - cum_hist.min())

# Step 4: Apply the transfer function to the original image
img_equalized = np.interp(img.ravel(), range(256), cdf_normalized).reshape(img.shape)

# Step 5: Calculate the histogram and CDF of the equalized image
hist_eq = cv2.calcHist([img_equalized.astype(np.uint8)], [0], None, [256], [0, 256])
cum_hist_eq = hist_eq.cumsum()
cdf_eq_normalized = (cum_hist_eq - cum_hist_eq.min()) * 255 / (cum_hist_eq.max() - cum_hist_eq.min())

# Apply OpenCV's built-in equalizer
img_eq = cv2.equalizeHist(img)

# Step 6: Calculate the histogram and CDF of the built-in equalized image
hist_eq_cv = cv2.calcHist([img_eq], [0], None, [256], [0, 256])
cum_hist_eq_cv = hist_eq_cv.cumsum()
cdf_eq_normalized_cv = (cum_hist_eq_cv - cum_hist_eq_cv.min()) * 255 / (cum_hist_eq_cv.max() - cum_hist_eq_cv.min())

# Plotting the original, equalized (manual), and equalized (OpenCV) images, their histograms, and CDFs
fig, axs = plt.subplots(3, 3, figsize=(12, 18))

# Original Image and its histogram
axs[0, 0].imshow(img, cmap='gray')
axs[0, 0].axis('off')
axs[0, 0].set_title('Original Image')

axs[0, 1].hist(img.ravel(), bins=256, range=[0, 256], color='black', histtype='step')
axs[0, 1].set_title('Original Histogram')

# Plot the original CDF
axs[0, 2].plot(cdf_normalized, color='blue', label='Original CDF')
axs[0, 2].set_title('Original CDF')
axs[0, 2].set_xlim([0, 255])
axs[0, 2].set_ylim([0, 255])
axs[0, 2].legend()

# Equalized Image (Manual) and its histogram
axs[1, 0].imshow(img_equalized, cmap='gray')
axs[1, 0].axis('off')
axs[1, 0].set_title('Manual Equalized Image')

axs[1, 1].hist(img_equalized.ravel(), bins=256, range=[0, 256], color='black', histtype='step')
axs[1, 1].set_title('Manual Equalized Histogram')

# Plot the manual equalized CDF
axs[1, 2].plot(cdf_eq_normalized, color='red', label='Manual Equalized CDF')
axs[1, 2].set_title('Manual Equalized CDF')
axs[1, 2].set_xlim([0, 255])
axs[1, 2].set_ylim([0, 255])
axs[1, 2].legend()

# Equalized Image (OpenCV) and its histogram
axs[2, 0].imshow(img_eq, cmap='gray')
axs[2, 0].axis('off')
axs[2, 0].set_title('OpenCV Equalizer')

axs[2, 1].hist(img_eq.ravel(), bins=256, range=[0, 256], color='black', histtype='step')
axs[2, 1].set_title('OpenCV Equalizer Histogram')

# Plot the OpenCV equalized CDF
axs[2, 2].plot(cdf_eq_normalized_cv, color='green', label='OpenCV Equalizer CDF')
axs[2, 2].set_title('OpenCV Equalizer CDF')
axs[2, 2].set_xlim([0, 255])
axs[2, 2].set_ylim([0, 255])
axs[2, 2].legend()

plt.tight_layout()
plt.show()
cv2.waitKey()
