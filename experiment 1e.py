import cv2, numpy as np
img=cv2.imread("exp1e.png",0)
e=cv2.erode(img,np.ones((5,5),np.uint8),1)
cv2.imshow("Erode",e)
cv2.waitKey(0)
