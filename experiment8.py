import cv2, numpy as np

img=cv2.imread("image.png")

p1=np.float32([[0,0],[300,0],[0,300],[300,300]])
p2=np.float32([[50,50],[250,0],[0,250],[300,300]])

M=cv2.getPerspectiveTransform(p1,p2)
p=cv2.warpPerspective(img,M,(300,300))

cv2.imshow("Perspective",p)
cv2.waitKey(0)
