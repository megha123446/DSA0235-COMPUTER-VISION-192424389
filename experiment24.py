
import cv2,numpy as np
img=cv2.imread('image.png',0)
k=np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
cv2.imshow('Boundary',cv2.filter2D(img,-1,k));cv2.waitKey(0)
