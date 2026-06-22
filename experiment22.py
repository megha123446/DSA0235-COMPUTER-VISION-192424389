import cv2
img=cv2.imread('image.png')
cv2.putText(img,'WATERMARK',(50,50),0,1,(255,255,255),2)
cv2.imshow('WM',img);cv2.waitKey(0)
