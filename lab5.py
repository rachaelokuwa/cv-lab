# finally some texture stuff

import cv2
import numpy as np

img = cv2.imread('data/satellite.png')
img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Defining ROI
x, y, w, h = 100, 200, 50, 50  # coords
a, b, l, m = 200, 300, 75, 75
roi = img_grey[y:y+h, x:x+w]
roi2 = img_grey[b:b+m, a:a+l]

# Draw the ROI on the image
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.rectangle(img, (a, b), (a + l, b + m), (0, 255, 0), 2)

# Display the image with the ROI
cv2.imshow("Region of Interest", img)
#plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


def get_stats(roi,L=256):
    """Calculate statistical texture features for a given region of interest (roi)
    roi: 2D numpy array representing the region of interest
    L: number of gray levels
    return: mean,variance,r,skewness,uniformity,entropy
    """

    hist = np.histogram(roi, bins=L, range=(0, L),density=True)
    mean = 0
    uniformity=0.0
    entropy=0.0

    for i in range(0,L):
        mean = mean + float(i)*hist[0][i]
        uniformity = uniformity + hist[0][i]**2
        entropy = entropy - hist[0][i]*np.log2(hist[0][i]+1e-6)
    
    # Calculate the moments
    # m[n] = nth moment. NB m[0] is always 1 and m[1] is always 0

    m=np.zeros(5)
    for n in range(0,5):
        for zi in range(0,L):
            m[n] += (float(zi)-mean)**n*hist[0][zi]


    variance = m[2]
    normalised_variance = variance/((L-1)**2)
    r = 1-(1/(1+normalised_variance))
    skewness = m[3]
    flatness = m[4]

    return mean,variance,r,skewness,flatness,uniformity,entropy

# Calculate statistics for the selected region
mean, variance, r, skewness, flatness, uniformity, entropy = get_stats(roi)
mean2, variance2, r2, skewness2, flatness2, uniformity2, entropy2 = get_stats(roi2)

# Print results
print("ROI 1")
print(f"Mean: {mean}")
print(f"Variance: {variance}")
print(f"R-value: {r}")
print(f"Skewness: {skewness}")
print(f"Flatness: {flatness}")
print(f"Uniformity: {uniformity}")
print(f"Entropy: {entropy}")

print("ROI 2")
print(f"Mean: {mean2}")
print(f"Variance: {variance2}")
print(f"R-value: {r2}")
print(f"Skewness: {skewness2}")
print(f"Flatness: {flatness2}")
print(f"Uniformity: {uniformity2}")
print(f"Entropy: {entropy2}")



cv2.waitKey(0)
cv2.destroyAllWindows()