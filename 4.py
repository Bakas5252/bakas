import cv2
import matplotlib.pyplot as plt

image = cv2.imread("object.jpg", cv2.IMREAD_GRAYSCALE)
edges = cv2.Canny(image, 100, 200)

plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(edges, cmap='gray')
plt.title("Canny Edges")
plt.axis('off')

plt.show()
