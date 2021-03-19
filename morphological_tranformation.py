import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('smarties.jpg', cv2.IMREAD_GRAYSCALE)

titles = ['image']
images = [img]

for i in range(1):
    plt.subplot(1, 1, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()