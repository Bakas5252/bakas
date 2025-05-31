import cv2
import matplotlib.pyplot as plt

main_img = cv2.imread("scene.jpg")
template = cv2.imread("template.jpg")
result = cv2.matchTemplate(main_img, template, cv2.TM_CCOEFF_NORMED)

_, _, _, max_loc = cv2.minMaxLoc(result)
h, w = template.shape[:2]
cv2.rectangle(main_img, max_loc, (max_loc[0]+w, max_loc[1]+h), (255,0,0), 2)

plt.imshow(cv2.cvtColor(main_img, cv2.COLOR_BGR2RGB))
plt.title("Template Matched")
plt.axis('off')
plt.show()
