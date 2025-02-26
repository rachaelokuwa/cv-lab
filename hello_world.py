import cv2
print("OpenCV version ",cv2.__version__)
img = cv2.imread('data/testtest4.jpg') # Load the file from disk into an image
object
cv2.imshow('Test 01', img) # Create a window and show the image
#cv2.imwrite('data/testtest4.jpg', img, [cv2.IMWRITE_JPEG_QUALITY, 100]) # replace 75 with different values between 0 and 100
cv2.waitKey() # Wait for the user to press a key



