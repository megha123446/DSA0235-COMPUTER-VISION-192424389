import cv2
img=cv2.imread('image.png',0)
cv2.imshow('SobelX',cv2.Sobel(img,cv2.CV_64F,1,0));cv2.waitKey(0)
