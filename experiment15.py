import cv2
img=cv2.imread('image.png',0)
cv2.imshow('SobelXY',cv2.Sobel(img,cv2.CV_64F,1,1));cv2.waitKey(0)
