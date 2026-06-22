import cv2
img=cv2.imread('image.png')
b=cv2.GaussianBlur(img,(9,9),10)
cv2.imshow('HighBoost',cv2.addWeighted(img,2,b,-1,0));cv2.waitKey(0)
