import cv2
import matplotlib.pyplot as plt

image = cv2.imread("image.jpg")
resized = cv2.resize(image, (256, 256))
gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
resized_rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

plt.subplot(1, 2, 1)
plt.imshow(resized_rgb)
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(gray, cmap='gray')
plt.title("Grayscale")
plt.axis('off')

plt.show()
