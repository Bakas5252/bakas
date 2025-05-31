import cv2
import numpy as np
import matplotlib.pyplot as plt

fg = cv2.imread("greenscreen.jpg")
bg = cv2.imread("beach.jpg")
bg = cv2.resize(bg, (fg.shape[1], fg.shape[0]))

hsv = cv2.cvtColor(fg, cv2.COLOR_BGR2HSV)
lower_green = np.array([35, 100, 100])
upper_green = np.array([85, 255, 255])
mask = cv2.inRange(hsv, lower_green, upper_green)

mask_inv = cv2.bitwise_not(mask)
fg_part = cv2.bitwise_and(fg, fg, mask=mask_inv)
bg_part = cv2.bitwise_and(bg, bg, mask=mask)
final = cv2.add(fg_part, bg_part)

plt.imshow(cv2.cvtColor(final, cv2.COLOR_BGR2RGB))
plt.title("Green Screen Replacement")
plt.axis('off')
plt.show()
