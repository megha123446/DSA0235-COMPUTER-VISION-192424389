import cv2
img=cv2.imread('image.png',0)
cv2.imshow('Gradient',cv2.morphologyEx(img,cv2.MORPH_GRADIENT,None));cv2.waitKey(0)
