import cv2
img=cv2.imread('image.png',0)
cv2.imshow('Lap',cv2.Laplacian(img,cv2.CV_64F));cv2.waitKey(0)
