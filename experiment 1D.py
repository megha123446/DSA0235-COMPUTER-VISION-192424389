import cv2, numpy as np
img=cv2.imread("exp1d.png",0)
d=cv2.dilate(img,np.ones((5,5),np.uint8),1)
cv2.imshow("Dilate",d)
cv2.waitKey(0)
