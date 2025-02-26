import cv2
print("OpenCV version ",cv2.__version__)
img = cv2.imread('data/coins.png') # Load the file from disk into an image
#img = cv2.imread('data/coins.png', cv2.IMREAD_GRAYSCALE) # presents the image as a gryscale, meaning it will only have one channel. 
# the img.shape[2] will be out of bounds because of this
object
cv2.imshow('Test 01', img) # Create a window and show the image
#cv2.imwrite('data/testtest4.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100]) # replace 75 with different values between 0 and 100
print(f'Image shape: {img.shape[0]}x{img.shape[1]} pixels')
print(f'Number of channels: {img.shape[2]}')
print(f'Image size: {img.size} bytes')
print(f'Image data type: {img.dtype}')


cv2.waitKey() # Wait for the user to press a key