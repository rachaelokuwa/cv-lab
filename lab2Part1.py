import cv2
import numpy as np
from matplotlib import pyplot as plt

# Tasks 1-3

img = cv2.imread('data/test05.jpg', cv2.IMREAD_GRAYSCALE)

hist_data = np.zeros(256) # create an array to store the results - one element for each possible grey value

# Iterate over the pixels in the image
# (i.e. the elements in the underlying array)
# and increment the correct cell in the histogram array
for i in range(img.shape[0]):  # //the part above and this can be replaced with hist_data = cv2.calcHist([img], [0], None, [256], [0, 256])
    for j in range(img.shape[1]):
        hist_data[img[i,j]] += 1
# Create an array big enough to hold the histogram image
#100 is the height of the histogram
hist_img = np.zeros([100,256])


# Draw the histogram by setting the correct pixels
# Use python array slicing to do this, rather than
# graphics primitives such as drawing lines
for i in range(256):    
    hist_img[0:100,i] = 255
    hist_img[90:100,i] = i
    hist_img[0:int(hist_data[i]/max(hist_data)*100),i] = 0


# fig,axs = plt.subplots(1,2)

# axs[0].imshow(img, cmap = 'gray')
# axs[0].axis('off')
# axs[1].imshow(hist_img, cmap = 'gray')
# axs[1].invert_yaxis()
# plt.show()


# Calculate the cumulative desnsity function (CDF)
cdf = np.cumsum(hist_data)
cdf_normalized = cdf / cdf[-1] * 100  # Normalize to 100

# Create an image for the CDF
cdf_img = np.zeros([100, 256])

# Plot CDF
for i in range(256):
    cdf_img[0:int(cdf_normalized[i]), i] = 255  # Set pixels for CDF plot

# Create two subplots: one for the histogram and one for the CDF
fig, axs = plt.subplots(1, 3, figsize = (10, 5)) #figsize=(12, 6)

# Plot original image
axs[0].imshow(img, cmap='gray')
axs[0].axis('off')
axs[0].set_title('Original Image')

# Plot histogram
axs[1].imshow(hist_img, cmap='gray')
axs[1].invert_yaxis()
axs[1].set_title('Histogram')

# axs[1].hist(img.ravel(), bins=256, range=[0, 256], color='black')
# axs[1].set_title('Histogram')
# axs[1].set_xlim([0, 256]) #// can use this as well

# Plot CDF
axs[2].imshow(cdf_img, cmap='gray') #// can use this as well  axs[0].hist(img.ravel(), bins=256, range=[0,256], cumulative=True, histtype='step')
axs[2].invert_yaxis()
axs[2].set_title('Cumulative Distrubution Function')

plt.show()
Load the image in grayscale


cv2.waitKey()
