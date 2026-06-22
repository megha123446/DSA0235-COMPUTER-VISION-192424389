import cv2
img=cv2.imread('image.png',0)
cv2.imshow('Canny',cv2.Canny(img,100,200));cv2.waitKey(0)
