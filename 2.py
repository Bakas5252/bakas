import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
blur = cv2.GaussianBlur(image, (5, 5), 0)

kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
sharpened = cv2.filter2D(image, -1, kernel)

images = [image, blur, sharpened]
titles = ["Original", "Blurred", "Sharpened"]

plt.figure(figsize=(12, 4))
for i in range(3):
    plt.subplot(1, 3, i+1)
    rgb = cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB)
    plt.imshow(rgb)
    plt.title(titles[i])
    plt.axis('off')
plt.show()
