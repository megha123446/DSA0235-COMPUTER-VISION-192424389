import cv2, numpy as np

img=cv2.imread("image.png")

M=np.float32([[1,0,100],[0,1,50]])
move=cv2.warpAffine(img,M,(img.shape[1],img.shape[0]))

cv2.imshow("Moved",move)
cv2.waitKey(0)
