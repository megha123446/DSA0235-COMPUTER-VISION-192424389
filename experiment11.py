import cv2,numpy as np
img=cv2.imread('image.png')
M=np.eye(3)
out=cv2.warpPerspective(img,M,(img.shape[1],img.shape[0]))
cv2.imshow('DLT',out);cv2.waitKey(0)
