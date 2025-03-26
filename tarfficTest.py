import cv2
import numpy as np
from matplotlib import pyplot as plt



source = cv2.imread('data/traffic2.jpg', cv2.IMREAD_COLOR)
source_rgb = cv2.cvtColor(source, cv2.COLOR_BGR2RGB)
source_hsv = cv2.cvtColor(source, cv2.COLOR_BGR2HSV)
img_blue = cv2.inRange(source_hsv, (90, 50, 50), (130, 255, 255))
img_blue_sat = cv2.inRange(source_hsv, (110, 5, 50), (130, 255, 255))
img_blue_sat_light = cv2.inRange(source_hsv, (110, 100, 100), (130, 255, 255))
masked = cv2.bitwise_and(source_rgb, source_rgb, mask=img_blue_sat_light)



fig,axs = plt.subplots(1,5, figsize=(15, 5))

axs[0].imshow(source_rgb)
axs[0].set_title("Original Image")
axs[0].axis('off')

axs[1].imshow(img_blue, cmap="gray")
axs[1].set_title("Blue Mask")
axs[1].axis('off')

axs[2].imshow(img_blue_sat, cmap="gray")
axs[2].set_title("Blue + Sat Mask")
axs[2].axis('off')

axs[3].imshow(img_blue_sat_light, cmap="gray")
axs[3].set_title("Blue + Sat + Light Mask")
axs[3].axis('off')

axs[4].imshow(masked)
axs[4].set_title("Masked Image")
axs[4].axis('off')


plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()