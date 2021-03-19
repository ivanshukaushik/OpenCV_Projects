import numpy as np
import cv2

img = cv2.imread('lena.jpg', 1)
# img = np.zeros([512, 512, 3], np.uint8) # To make the entire image black

img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)  # BGR
img = cv2.arrowedLine(img, (255, 255), (400, 400), (255, 0, 0), 5)  # Arrowed Line

img = cv2.rectangle(img, (50, 50), (200, 200), (100, 100, 100), 5)  # Draw Rectangle, Give -1 for filled rectangle

img = cv2.circle(img, (200, 200), 20, (120, 120, 120), 5)  # Draw a circle
font = cv2.FONT_HERSHEY_COMPLEX
img = cv2.putText(img, 'Hello world', (10, 500), font, 2, (255, 255, 255), 5, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
