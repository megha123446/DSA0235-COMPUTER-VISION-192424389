import cv2, numpy as np

img=cv2.imread("image.png")

p1=np.float32([[50,50],[200,50],[50,200]])
p2=np.float32([[10,100],[200,50],[100,250]])

M=cv2.getAffineTransform(p1,p2)
a=cv2.warpAffine(img,M,(300,300))

cv2.imshow("Affine",a)
cv2.waitKey(0)
