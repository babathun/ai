import cv2
import matplotlib.pyplot as plt
img = cv2.imread('image.jpg')
plt.imshow(img)
plt.title('car')
plt.axis('off')
plt.show()
