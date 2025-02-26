import cv2
import numpy as np
from matplotlib import pyplot as plt
print("OpenCV version ",cv2.__version__)



# Colour OpenCV uses BGR rather than RGB !!
# Image Comparison
#img1 = cv2.imread('data/testtest1.jpg') # Load the file from disk into an image
# img2 = cv2.imread('data/testtest2.jpg') # Load the file from disk into an image
# img3 = cv2.imread('data/testtest3.jpg') # Load the file from disk into an image
# img4 = cv2.imread('data/testtest4.jpg') # Load the file from disk into an image 

# # the below shows multiple images on the same window using the matplotlib library 
# fig,axs = plt.subplots(nrows=1,ncols=3) # this displays the images horizontally. for vertical, switch the numbers around
# axs[0].imshow(img1)
# axs[0].title.set_text('Original Image')
# axs[0].axis('off')
# axs[1].imshow(img2,cmap='gray')
# axs[1].title.set_text('Greyscale Image')
# axs[1].axis('off')
# axs[2].imshow(img1)
# axs[2].title.set_text('Original Image')
# axs[2].axis('off')
# plt.show()

# # the below plots the images as a grid. it has to be a 2d array if you think about it 
# fig,axs = plt.subplots(nrows=2,ncols=2) # this displays the images horizontally. for vertical, switch the numbers around
# axs[0, 0].imshow(img1)  # First row, first column
# axs[0, 0].title.set_text('Level 25')
# axs[0, 0].axis('off')
# axs[0, 1].imshow(img2, cmap='gray')  # First row, second column
# axs[0, 1].title.set_text('Level 50')
# axs[0, 1].axis('off')
# axs[1, 0].imshow(img3)  # Second row, first column
# axs[1, 0].title.set_text('Level 75')
# axs[1, 0].axis('off')
# axs[1, 1].imshow(img4)  # Second row, second column
# axs[1, 1].title.set_text('Level 100')
# axs[1, 1].axis('off')
# plt.show()

# Cropping

# img1 = cv2.imread('data/test01.jpg') # Load the file from disk into an image
# img2 = img1[50:100, 100:300] # slicing data from the main image. starts at the top left and were extracting 50 pixels tall and 200 wide starting at 50, 100. 
# #(careful not to get all these axis stuff mixed up!!)

# figure,axes = plt.subplots(nrows=1,ncols=2)
# axes[0].imshow(img1)
# axes[0].title.set_text('Original Image')
# axes[0].axis('off')
# axes[1].imshow(img2)
# axes[1].title.set_text('Cropped Image')
# axes[1].axis('off')
# plt.show()


# Resizing Images
#  
# shrinking and increasing data is tricky because shrinking loses data, and when enlarging, data must be created

# img1 = cv2.imread('data/test01.jpg') # Load the file from disk into an image
# img2 = cv2.resize(img1, (100,100)) # here what was a 500px square becomes a 100x100 px square

# figure,axes = plt.subplots(nrows=1,ncols=2)
# axes[0].imshow(img1)
# axes[0].title.set_text('Original Image')
# axes[0].axis('off')
# axes[1].imshow(img2)
# axes[1].title.set_text('Shrunk Image')
# axes[1].axis('off')
# plt.show()

# img1 = cv2.imread('data/test01.jpg') # Load the file from disk into an image
# img2 = cv2.resize(img1, (1000,500)) # here what was a 500px square becomes a 100x100 px square

# figure,axes = plt.subplots(nrows=1,ncols=2)
# axes[0].imshow(img1)
# axes[0].title.set_text('Original Image')
# axes[0].axis('off')
# axes[1].imshow(img2)
# axes[1].title.set_text('Enlarged Image')
# axes[1].axis('off')
# plt.show()


#  Greyscale

#img2 = cv2.imread('data/test01.jpg', cv2.IMREAD_GRAYSCALE) # presents the image as a gryscale, meaning it will only have one channel. 
# the img.shape[2] will be out of bounds because of this
#cv2.imshow('Test 01', img) # Create a window and show the image

# Image Quality

# the below changes the level of quality that a jpeg is saved as (jpeg is lossy png is lossless)
#cv2.imwrite('data/testtest4.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100]) # replace 75 with different values between 0 and 100


# Annotation
# img1 = cv2.imread('data/test01.jpg')
# img2 = cv2.putText(img1, 'Annotated Image', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1,
# (128, 128, 255), 2, cv2.LINE_AA)  # the text is positioned at point 50,50, but keep in mind this time its (col, row) format! The text is drawn to the right and up of the coord. 
# # the 1 is the scale of the font ie size. the (128,128,255) is the colour of the text (a shade of pink, in this case), in BGR values. the 2 is the line thickness and the last param sorts the line smoothness?
# #just stick to this cv2.LINE_AA
# cv2.imshow('Annotated Image', img2) # Create a window and show the image

# # can also draw points, lines, circles (ellipses), rectangles and polylines on your images. Shapes can be filled or open.

# img3 = cv2.putText(img1, 'Annotated Image', (50, 400), cv2.FONT_HERSHEY_SIMPLEX,
# 1, (128, 128, 255), 2)
# cv2.line(img3, (0, 0), (300, 300), (255, 0, 255), 2)
# cv2.rectangle(img3, (50, 50), (200, 200), (0, 255, 0), 2)
# cv2.rectangle(img3, (220, 50), (300, 200), (192, 64, 128),-1)
# cv2.circle(img3, (300, 300), 50, (255, 0, 0), 3)
# cv2.circle(img3, (100, 300), 50, (128, 255, 255),-1)
# pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# pts = pts.reshape((-1, 1, 2))
# cv2.polylines(img3, [pts], True, (0, 0, 255), 2)

# cv2.imshow('Annotated Image', img3)

# Image Properties

## the below outputs some useful info about the code
# print(f'Image shape: {img.shape[0]}x{img.shape[1]} pixels')
# print(f'Number of channels: {img.shape[2]}')
# print(f'Image size: {img.size} bytes')
# print(f'Image data type: {img.dtype}')


# Creating Images

import cv2
import numpy as np
new_img = np.zeros((500, 500, 3), np.uint8) # creates a new numpy array of 500, 500 and 3 and puts the value of 0 into each cell. np.uint8 is the data type of the element stored in each cell
# for RGB image, use unsigned 8 bit integer data. can use a single channel for a greyscale image, and this can be 8 bit integer or float data. 
# can also manipulate the individual data elements in the arrays, and these will show up on the images

cv2.imshow('Blank image', new_img)

# Create a BGR image (value of each channel is 0 to 255)
new_img[100:200, 100:200,0] = 128
new_img[150:250, 150:250,1] = 128
new_img[200:300, 200:300,2] = 128
new_img[300:400, 300:400, 0:3] = 192
cv2.imshow('RGB image', new_img)
# Create an 8-bit grey scale image (brightness from 0 to 255)
new_img2 = np.zeros((500, 500, 1), np.uint8)
new_img2[200:300, 200:300] = 128
cv2.imshow('Int greyscale image', new_img2)
# Create a float grey scale image (brightness from 0.0 to 1.0)
new_img3 = np.zeros((500, 500, 1), np.float32)
new_img3[200:300, 200:300] = 0.5
cv2.imshow('Float greyscale image', new_img3)


cv2.waitKey() # Wait for the user to press a key