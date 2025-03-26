import cv2
import numpy as np


img = cv2.imread('data/mixture_01_800.jpg')
#img = cv2.imread('data/sdcards_01_800.jpg')
#img = cv2.imread('data/coins_01_800.jpg')
#img = cv2.imread('data/testOval.jpg')





img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


                    # coins   # general  # sd       # mixture
lower_hue = 0     # 100     # 0        # 100        # 0
upper_hue = 10     # 140     # 180      # 170       # 10

lower_sat = 100      # 80      # 100      # 80      # 100
upper_sat = 255     # 255     # 255      # 255      # 255

lower_val = 150       # 30      # 50       # 3      # 150 or 50
upper_val = 255     # 255     # 255      # 255      # 255

# Apply thresholds on the HSV channels to create masks
hue_mask = cv2.inRange(img_hsv, (lower_hue, 0, 0), (upper_hue, 255, 255))
sat_mask = cv2.inRange(img_hsv, (0, lower_sat, 0), (179, upper_sat, 255))
val_mask = cv2.inRange(img_hsv, (0, 0, lower_val), (179, 255, upper_val))

# Combine masks using logical AND to combine conditions
combined_mask = cv2.bitwise_and(hue_mask, sat_mask)
combined_mask = cv2.bitwise_and(combined_mask, val_mask)



# Find contours
contours, hierarchy = cv2.findContours(combined_mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# Print the number of detected objects
print(f"Number of detected contours: {len(contours)}")
# Draw contours on a blank canvas
output_img = np.zeros((combined_mask.shape[0], combined_mask.shape[1], 3), dtype=np.uint8)
cv2.drawContours(output_img, contours, -1, (255, 128, 0), 2)
# Show the result
cv2.imshow("Contours", output_img)




strel2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))


# Execute an erosion using the structuring element
img_eroded = cv2.erode(combined_mask, strel2, iterations=1) #increasing iterations to 3 improves gfaps in coins, but so does tweaking bounds
# Execute a dilation using the structuring element  # ruins picture of coins but imrpoves for sd cards. 3 iterations for sd cards imrpves. loooks better for mixture
img_dilated = cv2.dilate(combined_mask, strel2, iterations=1)
#closing
sdilated = cv2.dilate(img_eroded, strel2, iterations=1)  

test = img_eroded # change and for mixture, dillated is the best one for some reason 

# Find contours
contours, hierarchy = cv2.findContours(test, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
# Print the number of detected objects
print(f"Number of detected contours: {len(contours)}")
# Draw contours on a blank canvas
test_img = np.zeros((test.shape[0], test.shape[1], 3), dtype=np.uint8)
cv2.drawContours(test_img, contours, -1, (255, 128, 0), 2)
# Show the result
cv2.imshow("Contours x", test_img)










for i, cnt in enumerate(contours):
    # Bounding Box (axis-aligned)
    x, y, w, h = cv2.boundingRect(cnt)

    # Rotated Bounding Box
    box = cv2.minAreaRect(cnt)
    box_points = np.int32(cv2.boxPoints(box))  # Convert to int for drawing

    # Area (filled region)
    area = cv2.contourArea(cnt)

    # Perimeter (arc length)
    perimeter = cv2.arcLength(cnt, True)

    # Convex Hull
    hull = cv2.convexHull(cnt)
    convex_area = cv2.contourArea(hull)

    # Enclosing Circle
    (cx, cy), radius = cv2.minEnclosingCircle(cnt)
    enclosing_circle_area = np.pi * (radius ** 2)

    # Enclosing Triangle
    _, triangle_points = cv2.minEnclosingTriangle(cnt)

    # Moments (to find centroid)
    moments = cv2.moments(cnt)
    if moments["m00"] != 0:
        centroid_x = int(moments["m10"] / moments["m00"])
        centroid_y = int(moments["m01"] / moments["m00"])
    else:
        centroid_x, centroid_y = 0, 0

    # --- Circle / Oval Classification ---
    circularity = (4 * np.pi * area) / (perimeter ** 2) if perimeter > 0 else 0
    aspect_ratio = w / h  # Width / Height

    if circularity > 0.85 and 0.9 <= aspect_ratio <= 1.1:
        shape = "Circle"
    elif circularity > 0.5 and (aspect_ratio < 0.9 or aspect_ratio > 1.1):
        shape = "Oval"
    else:
        shape = "Other"

    print(f"Contour {i}:")
    print(f"  - Bounding Box: x={x}, y={y}, width={w}, height={h}")
    print(f"  - Area: {area}, Perimeter: {perimeter}")
    print(f"  - Convex Hull Area: {convex_area}")
    print(f"  - Enclosing Circle: Centre=({cx},{cy}), Radius={radius}")
    print(f"  - Centroid: ({centroid_x}, {centroid_y})")
    print(f"  - Circularity: {circularity:.2f}, Aspect Ratio: {aspect_ratio:.2f}")
    print(f"  - Classified as: {shape}")

    # Draw Bounding Boxes
    cv2.rectangle(output_img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.drawContours(output_img, [box_points], 0, (255, 0, 0), 2)  # Rotated Box

    # Draw text for classification
    cv2.putText(output_img, shape, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

cv2.imshow("Contour Properties", output_img)


cv2.waitKey(0)
cv2.destroyAllWindows()