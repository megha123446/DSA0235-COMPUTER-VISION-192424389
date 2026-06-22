import cv2
img=cv2.imread('image.png')
c=img[50:200,50:200]
img[0:150,0:150]=c
cv2.imshow('CropCopy',img);cv2.waitKey(0)
