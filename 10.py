import cv2
import random
import matplotlib.pyplot as plt

cap = cv2.VideoCapture("video.mp4")
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print("Total frames:", frame_count)

random_frames = random.sample(range(frame_count), 5)

for i in random_frames:
    cap.set(cv2.CAP_PROP_POS_FRAMES, i)
    ret, frame = cap.read()
    if ret:
        plt.imshow(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        plt.title(f"Frame {i}")
        plt.axis('off')
        plt.show()

cap.release()
