import cv2
import numpy as np
from matplotlib import pyplot as plt
import os
print("OpenCV version ",cv2.__version__)





# # Task One
# img = np.zeros((500, 700, 3), np.uint8) 
# img[100:200, 100:200,0] = 128 #blu
# img[150:250, 175:275,1] = 128 #green
# img[100:200, 250:350,2] = 128 #red
# img[150:250, 325:425, 0:3] = 192 #white


# cv2.imshow('Initial image', img)

# img[:,:] = [255, 255, 255]  # Set background to white [255, 255, 255] in BGR
# img[100:200, 100:200] = [255, 0, 0] #blue_img[150:250, 175:275] = [0, 255, 255]  #yellow
# img[100:200, 250:350] = [0, 0, 0] #black
# img[150:250, 325:425] = [0, 255, 0]  #green
# img[100:200, 400:500] = [0, 0, 255]  # red

# cv2.imshow('RGB image', img)


# new_img = np.zeros((500, 700, 3), np.uint8) 
# new_img[:,:] = [255, 255, 255]  # Set background to white [255, 255, 255] in BGR
# cv2.circle(new_img, (150, 150) , 50, [255, 0, 0], thickness=2)
# cv2.circle(new_img, (225, 200) , 50, [0, 255, 255], thickness=2)
# cv2.circle(new_img, (300, 150) , 50, [0, 0, 0], thickness=2)
# cv2.circle(new_img, (375, 200) , 50, [0, 255, 0], thickness=2)
# cv2.circle(new_img, (450, 150) , 50, [0, 0, 255], thickness=2)


# cv2.imshow('Final image', new_img)


# Task Two



input_folder = "C:/Users/Racha/Downloads/cv_test/data"
output_folder = "C:/Users/Racha/Downloads/cv_test/task2/output"

# Scan for image files
image_files = [f for f in os.listdir(input_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp'))]

for filename in image_files:
    img_path = os.path.join(input_folder, filename)
    
    # Read image
    img = cv2.imread(img_path)

    # Get original dimensions
    h, w = img.shape[:2]

    # Compute new size while maintaining aspect ratio
    if w > h:
        new_w = 250
        new_h = int((250 / w) * h)
    else:
        new_h = 250
        new_w = int((250 / h) * w)

    resized_img = cv2.resize(img, (new_w, new_h))

    # Add text overlay (filename)
    text_position = (10, new_h - 10)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 0.5
    color = (255, 255, 255)  # White text
    thickness = 1
    cv2.putText(resized_img, filename, text_position, font, font_scale, color, thickness)

    # Save the processed image
    output_path = os.path.join(output_folder, filename)
    cv2.imwrite(output_path, resized_img)

    print(f"Processed: {filename}")

print("All images resized and saved successfully!")


# OR

# image_files = [
#     "C:/Users/Racha/Downloads/cv_test/data/test01.jpg",
#     "C:/Users/Racha/Downloads/cv_test/data/test02.jpg",
#     "C:/Users/Racha/Downloads/cv_test/data/test03.jpg",
#     "C:/Users/Racha/Downloads/cv_test/data/test04.jpg",
#     "C:/Users/Racha/Downloads/cv_test/data/test05.jpg",
# ]

# output_folder = "C:/Users/Racha/Downloads/cv_test/task2/output"

# for img_path in image_files:
#     img = cv2.imread(img_path)

#     if img is None:
#         print(f"Skipping {img_path}, could not read.")
#         continue

#     filename = img_path.split("/")[-1]  # Extract filename

#     # Get original dimensions
#     h, w = img.shape[:2]

#     # Compute new size while maintaining aspect ratio
#     if w > h:
#         new_w = 250
#         new_h = int((250 / w) * h)
#     else:
#         new_h = 250
#         new_w = int((250 / h) * w)

#     resized_img = cv2.resize(img, (new_w, new_h))

#     # Add filename text overlay
#     text_position = (10, new_h - 10)
#     font = cv2.FONT_HERSHEY_SIMPLEX
#     font_scale = 0.5
#     color = (255, 255, 255)  # White text
#     thickness = 1
#     cv2.putText(resized_img, filename, text_position, font, font_scale, color, thickness)

#     # Save the processed image
#     cv2.imwrite(output_folder + filename, resized_img)

#     print(f"Processed: {filename}")

# print("All images resized and saved successfully!")



# Task Three

import cv2
import numpy as np

# Image paths (ensure these images exist in your working directory)
image_paths = [
    "data/circles.png", "data/coins.png", "data/lighthouse.png", "data/olympic_rings.png",
    "data/test_save.jpg", "data/comparisonimage.png", "data/test01.jpg", "data/test02.jpg",
    "data/test03.jpg", "data/test04.jpg", "data/test05.jpg", "data/testtest1.jpg",
    "data/testtest2.jpg", "data/testtest3.jpg", "data/testtest4.jpg", "data/circles.png"
]

# Read and resize the images
images = [cv2.resize(cv2.imread(img_path), (200, 200)) for img_path in image_paths]

# Create an empty 800x800 mosaic (all black initially)
mosaic = np.zeros((800, 800, 3), dtype=np.uint8)

# Manually placing images into the 4x4 grid
mosaic[0:200, 0:200] = images[0]    # Image 1
mosaic[0:200, 200:400] = images[1]  # Image 2
mosaic[0:200, 400:600] = images[2]  # Image 3
mosaic[0:200, 600:800] = images[3]  # Image 4

mosaic[200:400, 0:200] = images[4]  # Image 5
mosaic[200:400, 200:400] = images[5]# Image 6
mosaic[200:400, 400:600] = images[6]# Image 7
mosaic[200:400, 600:800] = images[7]# Image 8

mosaic[400:600, 0:200] = images[8]  # Image 9
mosaic[400:600, 200:400] = images[9]# Image 10
mosaic[400:600, 400:600] = images[10]# Image 11
mosaic[400:600, 600:800] = images[11]# Image 12

mosaic[600:800, 0:200] = images[12] # Image 13
mosaic[600:800, 200:400] = images[13]# Image 14
mosaic[600:800, 400:600] = images[14]# Image 15
mosaic[600:800, 600:800] = images[15]# Image 16

# Save the final mosaic image
cv2.imwrite('data/mosaic_800x800.jpg', mosaic)

# Optionally, display the mosaic
cv2.imshow('Mosaic', mosaic)
print("Mosaic saved successfully!")


cv2.waitKey() # Wait for the user to press a key

