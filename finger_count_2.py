import numpy as np
import cv2


def skin_mask(img_mask):
    hsvim = cv2.cvtColor(img_mask, cv2.COLOR_BGR2HSV)
    lower = np.array([0, 48, 80], dtype="uint8")
    upper = np.array([20, 255, 255], dtype="uint8")
    skinRegionHSV = cv2.inRange(hsvim, lower, upper)
    blurred = cv2.blur(skinRegionHSV, (2, 2))
    ret, thresh = cv2.threshold(blurred, 0, 255, cv2.THRESH_BINARY)
    return thresh


cap = cv2.VideoCapture(0)

while True:
    img = cap.read()
    mask = skin_mask(img)
    cv2.imshow('masked', mask)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
