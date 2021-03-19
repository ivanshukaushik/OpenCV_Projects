import cv2
import matplotlib.pyplot as plt


img = cv2.imread('lena.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
while True:
    cv2.imshow('image', img)

