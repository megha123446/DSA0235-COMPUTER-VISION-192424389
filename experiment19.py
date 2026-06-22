import cv2
img=cv2.imread('image.png')
b=cv2.GaussianBlur(img,(9,9),10)
cv2.imshow('Unsharp',cv2.addWeighted(img,1.5,b,-0.5,0));cv2.waitKey(0)
